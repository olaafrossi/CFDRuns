#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
masterCaseOpenFOAM = GetActiveSource()

# Properties modified on masterCaseOpenFOAM
masterCaseOpenFOAM.IncludeSets = 1
masterCaseOpenFOAM.IncludeZones = 1
masterCaseOpenFOAM.MeshParts = ['internalMesh', 'tireGroup - group', 'wall - group', 'carGroup - group', 'symmetry - group', 'symWall - symmetry', 'outlet - patch', 'upperWall - patch', 'inlet - patch', 'left - patch', 'lowerWall - wall', 'CarBody_wall - wall', 'Splitter_wall - wall', 'Wing_wall - wall', 'Upright_wall - wall', 'RadBody_wall - wall', 'FRTire_wall - wall', 'FRPlinth_wall - wall', 'RRTire_wall - wall', 'RRPlinth_wall - wall']
masterCaseOpenFOAM.VolumeFields = ['k', 'nut', 'omega', 'p', 'total(p)', 'U', 'yPlus', 'wallShearStress']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2094, 913]

# show data in view
masterCaseOpenFOAMDisplay = Show(masterCaseOpenFOAM, renderView1)
# trace defaults for the display properties.
masterCaseOpenFOAMDisplay.Representation = 'Surface'
masterCaseOpenFOAMDisplay.ColorArrayName = [None, '']
masterCaseOpenFOAMDisplay.OSPRayScaleArray = 'U'
masterCaseOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
masterCaseOpenFOAMDisplay.SelectOrientationVectors = 'None'
masterCaseOpenFOAMDisplay.ScaleFactor = 3.0
masterCaseOpenFOAMDisplay.SelectScaleArray = 'None'
masterCaseOpenFOAMDisplay.GlyphType = 'Arrow'
masterCaseOpenFOAMDisplay.GlyphTableIndexArray = 'None'
masterCaseOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
masterCaseOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'
masterCaseOpenFOAMDisplay.SelectInputVectors = ['POINTS', 'U']
masterCaseOpenFOAMDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
masterCaseOpenFOAMDisplay.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Text'
text1 = Text()

# set active source
SetActiveSource(text1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1470, 263]

# show data in view
text1Display = Show(text1, renderView1)

# Properties modified on text1
text1.Text = 'Y=0'

# Properties modified on text1Display
text1Display.WindowLocation = 'UpperLeftCorner'

# set scalar coloring
ColorBy(masterCaseOpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
masterCaseOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.LockDataRange = 1
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1000.0, 1.0, 0.0, 0.0]
vtkBlockColorsLUT.ColorSpace = 'HSV'
vtkBlockColorsLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
vtkBlockColorsLUT.NumberOfTableValues = 64
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# create a new 'STL Reader'
fullCarstl = STLReader(FileNames=['/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/FullCar.stl'])

# Properties modified on renderView1
renderView1.Background = [0.0, 0.0, 0.0]

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitVertical(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [2094, 441]
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
renderView3.ViewSize = [1042, 441]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.StereoType = 0
renderView3.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(6, renderView3)

# Properties modified on renderView3
renderView3.Background = [0.0, 0.0, 0.0]

# set active source
SetActiveSource(fullCarstl)

# get color transfer function/color map for 'STLSolidLabeling'
sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')
sTLSolidLabelingLUT.LockDataRange = 1
sTLSolidLabelingLUT.RGBPoints = [0.0, 0.0, 0.0, 1.0, 1.1757813367477812e-38, 1.0, 0.0, 0.0]
sTLSolidLabelingLUT.ColorSpace = 'HSV'
sTLSolidLabelingLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
sTLSolidLabelingLUT.NumberOfTableValues = 64
sTLSolidLabelingLUT.ScalarRangeInitialized = 1.0

# show data in view
fullCarstlDisplay = Show(fullCarstl, renderView3)
# trace defaults for the display properties.
fullCarstlDisplay.Representation = 'Surface'
fullCarstlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
fullCarstlDisplay.LookupTable = sTLSolidLabelingLUT
fullCarstlDisplay.OSPRayScaleArray = 'STLSolidLabeling'
fullCarstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fullCarstlDisplay.SelectOrientationVectors = 'None'
fullCarstlDisplay.ScaleFactor = 0.4202465057373047
fullCarstlDisplay.SelectScaleArray = 'STLSolidLabeling'
fullCarstlDisplay.GlyphType = 'Arrow'
fullCarstlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
fullCarstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
fullCarstlDisplay.PolarAxes = 'PolarAxesRepresentation'
fullCarstlDisplay.SelectInputVectors = [None, '']
fullCarstlDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fullCarstlDisplay.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# show color bar/color legend
fullCarstlDisplay.SetScalarBarVisibility(renderView3, True)

# reset view to fit data
renderView3.ResetCamera()

# set active view
SetActiveView(renderView2)

# show data in view
fullCarstlDisplay_1 = Show(fullCarstl, renderView2)
# trace defaults for the display properties.
fullCarstlDisplay_1.Representation = 'Surface'
fullCarstlDisplay_1.ColorArrayName = ['CELLS', 'STLSolidLabeling']
fullCarstlDisplay_1.LookupTable = sTLSolidLabelingLUT
fullCarstlDisplay_1.OSPRayScaleArray = 'STLSolidLabeling'
fullCarstlDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
fullCarstlDisplay_1.SelectOrientationVectors = 'None'
fullCarstlDisplay_1.ScaleFactor = 0.4202465057373047
fullCarstlDisplay_1.SelectScaleArray = 'STLSolidLabeling'
fullCarstlDisplay_1.GlyphType = 'Arrow'
fullCarstlDisplay_1.GlyphTableIndexArray = 'STLSolidLabeling'
fullCarstlDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
fullCarstlDisplay_1.PolarAxes = 'PolarAxesRepresentation'
fullCarstlDisplay_1.SelectInputVectors = [None, '']
fullCarstlDisplay_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fullCarstlDisplay_1.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# show color bar/color legend
fullCarstlDisplay_1.SetScalarBarVisibility(renderView2, True)

# reset view to fit data
renderView2.ResetCamera()

# hide color bar/color legend
fullCarstlDisplay_1.SetScalarBarVisibility(renderView2, False)

# set active view
SetActiveView(renderView3)

# hide color bar/color legend
fullCarstlDisplay.SetScalarBarVisibility(renderView3, False)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(masterCaseOpenFOAM)

# create a new 'Slice'
slice1 = Slice(Input=masterCaseOpenFOAM)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [5.0, 4.0, 4.0]

# Properties modified on masterCaseOpenFOAM
masterCaseOpenFOAM.MeshParts = ['internalMesh', 'tireGroup - group', 'wall - group', 'carGroup - group', 'symmetry - group', 'symWall - symmetry', 'outlet - patch', 'upperWall - patch', 'inlet - patch', 'left - patch', 'lowerWall - wall', 'CarBody_wall - wall', 'Splitter_wall - wall', 'Wing_wall - wall', 'Upright_wall - wall', 'RadBody_wall - wall', 'FRTire_wall - wall', 'FRPlinth_wall - wall', 'RRTire_wall - wall', 'RRPlinth_wall - wall']

# show data in view
fullCarstlDisplay_2 = Show(fullCarstl, renderView1)
# trace defaults for the display properties.
fullCarstlDisplay_2.Representation = 'Surface'
fullCarstlDisplay_2.ColorArrayName = ['CELLS', 'STLSolidLabeling']
fullCarstlDisplay_2.LookupTable = sTLSolidLabelingLUT
fullCarstlDisplay_2.OSPRayScaleArray = 'STLSolidLabeling'
fullCarstlDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
fullCarstlDisplay_2.SelectOrientationVectors = 'None'
fullCarstlDisplay_2.ScaleFactor = 0.4202465057373047
fullCarstlDisplay_2.SelectScaleArray = 'STLSolidLabeling'
fullCarstlDisplay_2.GlyphType = 'Arrow'
fullCarstlDisplay_2.GlyphTableIndexArray = 'STLSolidLabeling'
fullCarstlDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
fullCarstlDisplay_2.PolarAxes = 'PolarAxesRepresentation'
fullCarstlDisplay_2.SelectInputVectors = [None, '']
fullCarstlDisplay_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fullCarstlDisplay_2.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# show color bar/color legend
fullCarstlDisplay_2.SetScalarBarVisibility(renderView1, True)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.001, 0.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.001, 0.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.OSPRayScaleArray = 'U'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 3.0
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = ['POINTS', 'U']
slice1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(masterCaseOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'total(p)'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'totalp'
totalpLUT = GetColorTransferFunction('totalp')
totalpLUT.LockDataRange = 1
totalpLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1000.0, 1.0, 0.0, 0.0]
totalpLUT.ColorSpace = 'HSV'
totalpLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
totalpLUT.NumberOfTableValues = 64

# set active source
SetActiveSource(fullCarstl)

# hide data in view
Hide(fullCarstl, renderView1)

# set active source
SetActiveSource(slice1)

# get color legend/bar for totalpLUT in view renderView1
totalpLUTColorBar = GetScalarBar(totalpLUT, renderView1)
totalpLUTColorBar.Title = 'total(p)'
totalpLUTColorBar.ComponentTitle = ''
totalpLUTColorBar.RangeLabelFormat = '%-#6.1f'

# Properties modified on totalpLUTColorBar
totalpLUTColorBar.WindowLocation = 'AnyLocation'

# Properties modified on totalpLUTColorBar
totalpLUTColorBar.WindowLocation = 'LowerRightCorner'
totalpLUTColorBar.ScalarBarLength = 0.23

# Rescale transfer function
totalpLUT.RescaleTransferFunction(-1500.0, 1500.0)

# get opacity transfer function/opacity map for 'totalp'
totalpPWF = GetOpacityTransferFunction('totalp')
totalpPWF.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]
totalpPWF.ScalarRangeInitialized = 1

# Rescale transfer function
totalpPWF.RescaleTransferFunction(-1500.0, 1500.0)

# set active view
SetActiveView(renderView2)

#change interaction mode for render view
renderView2.InteractionMode = '2D'

# Properties modified on renderView2.AxesGrid
renderView2.AxesGrid.Visibility = 1

# set active view
SetActiveView(renderView3)

#change interaction mode for render view
renderView3.InteractionMode = '2D'

# Properties modified on renderView3.AxesGrid
renderView3.AxesGrid.Visibility = 1

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display_1 = Show(slice1, renderView3)
# trace defaults for the display properties.
slice1Display_1.Representation = 'Surface'
slice1Display_1.ColorArrayName = [None, '']
slice1Display_1.OSPRayScaleArray = 'U'
slice1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display_1.SelectOrientationVectors = 'None'
slice1Display_1.ScaleFactor = 3.0
slice1Display_1.SelectScaleArray = 'None'
slice1Display_1.GlyphType = 'Arrow'
slice1Display_1.GlyphTableIndexArray = 'None'
slice1Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice1Display_1.PolarAxes = 'PolarAxesRepresentation'
slice1Display_1.SelectInputVectors = ['POINTS', 'U']
slice1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display_1.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# set active view
SetActiveView(renderView2)

# show data in view
slice1Display_2 = Show(slice1, renderView2)
# trace defaults for the display properties.
slice1Display_2.Representation = 'Surface'
slice1Display_2.ColorArrayName = [None, '']
slice1Display_2.OSPRayScaleArray = 'U'
slice1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display_2.SelectOrientationVectors = 'None'
slice1Display_2.ScaleFactor = 3.0
slice1Display_2.SelectScaleArray = 'None'
slice1Display_2.GlyphType = 'Arrow'
slice1Display_2.GlyphTableIndexArray = 'None'
slice1Display_2.DataAxesGrid = 'GridAxesRepresentation'
slice1Display_2.PolarAxes = 'PolarAxesRepresentation'
slice1Display_2.SelectInputVectors = ['POINTS', 'U']
slice1Display_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display_2.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView3)

#change interaction mode for render view
renderView3.InteractionMode = '3D'

#change interaction mode for render view
renderView3.InteractionMode = '2D'

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.1, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.1, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# reset view to fit data
renderView3.ResetCamera()

# reset view to fit data
renderView3.ResetCamera()

# reset view to fit data
renderView3.ResetCamera()

# reset view to fit data
renderView3.ResetCamera()

# reset view to fit data
renderView3.ResetCamera()

# reset view to fit data
renderView3.ResetCamera()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0001, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0001, 0.0]

# Properties modified on text1
text1.Text = 'Y=0'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# current camera placement for renderView3
renderView3.InteractionMode = '2D'
renderView3.CameraPosition = [0.4068092415806871, -0.11531022824483632, 64.11140425314966]
renderView3.CameraFocalPoint = [0.4068092415806871, -0.11531022824483632, 4.0]
renderView3.CameraParallelScale = 1.5551787910319006

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [-55.11140425314966, 0.008491841081358465, 0.6219108888530256]
renderView2.CameraFocalPoint = [5.0, 0.008491841081358465, 0.6219108888530256]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 0.9053180407924316

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [5.0, -84.67221808526989, 4.000000238418579]
renderView1.CameraFocalPoint = [5.0, 0.0009999275207519531, 4.000000238418579]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 4.163770581228194

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.05, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.10, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.15, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.20, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.25, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.30, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.35, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.40, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.45, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.50, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.55, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.60, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.65, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.70, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.75, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.85, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.90, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.95, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.00, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.05, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.10, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.15, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.20, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.25, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.30, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.35, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.40, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.45, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.50, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpY30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])




################################$###########################pressure
# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'p'))

# get color transfer function/color map for 'totalp'
totalpLUT = GetColorTransferFunction('totalp')
totalpLUT.LockDataRange = 1
totalpLUT.RGBPoints = [-1500.0, 0.0, 0.0, 1.0, 1500.0, 1.0, 0.0, 0.0]
totalpLUT.ColorSpace = 'HSV'
totalpLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
totalpLUT.NumberOfTableValues = 64
totalpLUT.ScalarRangeInitialized = 1.0

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(totalpLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.LockDataRange = 1
pLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1000.0, 1.0, 0.0, 0.0]
pLUT.ColorSpace = 'HSV'
pLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pLUT.NumberOfTableValues = 64
pLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)
pLUTColorBar.Title = 'Pressure'
pLUTColorBar.ComponentTitle = '[Pa]'
pLUTColorBar.RangeLabelFormat = '%-#6.1f'


# change scalar bar placement
pLUTColorBar.WindowLocation = 'LowerRightCorner'
pLUTColorBar.ScalarBarLength = 0.23

# Properties modified on text1
text1.Text = 'Y=0.1'

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0001, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)


SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.05, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.10, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.15, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.20, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.25, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.30, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.35, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.40, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.45, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.50, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.55, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.60, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.65, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.70, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.75, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.85, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.90, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.95, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.00, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.05, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.10, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.15, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.20, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.25, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.30, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.35, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.40, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.45, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.50, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pY30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

################################$###########################velocity

ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.LockDataRange = 1
uLUT.RGBPoints = [0.0, 0.0, 0.0, 1.0, 70.0, 1.0, 0.0, 0.0]
uLUT.ColorSpace = 'HSV'
uLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
uLUT.NumberOfTableValues = 64

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# Rescale transfer function
uPWF.RescaleTransferFunction(0.0, 70.0)

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'Velocity'
uLUTColorBar.ComponentTitle = 'M/sec'
uLUTColorBar.RangeLabelFormat = '%-#6.1f'

# change scalar bar placement
uLUTColorBar.WindowLocation = 'LowerRightCorner'
uLUTColorBar.ScalarBarLength = 0.23

# Properties modified on text1
text1.Text = 'Y=0.0'

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0001, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)


SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.05, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.10, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.15, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.20, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.25, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.30, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.35, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.40, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.45, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.50, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.55, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.60, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.65, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.70, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.75, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.85, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.90, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.95, 0.0]

# Properties modified on text1
text1.Text = 'Y=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.00, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.05, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.10, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.15, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.20, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.25, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.30, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.35, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.40, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.45, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 1.50, 0.0]

# Properties modified on text1
text1.Text = 'Y=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uY30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView1)


##Closes ParaFoam
import subprocess
subprocess.call("kill $(ps aux|grep -e 'paraview'|grep -v grep|awk {'print $2'})", shell=True)
