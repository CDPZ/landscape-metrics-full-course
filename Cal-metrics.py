# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
from osgeo import gdal
from osgeo import gdalconst


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Calculate metrics for a given raster')