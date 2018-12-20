#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
masterCaseOpenFOAM = GetActiveSource()

# Properties modified on masterCaseOpenFOAM
masterCaseOpenFOAM.MeshParts = ['internalMesh', 'tireGroup - group', 'wall - group', 'carGroup - group', 'symmetry - group', 'symWall - symmetry', 'outlet - patch', 'upperWall - patch', 'inlet - patch', 'left - patch', 'lowerWall - wall', 'CarBody_wall - wall', 'Splitter_wall - wall', 'Wing_wall - wall', 'Upright_wall - wall', 'RadBody_wall - wall', 'FRTire_wall - wall', 'FRPlinth_wall - wall', 'RRTire_wall - wall', 'RRPlinth_wall - wall']
masterCaseOpenFOAM.VolumeFields = ['k', 'nut', 'omega', 'p', 'total(p)', 'U', 'yPlus', 'wallShearStress']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2094, 1162]

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
renderView2.ViewSize = [2094, 565]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 0
renderView2.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(2, renderView2)

# Properties modified on renderView2
renderView2.Background = [0.0, 0.0, 0.0]

# set active view
SetActiveView(renderView1)

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(Input=masterCaseOpenFOAM)

# Properties modified on extractBlock1
extractBlock1.BlockIndices = [1]

# show data in view
extractBlock1Display = Show(extractBlock1, renderView1)
# trace defaults for the display properties.
extractBlock1Display.Representation = 'Surface'
extractBlock1Display.ColorArrayName = [None, '']
extractBlock1Display.OSPRayScaleArray = 'U'
extractBlock1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractBlock1Display.SelectOrientationVectors = 'None'
extractBlock1Display.ScaleFactor = 3.0
extractBlock1Display.SelectScaleArray = 'None'
extractBlock1Display.GlyphType = 'Arrow'
extractBlock1Display.GlyphTableIndexArray = 'None'
extractBlock1Display.DataAxesGrid = 'GridAxesRepresentation'
extractBlock1Display.PolarAxes = 'PolarAxesRepresentation'
extractBlock1Display.ScalarOpacityUnitDistance = 0.18556617709162576
extractBlock1Display.SelectInputVectors = ['POINTS', 'U']
extractBlock1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractBlock1Display.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(masterCaseOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Reflect'
reflect1 = Reflect(Input=extractBlock1)

# Properties modified on reflect1
reflect1.Plane = 'Y Min'

# show data in view
reflect1Display = Show(reflect1, renderView1)
# trace defaults for the display properties.
reflect1Display.Representation = 'Surface'
reflect1Display.ColorArrayName = [None, '']
reflect1Display.OSPRayScaleArray = 'U'
reflect1Display.OSPRayScaleFunction = 'PiecewiseFunction'
reflect1Display.SelectOrientationVectors = 'None'
reflect1Display.ScaleFactor = 3.0
reflect1Display.SelectScaleArray = 'None'
reflect1Display.GlyphType = 'Arrow'
reflect1Display.GlyphTableIndexArray = 'None'
reflect1Display.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display.PolarAxes = 'PolarAxesRepresentation'
reflect1Display.ScalarOpacityUnitDistance = 0.1604496769119589
reflect1Display.SelectInputVectors = ['POINTS', 'U']
reflect1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
reflect1Display.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractBlock1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# set active view
SetActiveView(renderView2)

#change interaction mode for render view
renderView2.InteractionMode = '2D'

# create a new 'STL Reader'
fullCarstl = STLReader(FileNames=['/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/FullCar.stl'])

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
fullCarstlDisplay = Show(fullCarstl, renderView2)
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
fullCarstlDisplay.SetScalarBarVisibility(renderView2, True)

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# Properties modified on renderView2.AxesGrid
renderView2.AxesGrid.Visibility = 1

# hide color bar/color legend
fullCarstlDisplay.SetScalarBarVisibility(renderView2, False)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(reflect1)

# create a new 'Slice'
slice1 = Slice(Input=reflect1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [5.0, 0.0, 4.0]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.OSPRayScaleArray = 'U'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 1.6
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
Hide(reflect1, renderView1)

# show data in view
fullCarstlDisplay_1 = Show(fullCarstl, renderView1)
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
fullCarstlDisplay_1.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display_1 = Show(slice1, renderView2)
# trace defaults for the display properties.
slice1Display_1.Representation = 'Surface'
slice1Display_1.ColorArrayName = [None, '']
slice1Display_1.OSPRayScaleArray = 'U'
slice1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display_1.SelectOrientationVectors = 'None'
slice1Display_1.ScaleFactor = 1.6
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
SetActiveView(renderView1)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'total(p)'))

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

# hide data in view
Hide(fullCarstl, renderView1)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView1)

# get color legend/bar for totalpLUT in view renderView1
totalpLUTColorBar = GetScalarBar(totalpLUT, renderView1)
totalpLUTColorBar.WindowLocation = 'UpperRightCorner'
totalpLUTColorBar.Title = 'total(p)'
totalpLUTColorBar.ComponentTitle = ''
totalpLUTColorBar.RangeLabelFormat = '%-#6.1f'

# change scalar bar placement
totalpLUTColorBar.WindowLocation = 'AnyLocation'
totalpLUTColorBar.Position = [0.9293218720152817, 0.0565371024734983]
totalpLUTColorBar.ScalarBarLength = 0.32999999999999896

# change scalar bar placement
totalpLUTColorBar.ScalarBarLength = 0.3582685512367481

# Rescale transfer function
totalpLUT.RescaleTransferFunction(-1500.0, 1500.0)

# get opacity transfer function/opacity map for 'totalp'
totalpPWF = GetOpacityTransferFunction('totalp')
totalpPWF.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]
totalpPWF.ScalarRangeInitialized = 1

# Rescale transfer function
totalpPWF.RescaleTransferFunction(-1500.0, 1500.0)

# create a new 'Text'
text1 = Text()

# Properties modified on text1
text1.Text = 'X=-3.00'

# show data in view
text1Display = Show(text1, renderView1)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-3.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on text1Display
text1Display.WindowLocation = 'LowerLeftCorner'

# Properties modified on text1Display
text1Display.WindowLocation = 'UpperLeftCorner'

# Properties modified on text1Display
text1Display.Interactivity = 0

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(slice1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# set active source
SetActiveSource(fullCarstl)

# Properties modified on fullCarstlDisplay.DataAxesGrid
fullCarstlDisplay.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on fullCarstlDisplay.DataAxesGrid
fullCarstlDisplay.DataAxesGrid.GridAxesVisibility = 0

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(fullCarstl)

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.05412650108337402, -9.314947769074745, 0.7436999827623367]
renderView2.CameraFocalPoint = [0.05412650108337402, 0.0, 0.7436999827623367]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 0.931153548689343

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-62.47667734287181, -0.05567986253685033, 1.1268883793815065]
renderView1.CameraFocalPoint = [5.0, -0.05567986253685033, 1.1268883793815065]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1.168211283570875

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.9, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX31.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX32.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX33.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX34.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX35.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX36.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX37.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX38.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX39.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX40.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX41.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX42.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX43.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX44.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX45.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX46.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX47.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX48.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX49.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX50.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX51.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX52.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX53.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX54.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX55.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX56.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX57.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX58.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX59.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX60.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX61.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX62.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX63.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX64.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX65.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX66.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX67.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX68.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX69.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX70.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX71.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX72.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX73.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX74.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX75.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX76.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX77.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX78.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX79.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX80.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX81.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX82.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX83.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX84.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX85.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX86.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX87.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX88.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX89.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX90.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX91.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX92.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX93.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX94.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX95.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX96.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX97.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX98.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX99.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX100.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX101.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX102.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX103.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX104.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX105.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX106.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX107.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX108.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX109.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX110.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX111.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX112.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX113.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX114.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX115.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX116.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX117.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX118.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX119.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX120.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX121.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX122.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX123.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX124.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX125.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX126.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX127.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX128.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX129.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX130.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX131.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX132.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX133.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX134.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX135.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX136.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX137.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX138.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [4.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=4.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpX139.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)


######################################################################################
# set active view
SetActiveView(renderView1)

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
pLUTColorBar.WindowLocation = 'AnyLocation'
pLUTColorBar.Position = [0.9293218720152817, 0.0565371024734983]
pLUTColorBar.ScalarBarLength = 0.3582685512367481

# Properties modified on text1
text1.Text = 'X=-3.00'

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-3.00, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.9, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX31.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX32.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX33.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX34.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX35.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX36.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX37.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX38.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX39.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX40.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX41.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX42.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX43.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX44.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX45.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX46.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX47.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX48.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX49.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX50.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX51.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX52.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX53.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX54.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX55.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX56.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX57.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX58.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX59.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX60.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX61.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX62.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX63.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX64.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX65.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX66.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX67.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX68.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX69.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX70.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX71.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX72.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX73.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX74.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX75.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX76.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX77.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX78.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX79.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX80.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX81.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX82.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX83.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX84.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX85.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX86.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX87.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX88.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX89.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX90.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX91.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX92.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX93.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX94.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX95.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX96.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX97.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX98.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX99.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX100.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX101.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX102.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX103.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX104.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX105.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX106.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX107.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX108.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX109.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX110.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX111.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX112.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX113.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX114.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX115.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX116.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX117.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX118.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX119.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX120.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX121.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX122.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX123.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX124.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX125.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX126.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX127.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX128.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX129.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX130.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX131.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX132.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX133.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX134.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX135.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX136.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX137.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX138.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [4.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=4.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pX139.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)


################################################################################################




################################$###########################velocity
SetActiveView(renderView1)

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
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.9293218720152817, 0.0565371024734983]
uLUTColorBar.ScalarBarLength = 0.3582685512367481

################

# Properties modified on text1
text1.Text = 'X=-3.00'

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-3.00, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])



# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.9, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux31.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux32.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux33.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux34.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux35.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux36.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux37.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux38.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux39.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux40.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux41.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux42.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux43.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux44.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux45.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux46.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux47.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux48.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux49.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux50.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux51.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux52.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux53.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux54.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux55.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux56.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux57.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=-0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux58.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux59.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux60.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux61.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux62.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux63.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux64.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux65.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux66.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux67.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux68.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux69.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux70.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux71.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux72.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux73.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux74.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux75.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux76.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux77.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux78.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux79.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux80.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux81.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux82.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux83.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux84.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux85.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux86.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux87.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux88.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux89.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux90.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux91.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux92.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux93.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux94.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux95.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux96.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux97.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux98.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux99.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux100.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux101.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux102.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux103.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux104.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux105.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux106.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux107.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux108.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux109.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux110.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux111.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux112.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux113.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux114.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux115.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux116.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux117.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=2.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux118.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux119.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.05, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux120.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.10, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux121.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.15, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux122.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.20, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux123.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.25, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux124.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.30, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux125.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.35, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux126.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.40, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux127.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.45, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux128.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.50, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux129.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.55, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux130.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.60, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux131.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.65, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux132.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.70, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux133.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.75, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux134.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.80, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux135.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.85, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux136.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.90, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux137.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.95, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=3.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux138.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [4.00, 0.0, 0.0]

# Properties modified on text1
text1.Text = 'X=4.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/Ux139.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

##Closes ParaFoam
import subprocess
subprocess.call("kill $(ps aux|grep -e 'paraview'|grep -v grep|awk {'print $2'})", shell=True)