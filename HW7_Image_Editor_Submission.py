# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Instrctions:
#Run the code below.
#Click on Load and give the path for your file. Loacal or web path will work.
# Click on Show to see the image.
#Click on other buttons to see the effects.
# Only challenge I have is as I could not make the wx work the images are shown in different window and not in the image_editor
# box. I tried several ways but could not make it work.
# Also couple of methods for image transformation are having some challenges which worked fine indiviually I left it in 
# the main code to show the work.

# <codecell>

from traits.api import *
from traitsui.api import *
from PIL import Image
import io
from PIL import Image
import os, sys
import numpy as np
import scipy
import pylab
import pymorph
import mahotas
import urllib
import io
from scipy import ndimage
from PIL import ImageFilter, ImageEnhance
from pyface.image_resource import ImageResource


link=[]

# print path

# class ImageDisplay(HasTraits):
#     Image = Image()
#     view= View( Item('Image', show_label=True, springy=True, style='custom' ))




def image_read(path):
#     print url
    if path.startswith("http"):
        image_url=path
        fd=urllib.urlopen(image_url)
#         print type(fd)
        image_file = io.BytesIO(fd.read())
#         print type(image_file)
        im0 = Image.open(image_file)
    return im0
    
def image_show(url):
    im1=image_read(url)
    im2=im1.convert('RGB')
#     im2.save("out.png")
    return im2

def contrast(url):
    im=image_read(url)
    im=im.convert('RGB')
    sharpener = ImageEnhance.Contrast(im)
    im1 = sharpener.enhance(2)
    return im1   

def brightner(url):
    im=image_read(url)
    im=im.convert('RGB')
    brightner = ImageEnhance.Brightness(im)
    im1 = brightner.enhance(4)
    return im1

def effect(url):
    im=image_read(url)
    pylab.imshow(im)
    dnaf = ndimage.gaussian_filter(im, 1)
    rmax = pymorph.regmax(dnaf)
    T = mahotas.thresholding.otsu(dnaf)
    seeds,nr_nuclei = ndimage.label(rmax)
    T = mahotas.thresholding.otsu(dnaf)
    T = mahotas.thresholding.otsu(dnaf)
    dist = ndimage.distance_transform_edt(dnaf > T)
    dist = dist.max() - dist
    dist -= dist.min()
    dist = dist/float(dist.ptp()) * 255
    dist = dist.astype(np.uint8)
    nuclei = pymorph.cwatershed(dist, seeds)
    pylab.imshow(nuclei)
#     pylab.save("out.png")
    pylab.show()

def colorscheme(url):
    im=image_read(url)
    pylab.imshow(im)
    dnaf = ndimage.gaussian_filter(im, 1)
    rmax = pymorph.regmax(dnaf)
    seeds,nr_nuclei = ndimage.label(rmax)
    T = mahotas.thresholding.otsu(dnaf)
    dist = ndimage.distance_transform_edt(dnaf > T)
    dist = dist.max() - dist
    dist -= dist.min()
    dist = dist/float(dist.ptp()) * 255
    dist = dist.astype(np.uint8)
    nuclei = pymorph.cwatershed(dist, seeds)
    whole = mahotas.segmentation.gvoronoi(nuclei)
    im0=pylab.imshow(whole)
    pylab.show()

def colortile(url):
    im=image_read(url)
    pylab.imshow(im)
    dnaf = ndimage.gaussian_filter(im, 1)
    rmax = pymorph.regmax(dnaf)
    seeds,nr_nuclei = ndimage.label(rmax)
    T = mahotas.thresholding.otsu(dnaf)
    dist = ndimage.distance_transform_edt(dnaf > T)
    dist = dist.max() - dist
    dist -= dist.min()
    dist = dist/float(dist.ptp()) * 255
    dist = dist.astype(np.uint8)
    nuclei = pymorph.cwatershed(dist, seeds)
    whole = mahotas.segmentation.gvoronoi(nuclei)
    im0=pylab.imshow(whole)
#     pylab.save("out.png")
    pylab.show()

def filter1(url):
    im=image_read(url)
    pylab.imshow(im)
    dnaf = ndimage.gaussian_filter(im, 1)
    T = mahotas.thresholding.otsu(dnaf)
    T = mahotas.thresholding.otsu(dnaf)
    dist = ndimage.distance_transform_edt(dnaf > T)
    dist = dist.max() - dist
    dist -= dist.min()
    dist = dist/float(dist.ptp()) 
    dist = dist.astype(np.uint8)
    pylab.imshow(dist)
#     pylab.save(dist,"out_filter1.png")
    pylab.show()

def filter2(url):
    im=image_read(url)
    pylab.imshow(im)
    dnaf = ndimage.gaussian_filter(im, 1)
    T = mahotas.thresholding.otsu(dnaf)
    T = mahotas.thresholding.otsu(dnaf)
    dist = ndimage.distance_transform_edt(dnaf > T)
    dist = dist.max() - dist
    dist -= dist.min()
    dist = dist/float(dist.ptp()) * 255
    dist = dist.astype(np.uint8)
    pylab.imshow(dist)
#     pylab.save("out_filter2.png")
    pylab.show()

def filter3(url):
    im=image_read(url)
    pylab.imshow(im)
    dnaf = ndimage.gaussian_filter(im, 1)
    T = mahotas.thresholding.otsu(dnaf)
    labeled,nr_objects = ndimage.label(dnaf > T)
    pylab.imshow(labeled)
    pylab.jet()
#     pylab.save("out_filter3.png")
    pylab.show()

def show_im():
    img = ImageResource("/out.png")

class Elements(HasTraits):
    load= Button()
    show= Button()
    contrast=Button()
    brighten= Button()
    effect=Button()
    colortile=Button()
    filter1=Button()
    filter1=Button()
    filter2=Button()
    filter3=Button()
    img = Instance(ImageResource)
    
    
    
    def _load_fired():
        class path(HasTraits):
            path =  Str()
            def _path_changed(self, new):
                link.append(new)
        path().configure_traits()
    
    def _show_fired():
        pth=str(link[-1])
        im4=image_show(pth)
#         im4.save("out.png")
        im4.show()
#         img = Instance(ImageResource)
#         img = ImageResource("/out.png")
    
    def _contrast_fired():
        pth=str(link[-1])
        im4=contrast(pth)
#         im4.save("out_cont.png")
        im4.show()
    
    def _brighten_fired():
        pth=str(link[-1])
        im4=brightner(pth)
#         im4.save("out_bright.png")
        im4.show()
    
    def _effect_fired():
        pth=str(link[-1])
        effect(pth)
        
        
    def _colortile_fired():
        pth=str(link[-1])
        colortile(pth)
        
    def _filter1_fired():
        pth=str(link[-1])
        filter1(pth)
        
    def _filter2_fired():
        pth=str(link[-1])
        filter2(pth)
        
    def _filter3_fired():
        pth=str(link[-1])
        filter3(pth)
    
    
    
    view = View(Item('load',show_label=False ), Item('show',show_label=False ), Item('contrast',show_label=False ),Item('brighten',show_label=False ),
                Item('filter1',show_label=False ),Item('filter2',show_label=False ),Item('filter3',show_label=False),
                Item('img',editor=ImageEditor()))
    def _input_changed(self):
        link.append(self.input)
    
class Container(HasTraits):
    elements = Instance(Elements)
#     display = Instance(ImageDisplay)
#     path= Instance(path)

    view = View(
                Item('elements', style='custom', show_label=False, ),
#                 Item('display', style='custom', show_label=False, ),
#                 Item('path', style='custom', show_label=False, )
            )
container = Container(elements=Elements())
container.configure_traits()

# <codecell>


