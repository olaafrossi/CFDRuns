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

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

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

# create a new 'STL Reader'
fullCarstl = STLReader(FileNames=['/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/FullCar.stl'])

# Properties modified on masterCaseOpenFOAM
masterCaseOpenFOAM.MeshParts = ['internalMesh', 'tireGroup - group', 'wall - group', 'carGroup - group', 'symmetry - group', 'symWall - symmetry', 'outlet - patch', 'upperWall - patch', 'inlet - patch', 'left - patch', 'lowerWall - wall', 'CarBody_wall - wall', 'Splitter_wall - wall', 'Wing_wall - wall', 'Upright_wall - wall', 'RadBody_wall - wall', 'FRTire_wall - wall', 'FRPlinth_wall - wall', 'RRTire_wall - wall', 'RRPlinth_wall - wall']

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

# reset view to fit data
renderView2.ResetCamera()

# show color bar/color legend
fullCarstlDisplay.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# hide color bar/color legend
fullCarstlDisplay.SetScalarBarVisibility(renderView2, False)

# reset view to fit data
renderView2.ResetCamera()

#change interaction mode for render view
renderView2.InteractionMode = '2D'

# Properties modified on renderView2.AxesGrid
renderView2.AxesGrid.Visibility = 1

# set active source
SetActiveSource(masterCaseOpenFOAM)

# set active view
SetActiveView(renderView1)

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

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# create a new 'Slice'
slice1 = Slice(Input=reflect1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [5.0, 0.0, 4.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

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
Hide(reflect1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

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

# Rescale transfer function
totalpLUT.RescaleTransferFunction(-1500.0, 1500.0)

# get opacity transfer function/opacity map for 'totalp'
totalpPWF = GetOpacityTransferFunction('totalp')
totalpPWF.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]
totalpPWF.ScalarRangeInitialized = 1

# Rescale transfer function
totalpPWF.RescaleTransferFunction(-1500.0, 1500.0)

# get color legend/bar for totalpLUT in view renderView1
totalpLUTColorBar = GetScalarBar(totalpLUT, renderView1)
totalpLUTColorBar.Title = 'total(p)'
totalpLUTColorBar.ComponentTitle = ''
totalpLUTColorBar.RangeLabelFormat = '%-#6.1f'

# change scalar bar placement
totalpLUTColorBar.WindowLocation = 'AnyLocation'
totalpLUTColorBar.Position = [0.9293218720152817, 0.0565371024734983]
totalpLUTColorBar.ScalarBarLength = 0.32999999999999896

# change scalar bar placement
totalpLUTColorBar.ScalarBarLength = 0.3582685512367481

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

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

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# set active view
SetActiveView(renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.001]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.001]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# create a new 'Text'
text1 = Text()

# Properties modified on text1
text1.Text = 'Z=0.0'

# show data in view
text1Display = Show(text1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on text1Display
text1Display.WindowLocation = 'LowerLeftCorner'

# Properties modified on text1Display
text1Display.WindowLocation = 'UpperLeftCorner'

# Properties modified on text1Display
text1Display.Interactivity = 0

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.05088420732665447, -4.08046096594518, 0.7469422765190563]
renderView2.CameraFocalPoint = [0.05088420732665447, 5.234486803129569, 0.7469422765190563]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 0.9159479862732752

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [5.832972651644024, 0.0029953806643630097, 65.939875929653]
renderView1.CameraFocalPoint = [5.832972651644024, 0.0029953806643630097, 4.0]
renderView1.CameraParallelScale = 3.8222296520738333

# save screenshot
#SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ1.png', layout1, SaveAllViews=1,
#    ImageResolution=[3840, 2160])

# set active source
SetActiveSource(slice1)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView2)

# hide data in view
Hide(slice1, renderView2)

# set active view
SetActiveView(renderView1)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.001]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.05088420732665447, -4.08046096594518, 0.7469422765190563]
renderView2.CameraFocalPoint = [0.05088420732665447, 5.234486803129569, 0.7469422765190563]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 0.9159479862732752

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [5.832972651644024, 0.0029953806643630097, 65.939875929653]
renderView1.CameraFocalPoint = [5.832972651644024, 0.0029953806643630097, 4.0]
renderView1.CameraParallelScale = 3.8222296520738333

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.05]

# Properties modified on text1
text1.Text = 'Z=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.10]

# Properties modified on text1
text1.Text = 'Z=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.15]

# Properties modified on text1
text1.Text = 'Z=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.20]

# Properties modified on text1
text1.Text = 'Z=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.25]

# Properties modified on text1
text1.Text = 'Z=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.30]

# Properties modified on text1
text1.Text = 'Z=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.35]

# Properties modified on text1
text1.Text = 'Z=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.40]

# Properties modified on text1
text1.Text = 'Z=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.45]

# Properties modified on text1
text1.Text = 'Z=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.50]

# Properties modified on text1
text1.Text = 'Z=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.55]

# Properties modified on text1
text1.Text = 'Z=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.60]

# Properties modified on text1
text1.Text = 'Z=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.65]

# Properties modified on text1
text1.Text = 'Z=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.70]

# Properties modified on text1
text1.Text = 'Z=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.75]

# Properties modified on text1
text1.Text = 'Z=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.80]

# Properties modified on text1
text1.Text = 'Z=0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.85]

# Properties modified on text1
text1.Text = 'Z=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.90]

# Properties modified on text1
text1.Text = 'Z=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.95]

# Properties modified on text1
text1.Text = 'Z=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.00]

# Properties modified on text1
text1.Text = 'Z=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.05]

# Properties modified on text1
text1.Text = 'Z=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.10]

# Properties modified on text1
text1.Text = 'Z=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.15]

# Properties modified on text1
text1.Text = 'Z=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.20]

# Properties modified on text1
text1.Text = 'Z=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.25]

# Properties modified on text1
text1.Text = 'Z=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.30]

# Properties modified on text1
text1.Text = 'Z=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.35]

# Properties modified on text1
text1.Text = 'Z=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.40]

# Properties modified on text1
text1.Text = 'Z=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.45]

# Properties modified on text1
text1.Text = 'Z=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.50]

# Properties modified on text1
text1.Text = 'Z=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ31.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.55]

# Properties modified on text1
text1.Text = 'Z=1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ32.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.60]

# Properties modified on text1
text1.Text = 'Z=1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ33.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.65]

# Properties modified on text1
text1.Text = 'Z=1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ34.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.70]

# Properties modified on text1
text1.Text = 'Z=1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ35.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.75]

# Properties modified on text1
text1.Text = 'Z=1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ36.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.80]

# Properties modified on text1
text1.Text = 'Z=1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ37.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.85]

# Properties modified on text1
text1.Text = 'Z=1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ38.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.90]

# Properties modified on text1
text1.Text = 'Z=1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ39.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.95]

# Properties modified on text1
text1.Text = 'Z=1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/tp/tpZ40.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 2.00]

# Properties modified on text1
text1.Text = 'Z=2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)


#####################################################################

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

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.001]

# Properties modified on text1
text1.Text = 'Z=0.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.05]

# Properties modified on text1
text1.Text = 'Z=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.10]

# Properties modified on text1
text1.Text = 'Z=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.15]

# Properties modified on text1
text1.Text = 'Z=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.20]

# Properties modified on text1
text1.Text = 'Z=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.25]

# Properties modified on text1
text1.Text = 'Z=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.30]

# Properties modified on text1
text1.Text = 'Z=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.35]

# Properties modified on text1
text1.Text = 'Z=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.40]

# Properties modified on text1
text1.Text = 'Z=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.45]

# Properties modified on text1
text1.Text = 'Z=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.50]

# Properties modified on text1
text1.Text = 'Z=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.55]

# Properties modified on text1
text1.Text = 'Z=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.60]

# Properties modified on text1
text1.Text = 'Z=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.65]

# Properties modified on text1
text1.Text = 'Z=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.70]

# Properties modified on text1
text1.Text = 'Z=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.75]

# Properties modified on text1
text1.Text = 'Z=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.80]

# Properties modified on text1
text1.Text = 'Z=0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.85]

# Properties modified on text1
text1.Text = 'Z=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.90]

# Properties modified on text1
text1.Text = 'Z=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.95]

# Properties modified on text1
text1.Text = 'Z=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.00]

# Properties modified on text1
text1.Text = 'Z=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.05]

# Properties modified on text1
text1.Text = 'Z=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.10]

# Properties modified on text1
text1.Text = 'Z=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.15]

# Properties modified on text1
text1.Text = 'Z=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.20]

# Properties modified on text1
text1.Text = 'Z=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.25]

# Properties modified on text1
text1.Text = 'Z=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.30]

# Properties modified on text1
text1.Text = 'Z=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.35]

# Properties modified on text1
text1.Text = 'Z=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.40]

# Properties modified on text1
text1.Text = 'Z=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.45]

# Properties modified on text1
text1.Text = 'Z=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.50]

# Properties modified on text1
text1.Text = 'Z=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ31.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.55]

# Properties modified on text1
text1.Text = 'Z=1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ32.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.60]

# Properties modified on text1
text1.Text = 'Z=1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ33.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.65]

# Properties modified on text1
text1.Text = 'Z=1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ34.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.70]

# Properties modified on text1
text1.Text = 'Z=1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ35.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.75]

# Properties modified on text1
text1.Text = 'Z=1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ36.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.80]

# Properties modified on text1
text1.Text = 'Z=1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ37.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.85]

# Properties modified on text1
text1.Text = 'Z=1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ38.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.90]

# Properties modified on text1
text1.Text = 'Z=1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ39.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.95]

# Properties modified on text1
text1.Text = 'Z=1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/p/pZ40.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 2.00]

# Properties modified on text1
text1.Text = 'Z=2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)


##################################

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

#############################

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.001]

# Properties modified on text1
text1.Text = 'Z=0.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.05]

# Properties modified on text1
text1.Text = 'Z=0.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ2.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.10]

# Properties modified on text1
text1.Text = 'Z=0.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ3.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.15]

# Properties modified on text1
text1.Text = 'Z=0.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ4.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.20]

# Properties modified on text1
text1.Text = 'Z=0.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ5.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.25]

# Properties modified on text1
text1.Text = 'Z=0.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ6.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.30]

# Properties modified on text1
text1.Text = 'Z=0.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ7.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.35]

# Properties modified on text1
text1.Text = 'Z=0.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ8.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.40]

# Properties modified on text1
text1.Text = 'Z=0.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ9.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.45]

# Properties modified on text1
text1.Text = 'Z=0.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ10.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.50]

# Properties modified on text1
text1.Text = 'Z=0.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ11.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.55]

# Properties modified on text1
text1.Text = 'Z=0.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ12.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.60]

# Properties modified on text1
text1.Text = 'Z=0.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ13.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.65]

# Properties modified on text1
text1.Text = 'Z=0.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ14.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.70]

# Properties modified on text1
text1.Text = 'Z=0.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ15.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.75]

# Properties modified on text1
text1.Text = 'Z=0.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ16.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.80]

# Properties modified on text1
text1.Text = 'Z=0.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ17.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.85]

# Properties modified on text1
text1.Text = 'Z=0.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ18.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.90]

# Properties modified on text1
text1.Text = 'Z=0.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ19.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.95]

# Properties modified on text1
text1.Text = 'Z=0.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ20.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.00]

# Properties modified on text1
text1.Text = 'Z=1.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ21.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.05]

# Properties modified on text1
text1.Text = 'Z=1.05'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ22.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.10]

# Properties modified on text1
text1.Text = 'Z=1.10'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ23.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.15]

# Properties modified on text1
text1.Text = 'Z=1.15'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ24.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.20]

# Properties modified on text1
text1.Text = 'Z=1.20'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ25.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.25]

# Properties modified on text1
text1.Text = 'Z=1.25'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ26.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.30]

# Properties modified on text1
text1.Text = 'Z=1.30'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ27.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.35]

# Properties modified on text1
text1.Text = 'Z=1.35'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ28.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.40]

# Properties modified on text1
text1.Text = 'Z=1.40'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ29.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.45]

# Properties modified on text1
text1.Text = 'Z=1.45'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ30.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.50]

# Properties modified on text1
text1.Text = 'Z=1.50'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ31.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.55]

# Properties modified on text1
text1.Text = 'Z=1.55'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ32.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.60]

# Properties modified on text1
text1.Text = 'Z=1.60'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ33.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.65]

# Properties modified on text1
text1.Text = 'Z=1.65'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ34.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.70]

# Properties modified on text1
text1.Text = 'Z=1.70'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ35.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.75]

# Properties modified on text1
text1.Text = 'Z=1.75'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ36.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.80]

# Properties modified on text1
text1.Text = 'Z=1.80'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ37.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.85]

# Properties modified on text1
text1.Text = 'Z=1.85'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ38.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.90]

# Properties modified on text1
text1.Text = 'Z=1.90'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ39.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1.95]

# Properties modified on text1
text1.Text = 'Z=1.95'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/u/uZ40.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 2.00]

# Properties modified on text1
text1.Text = 'Z=2.00'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

##Closes ParaFoam
import subprocess
subprocess.call("kill $(ps aux|grep -e 'paraview'|grep -v grep|awk {'print $2'})", shell=True)