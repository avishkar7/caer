#    _____           ______  _____ 
#  / ____/    /\    |  ____ |  __ \
# | |        /  \   | |__   | |__) | Caer - Modern Computer Vision
# | |       / /\ \  |  __|  |  _  /  Languages: Python, C, C++
# | |___   / ____ \ | |____ | | \ \  http://github.com/jasmcaus/caer
#  \_____\/_/    \_ \______ |_|  \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Caer Authors <http://github.com/jasmcaus>


import cv2 as cv 

from ..adorad import Tensor, to_tensor
from ._constants import HSV2BGR, HSV2RGB
from ._bgr import bgr2gray, bgr2lab, bgr2hls

__all__ = [
    'hsv2rgb',
    'hsv2bgr',
    'hsv2lab',
    'hsv2gray',
    'hsv2hls'
]

def _is_hsv_image(img):
    # img = to_tensor(img)
    # return img.is_hsv()
    return len(img.shape) == 3 and img.shape[-1] == 3


def hsv2rgb(img) -> Tensor:
    r"""
        Converts a HSV Tensor to its RGB version.

    Args:
        img (Tensor): Valid HSV Tensor
    
    Returns:
        RGB Tensor of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_hsv_image(img):
        raise ValueError(f'Tensor of shape 3 expected. Found shape {len(img.shape)}. This function converts a HSV Tensor to its RGB counterpart')

    im = cv.cvtColor(img, HSV2RGB)
    return to_tensor(im, cspace='rgb')


def hsv2bgr(img) -> Tensor:
    r"""
        Converts a HSV Tensor to its BGR version.

    Args:
        img (Tensor): Valid HSV Tensor
    
    Returns:
        BGR Tensor of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_hsv_image(img):
        raise ValueError(f'Tensor of shape 3 expected. Found shape {len(img.shape)}. This function converts a HSV Tensor to its BGR counterpart')

    im = cv.cvtColor(img, HSV2BGR)
    return to_tensor(im, cspace='bgr')


def hsv2gray(img) -> Tensor:
    r"""
        Converts a HSV Tensor to its Grayscale version.

    Args:
        img (Tensor): Valid HSV Tensor
    
    Returns:
        Grayscale Tensor of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_hsv_image(img):
        raise ValueError(f'Tensor of shape 3 expected. Found shape {len(img.shape)}. This function converts a HSV Tensor to its Grayscale counterpart')

    bgr = hsv2bgr(img)

    im = bgr2gray(bgr)
    return to_tensor(im, cspace='gray')


def hsv2hls(img) -> Tensor:
    r"""
        Converts a HSV Tensor to its HLS version.

    Args:
        img (Tensor): Valid HSV Tensor
    
    Returns:
        HLS Tensor of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_hsv_image(img):
        raise ValueError(f'Tensor of shape 3 expected. Found shape {len(img.shape)}. This function converts a HSV Tensor to its HLS counterpart')

    bgr = hsv2bgr(img)

    im = bgr2hls(bgr)
    return to_tensor(im, cspace='hls')


def hsv2lab(img) -> Tensor:
    r"""
        Converts a HSV Tensor to its LAB version.

    Args:
        img (Tensor): Valid HSV Tensor
    
    Returns:
        LAB Tensor of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_hsv_image(img):
        raise ValueError(f'Tensor of shape 3 expected. Found shape {len(img.shape)}. This function converts a HSV Tensor to its LAB counterpart')

    bgr = hsv2bgr(img)

    im = bgr2lab(bgr)
    return to_tensor(im, cspace='lab')