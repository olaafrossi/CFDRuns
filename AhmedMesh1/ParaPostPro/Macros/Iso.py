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

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(Input=masterCaseOpenFOAM)

# Properties modified on masterCaseOpenFOAM
masterCaseOpenFOAM.MeshParts = ['internalMesh', 'tireGroup - group', 'wall - group', 'carGroup - group', 'symmetry - group', 'symWall - symmetry', 'outlet - patch', 'upperWall - patch', 'inlet - patch', 'left - patch', 'lowerWall - wall', 'CarBody_wall - wall', 'Splitter_wall - wall', 'Wing_wall - wall', 'Upright_wall - wall', 'RadBody_wall - wall', 'FRTire_wall - wall', 'FRPlinth_wall - wall', 'RRTire_wall - wall', 'RRPlinth_wall - wall']

# Properties modified on extractBlock1
extractBlock1.BlockIndices = [17, 18, 10, 11, 12, 13, 14, 15, 16]

# show data in view
extractBlock1Display = Show(extractBlock1, renderView1)
# trace defaults for the display properties.
extractBlock1Display.Representation = 'Surface'
extractBlock1Display.ColorArrayName = [None, '']
extractBlock1Display.OSPRayScaleArray = 'U'
extractBlock1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractBlock1Display.SelectOrientationVectors = 'None'
extractBlock1Display.ScaleFactor = 0.436339807510376
extractBlock1Display.SelectScaleArray = 'None'
extractBlock1Display.GlyphType = 'Arrow'
extractBlock1Display.GlyphTableIndexArray = 'None'
extractBlock1Display.DataAxesGrid = 'GridAxesRepresentation'
extractBlock1Display.PolarAxes = 'PolarAxesRepresentation'
extractBlock1Display.SelectInputVectors = ['POINTS', 'U']
extractBlock1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractBlock1Display.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(masterCaseOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractBlock1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractBlock1Display.SetScalarBarVisibility(renderView1, True)

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
reflect1Display.ScaleFactor = 0.436339807510376
reflect1Display.SelectScaleArray = 'None'
reflect1Display.GlyphType = 'Arrow'
reflect1Display.GlyphTableIndexArray = 'None'
reflect1Display.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display.PolarAxes = 'PolarAxesRepresentation'
reflect1Display.ScalarOpacityUnitDistance = 0.05310636881446335
reflect1Display.SelectInputVectors = ['POINTS', 'U']
reflect1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
reflect1Display.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractBlock1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(reflect1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'p'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.LockDataRange = 1
pLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1000.0, 1.0, 0.0, 0.0]
pLUT.ColorSpace = 'HSV'
pLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pLUT.NumberOfTableValues = 64

# Properties modified on renderView1
renderView1.Background = [0.0, 0.0, 0.0]

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1042, 1162]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 0
renderView2.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(2, renderView2)

# Properties modified on renderView2
renderView2.Background = [0.0, 0.0, 0.0]

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitVertical(1, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [1043, 565]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.StereoType = 0
renderView3.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(4, renderView3)

# Properties modified on renderView3
renderView3.Background = [0.0, 0.0, 0.0]

# set active view
SetActiveView(renderView2)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [1042, 565]
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.StereoType = 0
renderView4.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(6, renderView4)

# Properties modified on renderView4
renderView4.Background = [0.0, 0.0, 0.0]

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display_1 = Show(reflect1, renderView2)
# trace defaults for the display properties.
reflect1Display_1.Representation = 'Surface'
reflect1Display_1.ColorArrayName = [None, '']
reflect1Display_1.OSPRayScaleArray = 'U'
reflect1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
reflect1Display_1.SelectOrientationVectors = 'None'
reflect1Display_1.ScaleFactor = 0.436339807510376
reflect1Display_1.SelectScaleArray = 'None'
reflect1Display_1.GlyphType = 'Arrow'
reflect1Display_1.GlyphTableIndexArray = 'None'
reflect1Display_1.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display_1.PolarAxes = 'PolarAxesRepresentation'
reflect1Display_1.ScalarOpacityUnitDistance = 0.05310636881446335
reflect1Display_1.SelectInputVectors = ['POINTS', 'U']
reflect1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
reflect1Display_1.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView2.ResetCamera()

# set scalar coloring
ColorBy(reflect1Display_1, ('POINTS', 'p'))

# rescale color and/or opacity maps used to include current data range
reflect1Display_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display_1.SetScalarBarVisibility(renderView2, True)

# set active view
SetActiveView(renderView3)

# show data in view
reflect1Display_2 = Show(reflect1, renderView3)
# trace defaults for the display properties.
reflect1Display_2.Representation = 'Surface'
reflect1Display_2.ColorArrayName = [None, '']
reflect1Display_2.OSPRayScaleArray = 'U'
reflect1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
reflect1Display_2.SelectOrientationVectors = 'None'
reflect1Display_2.ScaleFactor = 0.436339807510376
reflect1Display_2.SelectScaleArray = 'None'
reflect1Display_2.GlyphType = 'Arrow'
reflect1Display_2.GlyphTableIndexArray = 'None'
reflect1Display_2.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display_2.PolarAxes = 'PolarAxesRepresentation'
reflect1Display_2.ScalarOpacityUnitDistance = 0.05310636881446335
reflect1Display_2.SelectInputVectors = ['POINTS', 'U']
reflect1Display_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
reflect1Display_2.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView3.ResetCamera()

# set scalar coloring
ColorBy(reflect1Display_2, ('POINTS', 'p'))

# rescale color and/or opacity maps used to include current data range
reflect1Display_2.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display_2.SetScalarBarVisibility(renderView3, True)

# set active view
SetActiveView(renderView4)

# show data in view
reflect1Display_3 = Show(reflect1, renderView4)
# trace defaults for the display properties.
reflect1Display_3.Representation = 'Surface'
reflect1Display_3.ColorArrayName = [None, '']
reflect1Display_3.OSPRayScaleArray = 'U'
reflect1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
reflect1Display_3.SelectOrientationVectors = 'None'
reflect1Display_3.ScaleFactor = 0.436339807510376
reflect1Display_3.SelectScaleArray = 'None'
reflect1Display_3.GlyphType = 'Arrow'
reflect1Display_3.GlyphTableIndexArray = 'None'
reflect1Display_3.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display_3.PolarAxes = 'PolarAxesRepresentation'
reflect1Display_3.ScalarOpacityUnitDistance = 0.05310636881446335
reflect1Display_3.SelectInputVectors = ['POINTS', 'U']
reflect1Display_3.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
reflect1Display_3.OSPRayScaleFunction.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView4.ResetCamera()

# set scalar coloring
ColorBy(reflect1Display_3, ('POINTS', 'p'))

# rescale color and/or opacity maps used to include current data range
reflect1Display_3.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display_3.SetScalarBarVisibility(renderView4, True)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView3)

# set active view
SetActiveView(renderView4)

#change interaction mode for render view
renderView4.InteractionMode = '2D'

#change interaction mode for render view
renderView4.InteractionMode = '3D'

# set active view
SetActiveView(renderView2)

# set scalar coloring
ColorBy(reflect1Display_1, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
reflect1Display_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display_1.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.LockDataRange = 1
uLUT.RGBPoints = [0.0, 0.0, 0.0, 1.0, 70.0, 1.0, 0.0, 0.0]
uLUT.ColorSpace = 'HSV'
uLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
uLUT.NumberOfTableValues = 64

# change representation type
reflect1Display_1.SetRepresentationType('Surface LIC')

# Properties modified on reflect1Display_1
reflect1Display_1.SelectInputVectors = ['POINTS', 'wallShearStress']

# set active view
SetActiveView(renderView3)

# set scalar coloring
ColorBy(reflect1Display_2, ('POINTS', 'wallShearStress', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView3)

# rescale color and/or opacity maps used to include current data range
reflect1Display_2.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display_2.SetScalarBarVisibility(renderView3, True)

# get color transfer function/color map for 'wallShearStress'
wallShearStressLUT = GetColorTransferFunction('wallShearStress')
wallShearStressLUT.LockDataRange = 1
wallShearStressLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1000.0, 1.0, 0.0, 0.0]
wallShearStressLUT.ColorSpace = 'HSV'
wallShearStressLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
wallShearStressLUT.NumberOfTableValues = 64

# Rescale transfer function
wallShearStressLUT.RescaleTransferFunction(-2.0, 15.0)

# get opacity transfer function/opacity map for 'wallShearStress'
wallShearStressPWF = GetOpacityTransferFunction('wallShearStress')
wallShearStressPWF.Points = [-2000.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]
wallShearStressPWF.ScalarRangeInitialized = 1

# Rescale transfer function
wallShearStressPWF.RescaleTransferFunction(-2.0, 15.0)

# set active view
SetActiveView(renderView4)

# change representation type
reflect1Display_3.SetRepresentationType('Surface With Edges')

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView4)

# current camera placement for renderView2
renderView2.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView2.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView2.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView2.CameraParallelScale = 2.54276280729466

# current camera placement for renderView4
renderView4.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView4.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView4.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView4.CameraParallelScale = 2.54276280729466

# current camera placement for renderView3
renderView3.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView3.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView3.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView3.CameraParallelScale = 2.54276280729466

# current camera placement for renderView1
renderView1.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView1.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView1.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView1.CameraParallelScale = 2.54276280729466

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/ISO/Iso1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160])

#### saving camera placements for all active views

# current camera placement for renderView2
renderView2.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView2.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView2.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView2.CameraParallelScale = 2.54276280729466

# current camera placement for renderView4
renderView4.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView4.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView4.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView4.CameraParallelScale = 2.54276280729466

# current camera placement for renderView3
renderView3.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView3.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView3.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView3.CameraParallelScale = 2.54276280729466

# current camera placement for renderView1
renderView1.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView1.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView1.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView1.CameraParallelScale = 2.54276280729466

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

##Closes ParaFoam
import subprocess
subprocess.call("kill $(ps aux|grep -e 'paraview'|grep -v grep|awk {'print $2'})", shell=True)
