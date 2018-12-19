#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1470, 557]

# destroy renderView1
Delete(renderView1)
del renderView1

# load state
LoadState('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/Macros/ParaFoamState.pvsm', LoadStateDataFileOptions='Use File Names From State',
    DataDirectory='/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/Macros',
    OnlyUseFilesInDataDirectory=0,
    MasterCaseOpenFOAMFileName='/home/olaaf/FOAM/AB/A/MasterCase/MasterCase.OpenFOAM',
    #MasterCaseOpenFOAMFileName='/home/olaaf/FOAM/AB/A/MasterCase/MasterCase.OpenFOAM',
    FullCarstlFileNames=['/home/olaaf/FOAM/AB/A/MasterCase/ParaPostPro/FullCar.stl'])

# find view
renderView2 = FindViewOrCreate('RenderView2', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView2.ViewSize = [731, 405]

# set active view
SetActiveView(renderView2)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.LockDataRange = 1
pLUT.InterpretValuesAsCategories = 0
pLUT.ShowCategoricalColorsinDataRangeOnly = 0
pLUT.RescaleOnVisibilityChange = 0
pLUT.EnableOpacityMapping = 0
pLUT.RGBPoints = [-2000.0, 0.0, 0.0, 1.0, 1500.0, 1.0, 0.0, 0.0]
pLUT.UseLogScale = 0
pLUT.ColorSpace = 'HSV'
pLUT.UseBelowRangeColor = 0
pLUT.BelowRangeColor = [0.0, 0.0, 0.0]
pLUT.UseAboveRangeColor = 0
pLUT.AboveRangeColor = [1.0, 1.0, 1.0]
pLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pLUT.Discretize = 1
pLUT.NumberOfTableValues = 64
pLUT.ScalarRangeInitialized = 1.0
pLUT.HSVWrap = 0
pLUT.VectorComponent = 0
pLUT.VectorMode = 'Magnitude'
pLUT.AllowDuplicateScalars = 1
pLUT.Annotations = []
pLUT.ActiveAnnotatedValues = []
pLUT.IndexedColors = []

# get color legend/bar for pLUT in view renderView2
pLUTColorBar = GetScalarBar(pLUT, renderView2)
pLUTColorBar.AutoOrient = 1
pLUTColorBar.Orientation = 'Vertical'
pLUTColorBar.WindowLocation = 'AnyLocation'
pLUTColorBar.Position = [0.849472674976031, 0.015929203539823]
pLUTColorBar.Title = 'Pressure'
pLUTColorBar.ComponentTitle = '[Pa]'
pLUTColorBar.TitleJustification = 'Centered'
pLUTColorBar.TitleColor = [1.0, 1.0, 1.0]
pLUTColorBar.TitleOpacity = 1.0
pLUTColorBar.TitleFontFamily = 'Arial'
pLUTColorBar.TitleBold = 0
pLUTColorBar.TitleItalic = 0
pLUTColorBar.TitleShadow = 0
pLUTColorBar.TitleFontSize = 16
pLUTColorBar.LabelColor = [1.0, 1.0, 1.0]
pLUTColorBar.LabelOpacity = 1.0
pLUTColorBar.LabelFontFamily = 'Arial'
pLUTColorBar.LabelBold = 0
pLUTColorBar.LabelItalic = 0
pLUTColorBar.LabelShadow = 0
pLUTColorBar.LabelFontSize = 16
pLUTColorBar.AutomaticLabelFormat = 1
pLUTColorBar.LabelFormat = '%-#6.3g'
pLUTColorBar.DrawTickMarks = 1
pLUTColorBar.DrawTickLabels = 1
pLUTColorBar.UseCustomLabels = 0
pLUTColorBar.CustomLabels = []
pLUTColorBar.AddRangeLabels = 1
pLUTColorBar.RangeLabelFormat = '%-#6.1f'
pLUTColorBar.DrawAnnotations = 1
pLUTColorBar.AddRangeAnnotations = 0
pLUTColorBar.AutomaticAnnotations = 0
pLUTColorBar.DrawNanAnnotation = 0
pLUTColorBar.NanAnnotation = 'NaN'
pLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
pLUTColorBar.ScalarBarThickness = 16
pLUTColorBar.ScalarBarLength = 0.390

# find view
renderView3 = FindViewOrCreate('RenderView3', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView3.ViewSize = [730, 405]

# set active view
SetActiveView(renderView3)

# get color legend/bar for pLUT in view renderView3
pLUTColorBar_1 = GetScalarBar(pLUT, renderView3)
pLUTColorBar_1.AutoOrient = 1
pLUTColorBar_1.Orientation = 'Vertical'
pLUTColorBar_1.WindowLocation = 'AnyLocation'
pLUTColorBar_1.Position = [0.82725527831094, 0.0477876106194691]
pLUTColorBar_1.Title = 'Pressure'
pLUTColorBar_1.ComponentTitle = '[Pa]'
pLUTColorBar_1.TitleJustification = 'Centered'
pLUTColorBar_1.TitleColor = [1.0, 1.0, 1.0]
pLUTColorBar_1.TitleOpacity = 1.0
pLUTColorBar_1.TitleFontFamily = 'Arial'
pLUTColorBar_1.TitleBold = 0
pLUTColorBar_1.TitleItalic = 0
pLUTColorBar_1.TitleShadow = 0
pLUTColorBar_1.TitleFontSize = 16
pLUTColorBar_1.LabelColor = [1.0, 1.0, 1.0]
pLUTColorBar_1.LabelOpacity = 1.0
pLUTColorBar_1.LabelFontFamily = 'Arial'
pLUTColorBar_1.LabelBold = 0
pLUTColorBar_1.LabelItalic = 0
pLUTColorBar_1.LabelShadow = 0
pLUTColorBar_1.LabelFontSize = 16
pLUTColorBar_1.AutomaticLabelFormat = 1
pLUTColorBar_1.LabelFormat = '%-#6.3g'
pLUTColorBar_1.DrawTickMarks = 1
pLUTColorBar_1.DrawTickLabels = 1
pLUTColorBar_1.UseCustomLabels = 0
pLUTColorBar_1.CustomLabels = []
pLUTColorBar_1.AddRangeLabels = 1
pLUTColorBar_1.RangeLabelFormat = '%-#6.1f'
pLUTColorBar_1.DrawAnnotations = 1
pLUTColorBar_1.AddRangeAnnotations = 0
pLUTColorBar_1.AutomaticAnnotations = 0
pLUTColorBar_1.DrawNanAnnotation = 0
pLUTColorBar_1.NanAnnotation = 'NaN'
pLUTColorBar_1.TextPosition = 'Ticks right/top, annotations left/bottom'
pLUTColorBar_1.ScalarBarThickness = 16
pLUTColorBar_1.ScalarBarLength = 0.390

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1470, 405]

# set active view
SetActiveView(renderView1)

# get color legend/bar for pLUT in view renderView1
pLUTColorBar_2 = GetScalarBar(pLUT, renderView1)
pLUTColorBar_2.AutoOrient = 1
pLUTColorBar_2.Orientation = 'Vertical'
pLUTColorBar_2.WindowLocation = 'AnyLocation'
pLUTColorBar_2.Position = [0.89541547277937, 0.0583038869257951]
pLUTColorBar_2.Title = 'Pressure'
pLUTColorBar_2.ComponentTitle = '[Pa]'
pLUTColorBar_2.TitleJustification = 'Centered'
pLUTColorBar_2.TitleColor = [1.0, 1.0, 1.0]
pLUTColorBar_2.TitleOpacity = 1.0
pLUTColorBar_2.TitleFontFamily = 'Arial'
pLUTColorBar_2.TitleBold = 0
pLUTColorBar_2.TitleItalic = 0
pLUTColorBar_2.TitleShadow = 0
pLUTColorBar_2.TitleFontSize = 16
pLUTColorBar_2.LabelColor = [1.0, 1.0, 1.0]
pLUTColorBar_2.LabelOpacity = 1.0
pLUTColorBar_2.LabelFontFamily = 'Arial'
pLUTColorBar_2.LabelBold = 0
pLUTColorBar_2.LabelItalic = 0
pLUTColorBar_2.LabelShadow = 0
pLUTColorBar_2.LabelFontSize = 16
pLUTColorBar_2.AutomaticLabelFormat = 1
pLUTColorBar_2.LabelFormat = '%-#6.3g'
pLUTColorBar_2.DrawTickMarks = 1
pLUTColorBar_2.DrawTickLabels = 1
pLUTColorBar_2.UseCustomLabels = 0
pLUTColorBar_2.CustomLabels = []
pLUTColorBar_2.AddRangeLabels = 1
pLUTColorBar_2.RangeLabelFormat = '%-#6.1f'
pLUTColorBar_2.DrawAnnotations = 1
pLUTColorBar_2.AddRangeAnnotations = 0
pLUTColorBar_2.AutomaticAnnotations = 0
pLUTColorBar_2.DrawNanAnnotation = 0
pLUTColorBar_2.NanAnnotation = 'NaN'
pLUTColorBar_2.TextPosition = 'Ticks right/top, annotations left/bottom'
pLUTColorBar_2.ScalarBarThickness = 16
pLUTColorBar_2.ScalarBarLength = 0.390

# current camera placement for renderView3
renderView3.CameraPosition = [0.796819527973984, -7.47934640096561, 0.776405342917503]
renderView3.CameraFocalPoint = [0.796819527973984, 2.34513466180722, 0.776405342917503]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraParallelScale = 2.54276280729466

# current camera placement for renderView1
renderView1.CameraPosition = [-3.80018015426134, -2.58818131712464, 1.25806138237725]
renderView1.CameraFocalPoint = [2.77871843344151, 1.96208410343195, -0.134033844665608]
renderView1.CameraViewUp = [0.14309214267827705, 0.09451836618606432, 0.9851857272399234]
renderView1.CameraParallelScale = 2.54276280729466

# current camera placement for renderView2
renderView2.CameraPosition = [5.41373167105133, 0.0, 0.767507970333099]
renderView2.CameraFocalPoint = [-4.4107493917215, 0.0, 0.767507970333099]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 2.54276280729466

# get layout
layout1 = GetLayout()

# save screenshot
SaveScreenshot('/home/olaaf/FOAM/GITCases/MasterCase/ParaPostPro/PressureView1.png', layout1, SaveAllViews=1,
    ImageResolution=[3840, 2160],
    FontScaling='Scale fonts proportionally',
    SeparatorWidth=0,
    SeparatorColor=[0.0, 0.0, 0.0],
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100)