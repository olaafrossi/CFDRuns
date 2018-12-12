#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
currentOpenFOAM = GetActiveSource()

# set active source
SetActiveSource(currentOpenFOAM)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [1152, 674]

# show data in view
currentOpenFOAMDisplay = Show(currentOpenFOAM, renderView1)
# trace defaults for the display properties.
currentOpenFOAMDisplay.Representation = 'Surface'
currentOpenFOAMDisplay.ColorArrayName = [None, '']
currentOpenFOAMDisplay.OSPRayScaleArray = 'U'
currentOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
currentOpenFOAMDisplay.SelectOrientationVectors = 'None'
currentOpenFOAMDisplay.ScaleFactor = 3.0
currentOpenFOAMDisplay.SelectScaleArray = 'None'
currentOpenFOAMDisplay.GlyphType = 'Arrow'
currentOpenFOAMDisplay.GlyphTableIndexArray = 'None'
currentOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
currentOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# Properties modified on currentOpenFOAM
currentOpenFOAM.MeshParts = ['internalMesh']
currentOpenFOAM.VolumeFields = ['p', 'total(p)', 'U']

# show data in view
currentOpenFOAMDisplay = Show(currentOpenFOAM, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Slice'
slice1 = Slice(Input=currentOpenFOAM)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [5.0, 0.0, 0.0]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

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

# hide data in view
Hide(currentOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# change render mode to 2d and setup background color ////////////////////////////////////////////

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# Properties modified on renderView1
renderView1.Background = [0.10196078431372549, 0.10980392156862745, 0.1411764705882353]

# end change render mode to 2d and setup background color ////////////////////////////////////////////

# Setup U Render View ////////////////////////////////////////////////////////

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 32.16386077987473, 0.865003, 0.865003, 0.865003, 64.32772155974946, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
uLUT.ApplyPreset('Blue to Red Rainbow', True)

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'

# reset view to fit data
renderView1.ResetCamera()

# change scalar bar placement
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.15885416666666663, 0.11572700296735908]
uLUTColorBar.ScalarBarLength = 0.15999999999999978

# Rescale transfer function
uLUT.RescaleTransferFunction(20.0, 70.0)

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [0.0, 0.0, 0.5, 0.0, 64.32772155974946, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# Rescale transfer function
uPWF.RescaleTransferFunction(20.0, 70.0)

# End U Render View ////////////////////////////////////////////////////////

# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-3.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_A_-300.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_B_-275.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_C_-250.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_D_-225.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_E_-200.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_F_-175.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_G_-150.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_H_-125.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_I_-100.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_J_-075.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_K_-050.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_L_-025.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_M_000.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_N_025.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_O_050.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_P_075.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_Q_100.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_R_125.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_X_150.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_Y_175.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_Z_200.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZA_225.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZB_250.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZC_275.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZD_300.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZE_325.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZF_350.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZG_375.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [4.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/U_ZH_400.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop

# Setup P Render View ////////////////////////////////////////////////////////

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'p'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.RGBPoints = [-1578.7750244140625, 0.231373, 0.298039, 0.752941, -527.2277526855469, 0.865003, 0.865003, 0.865003, 524.3195190429688, 0.705882, 0.0156863, 0.14902]
pLUT.ScalarRangeInitialized = 1.0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pLUT.ApplyPreset('Blue to Red Rainbow', True)

# Rescale transfer function
pLUT.RescaleTransferFunction(-2000.0, 1000.0)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [-1578.7750244140625, 0.0, 0.5, 0.0, 524.3195190429688, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# Rescale transfer function
pPWF.RescaleTransferFunction(-2000.0, 1000.0)

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)
pLUTColorBar.Title = 'p'
pLUTColorBar.ComponentTitle = 'Pressure'

# change scalar bar placement
pLUTColorBar.WindowLocation = 'AnyLocation'
pLUTColorBar.Position = [0.15885416666666663, 0.11572700296735908]
pLUTColorBar.ScalarBarLength = 0.15999999999999978

# End P Render View ////////////////////////////////////////////////////////

# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-3.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_A_-300.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_B_-275.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_C_-250.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_D_-225.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_E_-200.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_F_-175.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_G_-150.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_H_-125.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_I_-100.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_J_-075.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_K_-050.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_L_-025.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_M_000.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_N_025.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_O_050.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_P_075.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_Q_100.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_R_125.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_X_150.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_Y_175.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_Z_200.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZA_225.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZB_250.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZC_275.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZD_300.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZE_325.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZF_350.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZG_375.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [4.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/P_ZH_400.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop





# Setup totalP Render View ////////////////////////////////////////////////////////

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'total(p)'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'totalP'
totalpLUT = GetColorTransferFunction('totalp')
totalpLUT.RGBPoints = [121.2272720336914, 0.231373, 0.298039, 0.752941, 839.1496467590332, 0.865003, 0.865003, 0.865003, 1557.072021484375, 0.705882, 0.0156863, 0.14902]
totalpLUT.ScalarRangeInitialized = 1.0

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'total(p)'))

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
totalpLUT.ApplyPreset('rainbow', True)

# get color legend/bar for uLUT in view renderView1
totalpLUTColorBar = GetScalarBar(totalpLUT, renderView1)
totalpLUTColorBar.Title = 'p'
totalpLUTColorBar.ComponentTitle = 'Total'

# reset view to fit data
renderView1.ResetCamera()

# change scalar bar placement
totalpLUTColorBar.WindowLocation = 'AnyLocation'
totalpLUTColorBar.Position = [0.15885416666666663, 0.11572700296735908]
totalpLUTColorBar.ScalarBarLength = 0.15999999999999978

# Rescale transfer function
totalpLUT.RescaleTransferFunction(-750.0, 1000.0)

# get opacity transfer function/opacity map for 'totalP'
totalpPWF = GetOpacityTransferFunction('totalp')
totalpPWF.Points = [121.2272720336914, 0.0, 0.5, 0.0, 1557.072021484375, 1.0, 0.5, 0.0]
totalpPWF.ScalarRangeInitialized = 1

# Rescale transfer function
totalpPWF.RescaleTransferFunction(-750.0, 1000.0)

# End totalP Render View ////////////////////////////////////////////////////////


# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-3.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_A_-300.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_B_-275.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_C_-250.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_D_-225.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-2.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_E_-200.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_F_-175.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_G_-150.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_H_-125.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_I_-100.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_J_-075.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_K_-050.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_L_-025.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_M_000.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_N_025.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_O_050.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_P_075.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_Q_100.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_R_125.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_X_150.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_Y_175.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_Z_200.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZA_225.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZB_250.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [2.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZC_275.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZD_300.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.25, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZE_325.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.5, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZF_350.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [3.75, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZG_375.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop
# Start ScreenShot Loop ////////////////////////////////////////////////////////

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [4.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/RUNS/Current/ParaPostPro/Images/TP_ZH_400.png', renderView1, ImageResolution=[4608, 2696])

# End Sceenshot Loop





#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-19.0, -3.0, 4.0]
renderView1.CameraFocalPoint = [1.73472347597681e-18, -3.0, 4.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 5.0

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

##Closes ParaFoam
import subprocess
subprocess.call("kill $(ps aux|grep -e 'paraview'|grep -v grep|awk {'print $2'})", shell=True)