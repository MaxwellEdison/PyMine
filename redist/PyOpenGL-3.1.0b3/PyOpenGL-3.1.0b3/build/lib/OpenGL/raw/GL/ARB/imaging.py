'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_imaging'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_imaging',error_checker=_errors._error_checker)
GL_BLEND_COLOR=_C('GL_BLEND_COLOR',0x8005)
GL_BLEND_EQUATION=_C('GL_BLEND_EQUATION',0x8009)
GL_COLOR_MATRIX=_C('GL_COLOR_MATRIX',0x80B1)
GL_COLOR_MATRIX_STACK_DEPTH=_C('GL_COLOR_MATRIX_STACK_DEPTH',0x80B2)
GL_COLOR_TABLE=_C('GL_COLOR_TABLE',0x80D0)
GL_COLOR_TABLE_ALPHA_SIZE=_C('GL_COLOR_TABLE_ALPHA_SIZE',0x80DD)
GL_COLOR_TABLE_BIAS=_C('GL_COLOR_TABLE_BIAS',0x80D7)
GL_COLOR_TABLE_BLUE_SIZE=_C('GL_COLOR_TABLE_BLUE_SIZE',0x80DC)
GL_COLOR_TABLE_FORMAT=_C('GL_COLOR_TABLE_FORMAT',0x80D8)
GL_COLOR_TABLE_GREEN_SIZE=_C('GL_COLOR_TABLE_GREEN_SIZE',0x80DB)
GL_COLOR_TABLE_INTENSITY_SIZE=_C('GL_COLOR_TABLE_INTENSITY_SIZE',0x80DF)
GL_COLOR_TABLE_LUMINANCE_SIZE=_C('GL_COLOR_TABLE_LUMINANCE_SIZE',0x80DE)
GL_COLOR_TABLE_RED_SIZE=_C('GL_COLOR_TABLE_RED_SIZE',0x80DA)
GL_COLOR_TABLE_SCALE=_C('GL_COLOR_TABLE_SCALE',0x80D6)
GL_COLOR_TABLE_WIDTH=_C('GL_COLOR_TABLE_WIDTH',0x80D9)
GL_CONSTANT_ALPHA=_C('GL_CONSTANT_ALPHA',0x8003)
GL_CONSTANT_BORDER=_C('GL_CONSTANT_BORDER',0x8151)
GL_CONSTANT_COLOR=_C('GL_CONSTANT_COLOR',0x8001)
GL_CONVOLUTION_1D=_C('GL_CONVOLUTION_1D',0x8010)
GL_CONVOLUTION_2D=_C('GL_CONVOLUTION_2D',0x8011)
GL_CONVOLUTION_BORDER_COLOR=_C('GL_CONVOLUTION_BORDER_COLOR',0x8154)
GL_CONVOLUTION_BORDER_MODE=_C('GL_CONVOLUTION_BORDER_MODE',0x8013)
GL_CONVOLUTION_FILTER_BIAS=_C('GL_CONVOLUTION_FILTER_BIAS',0x8015)
GL_CONVOLUTION_FILTER_SCALE=_C('GL_CONVOLUTION_FILTER_SCALE',0x8014)
GL_CONVOLUTION_FORMAT=_C('GL_CONVOLUTION_FORMAT',0x8017)
GL_CONVOLUTION_HEIGHT=_C('GL_CONVOLUTION_HEIGHT',0x8019)
GL_CONVOLUTION_WIDTH=_C('GL_CONVOLUTION_WIDTH',0x8018)
GL_FUNC_ADD=_C('GL_FUNC_ADD',0x8006)
GL_FUNC_REVERSE_SUBTRACT=_C('GL_FUNC_REVERSE_SUBTRACT',0x800B)
GL_FUNC_SUBTRACT=_C('GL_FUNC_SUBTRACT',0x800A)
GL_HISTOGRAM=_C('GL_HISTOGRAM',0x8024)
GL_HISTOGRAM_ALPHA_SIZE=_C('GL_HISTOGRAM_ALPHA_SIZE',0x802B)
GL_HISTOGRAM_BLUE_SIZE=_C('GL_HISTOGRAM_BLUE_SIZE',0x802A)
GL_HISTOGRAM_FORMAT=_C('GL_HISTOGRAM_FORMAT',0x8027)
GL_HISTOGRAM_GREEN_SIZE=_C('GL_HISTOGRAM_GREEN_SIZE',0x8029)
GL_HISTOGRAM_LUMINANCE_SIZE=_C('GL_HISTOGRAM_LUMINANCE_SIZE',0x802C)
GL_HISTOGRAM_RED_SIZE=_C('GL_HISTOGRAM_RED_SIZE',0x8028)
GL_HISTOGRAM_SINK=_C('GL_HISTOGRAM_SINK',0x802D)
GL_HISTOGRAM_WIDTH=_C('GL_HISTOGRAM_WIDTH',0x8026)
GL_MAX=_C('GL_MAX',0x8008)
GL_MAX_COLOR_MATRIX_STACK_DEPTH=_C('GL_MAX_COLOR_MATRIX_STACK_DEPTH',0x80B3)
GL_MAX_CONVOLUTION_HEIGHT=_C('GL_MAX_CONVOLUTION_HEIGHT',0x801B)
GL_MAX_CONVOLUTION_WIDTH=_C('GL_MAX_CONVOLUTION_WIDTH',0x801A)
GL_MIN=_C('GL_MIN',0x8007)
GL_MINMAX=_C('GL_MINMAX',0x802E)
GL_MINMAX_FORMAT=_C('GL_MINMAX_FORMAT',0x802F)
GL_MINMAX_SINK=_C('GL_MINMAX_SINK',0x8030)
GL_ONE_MINUS_CONSTANT_ALPHA=_C('GL_ONE_MINUS_CONSTANT_ALPHA',0x8004)
GL_ONE_MINUS_CONSTANT_COLOR=_C('GL_ONE_MINUS_CONSTANT_COLOR',0x8002)
GL_POST_COLOR_MATRIX_ALPHA_BIAS=_C('GL_POST_COLOR_MATRIX_ALPHA_BIAS',0x80BB)
GL_POST_COLOR_MATRIX_ALPHA_SCALE=_C('GL_POST_COLOR_MATRIX_ALPHA_SCALE',0x80B7)
GL_POST_COLOR_MATRIX_BLUE_BIAS=_C('GL_POST_COLOR_MATRIX_BLUE_BIAS',0x80BA)
GL_POST_COLOR_MATRIX_BLUE_SCALE=_C('GL_POST_COLOR_MATRIX_BLUE_SCALE',0x80B6)
GL_POST_COLOR_MATRIX_COLOR_TABLE=_C('GL_POST_COLOR_MATRIX_COLOR_TABLE',0x80D2)
GL_POST_COLOR_MATRIX_GREEN_BIAS=_C('GL_POST_COLOR_MATRIX_GREEN_BIAS',0x80B9)
GL_POST_COLOR_MATRIX_GREEN_SCALE=_C('GL_POST_COLOR_MATRIX_GREEN_SCALE',0x80B5)
GL_POST_COLOR_MATRIX_RED_BIAS=_C('GL_POST_COLOR_MATRIX_RED_BIAS',0x80B8)
GL_POST_COLOR_MATRIX_RED_SCALE=_C('GL_POST_COLOR_MATRIX_RED_SCALE',0x80B4)
GL_POST_CONVOLUTION_ALPHA_BIAS=_C('GL_POST_CONVOLUTION_ALPHA_BIAS',0x8023)
GL_POST_CONVOLUTION_ALPHA_SCALE=_C('GL_POST_CONVOLUTION_ALPHA_SCALE',0x801F)
GL_POST_CONVOLUTION_BLUE_BIAS=_C('GL_POST_CONVOLUTION_BLUE_BIAS',0x8022)
GL_POST_CONVOLUTION_BLUE_SCALE=_C('GL_POST_CONVOLUTION_BLUE_SCALE',0x801E)
GL_POST_CONVOLUTION_COLOR_TABLE=_C('GL_POST_CONVOLUTION_COLOR_TABLE',0x80D1)
GL_POST_CONVOLUTION_GREEN_BIAS=_C('GL_POST_CONVOLUTION_GREEN_BIAS',0x8021)
GL_POST_CONVOLUTION_GREEN_SCALE=_C('GL_POST_CONVOLUTION_GREEN_SCALE',0x801D)
GL_POST_CONVOLUTION_RED_BIAS=_C('GL_POST_CONVOLUTION_RED_BIAS',0x8020)
GL_POST_CONVOLUTION_RED_SCALE=_C('GL_POST_CONVOLUTION_RED_SCALE',0x801C)
GL_PROXY_COLOR_TABLE=_C('GL_PROXY_COLOR_TABLE',0x80D3)
GL_PROXY_HISTOGRAM=_C('GL_PROXY_HISTOGRAM',0x8025)
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE=_C('GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE',0x80D5)
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE=_C('GL_PROXY_POST_CONVOLUTION_COLOR_TABLE',0x80D4)
GL_REDUCE=_C('GL_REDUCE',0x8016)
GL_REPLICATE_BORDER=_C('GL_REPLICATE_BORDER',0x8153)
GL_SEPARABLE_2D=_C('GL_SEPARABLE_2D',0x8012)
GL_TABLE_TOO_LARGE=_C('GL_TABLE_TOO_LARGE',0x8031)
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glBlendColor(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLenum)
def glBlendEquation(mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glColorSubTable(target,start,count,format,type,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glColorTable(target,internalformat,width,format,type,table):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glColorTableParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glColorTableParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter1D(target,internalformat,width,format,type,image):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter2D(target,internalformat,width,height,format,type,image):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glConvolutionParameterf(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glConvolutionParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glConvolutionParameteri(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glConvolutionParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyColorSubTable(target,start,x,y,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyColorTable(target,internalformat,x,y,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyConvolutionFilter1D(target,internalformat,x,y,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyConvolutionFilter2D(target,internalformat,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetColorTable(target,format,type,table):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetColorTableParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetColorTableParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetConvolutionFilter(target,format,type,image):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetConvolutionParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetConvolutionParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetHistogram(target,reset,format,type,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetHistogramParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetHistogramParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetMinmax(target,reset,format,type,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMinmaxParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMinmaxParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p)
def glGetSeparableFilter(target,format,type,row,column,span):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLboolean)
def glHistogram(target,width,internalformat,sink):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLboolean)
def glMinmax(target,internalformat,sink):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetHistogram(target):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetMinmax(target):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p)
def glSeparableFilter2D(target,internalformat,width,height,format,type,row,column):pass