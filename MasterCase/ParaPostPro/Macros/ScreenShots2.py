#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1074, 806]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.Background = [0.32, 0.34, 0.43]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(0, renderView1)

# Properties modified on renderView1
renderView1.Background = [0.0, 0.0, 0.0]

# split cell
layout1.SplitVertical(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1074, 387]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 0
renderView2.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(2, renderView2)

# Properties modified on renderView2
renderView2.Background = [0.0, 0.0, 0.0]

# split cell
layout1.SplitHorizontal(2, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [532, 387]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.StereoType = 0
renderView3.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(6, renderView3)

# Properties modified on renderView3
renderView3.Background = [0.0, 0.0, 0.0]

# set active view
SetActiveView(renderView1)

# get active source.
fullCarReflect = GetActiveSource()

# set active source
SetActiveSource(fullCarReflect)

# show data in view
fullCarReflectDisplay = Show(fullCarReflect, renderView1)
# trace defaults for the display properties.
fullCarReflectDisplay.Representation = 'Surface'
fullCarReflectDisplay.ColorArrayName = [None, '']
fullCarReflectDisplay.OSPRayScaleArray = 'U'
fullCarReflectDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fullCarReflectDisplay.SelectOrientationVectors = 'None'
fullCarReflectDisplay.ScaleFactor = 0.436339807510376
fullCarReflectDisplay.SelectScaleArray = 'None'
fullCarReflectDisplay.GlyphType = 'Arrow'
fullCarReflectDisplay.GlyphTableIndexArray = 'None'
fullCarReflectDisplay.DataAxesGrid = 'GridAxesRepresentation'
fullCarReflectDisplay.PolarAxes = 'PolarAxesRepresentation'
fullCarReflectDisplay.ScalarOpacityUnitDistance = 0.05310636881446335
fullCarReflectDisplay.SelectInputVectors = ['POINTS', 'U']
fullCarReflectDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fullCarReflectDisplay.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# set active view
SetActiveView(renderView2)

# show data in view
fullCarReflectDisplay_1 = Show(fullCarReflect, renderView2)
# trace defaults for the display properties.
fullCarReflectDisplay_1.Representation = 'Surface'
fullCarReflectDisplay_1.ColorArrayName = [None, '']
fullCarReflectDisplay_1.OSPRayScaleArray = 'U'
fullCarReflectDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
fullCarReflectDisplay_1.SelectOrientationVectors = 'None'
fullCarReflectDisplay_1.ScaleFactor = 0.436339807510376
fullCarReflectDisplay_1.SelectScaleArray = 'None'
fullCarReflectDisplay_1.GlyphType = 'Arrow'
fullCarReflectDisplay_1.GlyphTableIndexArray = 'None'
fullCarReflectDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
fullCarReflectDisplay_1.PolarAxes = 'PolarAxesRepresentation'
fullCarReflectDisplay_1.ScalarOpacityUnitDistance = 0.05310636881446335
fullCarReflectDisplay_1.SelectInputVectors = ['POINTS', 'U']
fullCarReflectDisplay_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fullCarReflectDisplay_1.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView3)

# show data in view
fullCarReflectDisplay_2 = Show(fullCarReflect, renderView3)
# trace defaults for the display properties.
fullCarReflectDisplay_2.Representation = 'Surface'
fullCarReflectDisplay_2.ColorArrayName = [None, '']
fullCarReflectDisplay_2.OSPRayScaleArray = 'U'
fullCarReflectDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
fullCarReflectDisplay_2.SelectOrientationVectors = 'None'
fullCarReflectDisplay_2.ScaleFactor = 0.436339807510376
fullCarReflectDisplay_2.SelectScaleArray = 'None'
fullCarReflectDisplay_2.GlyphType = 'Arrow'
fullCarReflectDisplay_2.GlyphTableIndexArray = 'None'
fullCarReflectDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
fullCarReflectDisplay_2.PolarAxes = 'PolarAxesRepresentation'
fullCarReflectDisplay_2.ScalarOpacityUnitDistance = 0.05310636881446335
fullCarReflectDisplay_2.SelectInputVectors = ['POINTS', 'U']
fullCarReflectDisplay_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fullCarReflectDisplay_2.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView3.ResetCamera()

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView3)

# reset view to fit data
renderView3.ResetCamera()

# set active view
SetActiveView(renderView1)

# set scalar coloring
ColorBy(fullCarReflectDisplay, ('POINTS', 'p'))

# rescale color and/or opacity maps used to include current data range
#fullCarReflectDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fullCarReflectDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.LockDataRange = 1
pLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1000, 1.0, 0.0, 0.0]
pLUT.ColorSpace = 'HSV'
pLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pLUT.NumberOfTableValues = 64
pLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
pLUT.RescaleTransferFunction(-2000.0, 1000.0)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [-2000, 0.0, 0.5, 0.0, 1000, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# Rescale transfer function
pPWF.RescaleTransferFunction(-2000.0, 1000.0)

# set active view
SetActiveView(renderView2)

# set scalar coloring
ColorBy(fullCarReflectDisplay_1, ('POINTS', 'p'))

# rescale color and/or opacity maps used to include current data range
#fullCarReflectDisplay_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
#fullCarReflectDisplay_1.SetScalarBarVisibility(renderView2, True)

# set active view
SetActiveView(renderView3)

# set scalar coloring
ColorBy(fullCarReflectDisplay_2, ('POINTS', 'p'))

# rescale color and/or opacity maps used to include current data range
#fullCarReflectDisplay_2.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
#fullCarReflectDisplay_2.SetScalarBarVisibility(renderView3, True)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.LockDataRange = 1
pLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1000, 1.0, 0.0, 0.0]
pLUT.ColorSpace = 'HSV'
pLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pLUT.NumberOfTableValues = 64
pLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
pLUT.RescaleTransferFunction(-2000.0, 1000.0)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [-2000, 0.0, 0.5, 0.0, 1000, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# Rescale transfer function
pPWF.RescaleTransferFunction(-2000.0, 1000.0)

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)
pLUTColorBar.Title = 'Pressure'
pLUTColorBar.ComponentTitle = '[Pa]'
pLUTColorBar.RangeLabelFormat = '%-#6.1f'

# change scalar bar placement
pLUTColorBar.WindowLocation = 'LowerRightCorner'
pLUTColorBar.ScalarBarLength = 0.23


############################Setup Cam Loop##############

# current camera placement for renderView1
renderView1.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView1.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView1.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView1.CameraParallelScale = 2.54276280729466

# current camera placement for renderView2
renderView2.CameraPosition = [-5.014011031261785, 0.0, 0.7675079703330994]
renderView2.CameraFocalPoint = [4.810470031511043, 0.0, 0.7675079703330994]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 2.5427628072946633

# current camera placement for renderView3
renderView3.CameraPosition = [-0.025547266006469727, 0.0, -5.9307311843986215]
renderView3.CameraFocalPoint = [-0.025547266006469727, 0.0, 3.893749878374207]
renderView3.CameraParallelScale = 2.5427628072946633

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/Press1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# set active view
SetActiveView(renderView1)

############################Setup Cam Loop##############


# current camera placement for renderView1
renderView1.CameraPosition = [-3.5128990775510425, -2.930115880275356, 0.9427178483607985]
renderView1.CameraFocalPoint = [2.641117052980626, 2.298205640384767, 0.09566962794755436]
renderView1.CameraViewUp = [0.09211061201414687, 0.05267769806032644, 0.9943544113048649]
renderView1.CameraParallelScale = 2.54276280729466

# current camera placement for renderView2
renderView2.CameraPosition = [-0.025547266006469727, 0.0, 7.592059929430105]
renderView2.CameraFocalPoint = [-0.025547266006469727, 0.0, -2.2324211333427137]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 2.5427628072946633

# current camera placement for renderView3
renderView3.CameraPosition = [-3.047234746812034, 1.6671847320843867, -1.237125611868069]
renderView3.CameraFocalPoint = [3.4282178135673904, -2.666585178282036, 4.746801247232117]
renderView3.CameraViewUp = [-0.4067720089758329, 0.47209223659076954, 0.7820904377784514]
renderView3.CameraParallelScale = 2.5427628072946633


# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/Press2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

############################Setup Cam Loop##############


# current camera placement for renderView1
renderView1.CameraPosition = [4.004615049832183, -1.800267050337295, -0.007647342275201474]
renderView1.CameraFocalPoint = [-3.6402954829156675, 3.255249649586947, 3.5303636802975724]
renderView1.CameraViewUp = [0.3804147967519827, -0.07009382934986254, 0.9221558639943792]
renderView1.CameraParallelScale = 2.54276280729466

# current camera placement for renderView2
renderView2.CameraPosition = [5.37274847361473, 0.0, 0.7675079703330994]
renderView2.CameraFocalPoint = [-4.451732589158093, 0.0, 0.7675079703330994]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 2.5427628072946633

# current camera placement for renderView3
renderView3.CameraPosition = [-0.025547266006469727, 6.20627329884169, 0.7675079703330994]
renderView3.CameraFocalPoint = [-0.025547266006469727, -3.618207763931148, 0.7675079703330994]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraParallelScale = 2.5427628072946633


# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/Press3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

############################Setup Cam Loop##############


# current camera placement for renderView1
renderView1.CameraPosition = [4.382096544598962, -2.4888179095502325, 2.3422714558002866]
renderView1.CameraFocalPoint = [-4.13191240983388, 4.334493803053219, -2.3767991788657588]
renderView1.CameraViewUp = [-0.22485613270125082, 0.3486982591614691, 0.9098622113509268]
renderView1.CameraParallelScale = 2.54276280729466

# current camera placement for renderView2
renderView2.CameraPosition = [0.09854650143173363, 0.8494349371179011, 2.000449936096998]
renderView2.CameraFocalPoint = [8.650259457578773, -1.1681749787424383, -2.3947615372989453]
renderView2.CameraViewUp = [0.4375779598494829, -0.09349051204551338, 0.8943070240199571]
renderView2.CameraParallelScale = 2.5427628072946633

# current camera placement for renderView3
renderView3.CameraPosition = [-1.5084313121384147, -0.5042177071693742, -2.412406437402338]
renderView3.CameraFocalPoint = [-1.5084313121384147, -0.5042177071693742, 7.412074625370493]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraParallelScale = 2.5427628072946633


# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/Press4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

