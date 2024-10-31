# SlothPy
# Copyright (C) 2023 Mikolaj Tadeusz Zychowicz (MTZ)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Optional, Literal

from numpy import ndarray, asarray, zeros, where, outer, sum, hstack, linspace, max, abs, sqrt, complex64, log

from slothpy.core._hessian_object import Hessian
from slothpy._general_utilities._constants import AU_BOHR_CM_1
from slothpy._general_utilities._lapack import _cgemmt, _zgemmt
from slothpy._general_utilities._math_expresions import _lorentzian, _gaussian

def _ir_spectrum(hessian: ndarray, masses_inv_sqrt: ndarray, born_charges: ndarray, start_wavenumber: float, stop_wavenumber: float, convolution: Optional[Literal["lorentzian", "gaussian"]] = "lorentizan", resolution: int = None, fwhm: float = None):
    au_bohr_cm_1 = asarray(AU_BOHR_CM_1, dtype=hessian.dtype)
    hessian_object = Hessian([hessian, outer(masses_inv_sqrt, masses_inv_sqrt)], single_process=True)
    hessian_object._kpoint = asarray([0., 0., 0.], dtype=hessian.dtype)

    start_wavenumber_au = start_wavenumber / au_bohr_cm_1
    stop_wavenumber_au = stop_wavenumber / au_bohr_cm_1
    start_wavenumber_au = start_wavenumber_au * start_wavenumber_au if start_wavenumber_au >= 0 else -start_wavenumber_au * start_wavenumber_au
    stop_wavenumber_au = stop_wavenumber_au * stop_wavenumber_au if stop_wavenumber_au >= 0 else -stop_wavenumber_au * stop_wavenumber_au
    frequencies_squared, eigenvectors = hessian_object.frequencies_squared_eigenvectors(start_wavenumber_au, stop_wavenumber_au)
    frequencies = where(frequencies_squared >= 0, sqrt(abs(frequencies_squared)), -sqrt(abs(frequencies_squared))) * au_bohr_cm_1

    born_charges_weighted = born_charges * masses_inv_sqrt[:, None]
    Z_modes = _cgemmt(eigenvectors, born_charges_weighted) if eigenvectors.dtype == complex64 else _zgemmt(eigenvectors, born_charges_weighted)
    IR_intensities_xyz = (abs(Z_modes)**2)
    IR_intensities_av = sum(IR_intensities_xyz, axis=1)

    frequencies_intensities = hstack((frequencies.reshape(-1, 1), IR_intensities_xyz, IR_intensities_av.reshape(-1, 1))).T
    frequencies_intensities[1:4,:] = frequencies_intensities[1:4,:] / max(frequencies_intensities[1:4,:])
    frequencies_intensities[4,:] = frequencies_intensities[4,:] / max(frequencies_intensities[4,:]) 
    frequency_range_convolution = None

    if convolution is not None:
        frequency_range_convolution = zeros((5, resolution), dtype=hessian.dtype)
        frequency_range_convolution[0, :] = linspace(start_wavenumber, stop_wavenumber, resolution, dtype=hessian.dtype)
    
    #TODO: Move convolutions to numba when you eventually need them in a tight loop for dirac delta functions

        if convolution == "lorentzian":
            gamma = fwhm / 2
            for i in range(1, 5):
                for n in range(len(frequencies_intensities[0, :])):
                    frequency_range_convolution[i, :] += _lorentzian(frequency_range_convolution[0, :], frequencies_intensities[0, n], gamma, frequencies_intensities[i, n])
        
        elif convolution == "gaussian":
            sigma = fwhm / (2 * sqrt(2 * log(2)))
            for i in range(1, 5):
                for n in range(len(frequencies_intensities[0, :])):
                    frequency_range_convolution[i, :] += _gaussian(frequency_range_convolution[0, :], frequencies_intensities[0, n], sigma, frequencies_intensities[i, n])

        frequency_range_convolution[1:4,:] = frequency_range_convolution[1:4,:] / max(frequency_range_convolution[1:4,:])
        frequency_range_convolution[4,:] = frequency_range_convolution[4,:] / max(frequency_range_convolution[4,:])

    return frequencies_intensities, frequency_range_convolution