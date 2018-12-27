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

# Properties modified on renderView1
renderView1.Background = [0.0, 0.0, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# create a new 'Slice'
slice1 = Slice(Input=masterCaseOpenFOAM)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [5.0, 4.0, 4.0]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on masterCaseOpenFOAM
masterCaseOpenFOAM.MeshParts = ['internalMesh', 'tireGroup - group', 'wall - group', 'carGroup - group', 'symmetry - group', 'symWall - symmetry', 'outlet - patch', 'upperWall - patch', 'inlet - patch', 'left - patch', 'lowerWall - wall', 'CarBody_wall - wall', 'Splitter_wall - wall', 'Wing_wall - wall', 'Upright_wall - wall', 'RadBody_wall - wall', 'FRTire_wall - wall', 'FRPlinth_wall - wall', 'RRTire_wall - wall', 'RRPlinth_wall - wall']

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
slice1Display.ScaleFactor = 0.8
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

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# change representation type
slice1Display.SetRepresentationType('Surface With Edges')

# hide color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, False)

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# current camera placement for renderView1
renderView1.CameraPosition = [-1.6947471998049308, 1.6933613737623023, 1.5112611008354886]
renderView1.CameraFocalPoint = [16.334612919711844, -6.838532355532668, -7.424703673133138]
renderView1.CameraViewUp = [0.4061652531603055, -0.0937319492496543, 0.9089797075925762]
renderView1.CameraParallelScale = 0.9954386319424243

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/mesh/Mesh1.png', renderView1, ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1
slice1.Crinkleslice = 1

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.CameraPosition = [-14.774335127347182, 7.010177789308881, 7.669375743529799]
renderView1.CameraFocalPoint = [3.2550249921695533, -1.5217159399860836, -1.2665890304388114]
renderView1.CameraViewUp = [0.4061652531603055, -0.0937319492496543, 0.9089797075925762]
renderView1.CameraParallelScale = 0.9954386319424243

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/mesh/Mesh2.png', renderView1, ImageResolution=[3840, 2160])

# current camera placement for renderView1
renderView1.CameraPosition = [-2.7001172676889453, 0.5402236290689648, 0.544776445200009]
renderView1.CameraFocalPoint = [15.32924285182777, -7.991670100225991, -8.391188328768601]
renderView1.CameraViewUp = [0.4061652531603055, -0.0937319492496543, 0.9089797075925762]
renderView1.CameraParallelScale = 0.9954386319424243

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/mesh/Mesh3.png', renderView1, ImageResolution=[3840, 2160])

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.5]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.5]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.CameraPosition = [-9.989103344187834, 3.989533764689353, 4.1574461342942035]
renderView1.CameraFocalPoint = [8.040256775328894, -4.5423599646055886, -4.7785186396744015]
renderView1.CameraViewUp = [0.4061652531603055, -0.0937319492496543, 0.9089797075925762]
renderView1.CameraParallelScale = 0.9954386319424243

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/mesh/Mesh4.png', renderView1, ImageResolution=[3840, 2160])

# current camera placement for renderView1
renderView1.CameraPosition = [-3.6655143471998333, 1.7207514916383146, 1.5134144976508102]
renderView1.CameraFocalPoint = [14.363845772316905, -6.81114223765664, -7.422550276317808]
renderView1.CameraViewUp = [0.4061652531603055, -0.0937319492496543, 0.9089797075925762]
renderView1.CameraParallelScale = 0.9954386319424243

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/mesh/Mesh5.png', renderView1, ImageResolution=[3840, 2160])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-3.6655143471998333, 1.7207514916383146, 1.5134144976508102]
renderView1.CameraFocalPoint = [14.363845772316905, -6.81114223765664, -7.422550276317808]
renderView1.CameraViewUp = [0.4061652531603055, -0.0937319492496543, 0.9089797075925762]
renderView1.CameraParallelScale = 0.9954386319424243

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

##Closes ParaFoam
import subprocess
subprocess.call("kill $(ps aux|grep -e 'paraview'|grep -v grep|awk {'print $2'})", shell=True)
