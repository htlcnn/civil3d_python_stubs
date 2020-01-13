class AbbreviationAlignmentEnhancedType():
    """
    Defines Abbreviation Alignment Enhanced type.
    """
    pass

class AbbreviationAlignmentType():
    """
    Defines Abbreviation Alignment type.
    """
    pass

class AbbreviationCantType():
    """
    Defines cant type abbreviations.
    """
    pass

class AbbreviationProfileType():
    """
    Defines Abbreviation Profile type.
    """
    pass

class AbbreviationSuperelevationType():
    """
    Defines Abbreviation Superelevation type.
    """
    pass

class AutomaticManual():
    """
    Specifies how some properties are assigned point creation.
    """
    pass

class DrawingUnitType():
    """
    Specifies the linear units (feet or meters) for drawing entities in AutoCAD model space.
    """
    pass

class GeographicCoordinateType():
    """
    Specifies the order in which geographic coordinates are displayed on the command line during point creation.
    """
    pass

class GridCoordinateType():
    """
    Specifies the order in which grid coordinates are displayed on the command line during point creation.
    """
    pass

class GridScaleFactorType():
    """
    Specifies the type of scale factor.
    """
    pass

class ImperialToMetricConversionType():
    """
    Specifies the Imperial to Metric conversion type for the drawing.
    """
    pass

class LandXMLAngularUnits():
    """
    Specifies the units of the exported angles and directions.
    """
    pass

class LandXMLAttributeExportType():
    """
    Specifies the field that is used for specific attribute in the LandXML file.
    """
    pass

class LandXMLBreakLinesImportType():
    """
    Specifies how to import the BreakLines.
    """
    pass

class LandXMLConflictResolutionType():
    """
    Specifies how objects with the same name are handled.
    """
    pass

class LandXMLImperialUnitType():
    """
    Defines the default imperial pipe and structure diameter units that are applied when units are not specified in the source LandXML file.
    """
    pass

class LandXMLLinearUnits():
    """
    Specifies how to tag LandXML data when working in Imperial units.
    """
    pass

class LandXMLMetricUnitType():
    """
    Defines the default metric pipe and structure diameter units that are applied when units are not specified in the source LandXML file.
    """
    pass

class LandXMLPointDescriptionType():
    """
    Specifies how to map the ‘desc’ and ‘code’ attributes to the point descriptions.
    """
    pass

class LandXMLSurfaceDataExportType():
    """
    Specifies how to export the surface data.
    """
    pass

class LandXMLSurfaceDataImportType():
    """
    Specifies how to import the data.
    NoteIf the LandXML surface you intend to import has only breaklines (for example, no other points and faces definition data is present), 
    the resulting Autodesk Civil 3D surface is built from the breakline data. However, the breaklines are not available for editing (that is, they do not appear in the Prospector tree).
    """
    pass

class LocalCoordinateType():
    """
    Specifies the order and format used to display local coordinates on the command line during point creation.
    """
    pass

class MapcheckAngleType():
    """
    Definition of MapCheck Angle type.
    """
    pass

class MapcheckCurveDirectionType():
    """
    Definition of MapCheck Curve Direction type.
    """
    pass

class MapcheckSideType():
    """
    Definition of MapCheck side type.
    """
    pass

class MapcheckTraverseMethodType():
    """
    Definition of MapCheck Traverse Method type.
    """
    pass

class ObjectLayerModifierType():
    """
    Specifies whether the layer name includes a 
    text-string modifier, and if so, the location of the modifier.
    """
    pass

class SectionViewAnchorType():
    """
    Defines types of section view anchors.
    """
    pass

class SettingsAbbreviation(object):
    """
    Contains profile and alignment abbreviation strings as specified on the Abbreviations tab of the Drawing Settings dialog box.
    """
    AlignmentGeoPointEntityData = None
    AlignmentGeoPointText = None
    Cant = None
    GeneralText = None
    Profile = None
    Superelevation = None
    pass

class SettingsAbbreviationAlignment(object):
    """
    Abbreviations Settings for Alignment Geometry Point Entity Data
    """
    def GetAlignmentAbbreviation(self):
        """
        GetAlignmentAbbreviation(type: Autodesk.Civil.Settings.AbbreviationAlignmentType) -> AbbreviationAlignmentType
            Gets the alignment abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationAlignmentType - The type of settings to get.
        """
        pass
    
    
    def SetAlignmentAbbreviation(self):
        """
        SetAlignmentAbbreviation(type: Autodesk.Civil.Settings.AbbreviationAlignmentType, value: System.String) -> AbbreviationAlignmentType
            Sets the alignment abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationAlignmentType - The type of settings to set.
            value: System.String - The value to set.
        """
        pass
    
    pass

class SettingsAbbreviationAlignmentEnhanced(object):
    """
    Abbreviations Settings for Alignment Geometry Point Text
    """
    def GetAlignmentEnhancedAbbreviation(self):
        """
        GetAlignmentEnhancedAbbreviation(type: Autodesk.Civil.Settings.AbbreviationAlignmentEnhancedType) -> AbbreviationAlignmentEnhancedType
            Gets the alignment enhanced abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationAlignmentEnhancedType - The type of settings to get.
        """
        pass
    
    
    def SetAlignmentEnhancedAbbreviation(self):
        """
        SetAlignmentEnhancedAbbreviation(type: Autodesk.Civil.Settings.AbbreviationAlignmentEnhancedType, newValue: System.String) -> AbbreviationAlignmentEnhancedType
            Sets the alignment enhanced abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationAlignmentEnhancedType - The type of settings to set.
            newValue: System.String - The value to set.
        """
        pass
    
    pass

class SettingsAbbreviationCant(object):
    """
    Abbreviation settings for Cant.
    """
    def GetCantAbbreviation(self):
        """
        GetCantAbbreviation(type: Autodesk.Civil.Settings.AbbreviationCantType) -> AbbreviationCantType
            Gets the cant abbreviation settings.
            type: Autodesk.Civil.Settings.AbbreviationCantType - The type of SettingsAbbreviationCant to get.
        """
        pass
    
    
    def SetCantAbbreviation(self):
        """
        SetCantAbbreviation(type: Autodesk.Civil.Settings.AbbreviationCantType, newValue: System.String) -> AbbreviationCantType
            Sets the cant abbreviation settings.
            type: Autodesk.Civil.Settings.AbbreviationCantType - The type of SettingsAbbreviationCant to set.
            newValue: System.String - The value to set.
        """
        pass
    
    pass

class SettingsAbbreviationGeneral(object):
    """
    Abbreviations Settings for abbreviations that are not feature specific.
    """
    Infinity = None
    Left = None
    Right = None
    pass

class SettingsAbbreviationProfile(object):
    """
    Abbreviations Settings for Profile
    """
    def GetProfileAbbreviation(self):
        """
        GetProfileAbbreviation(type: Autodesk.Civil.Settings.AbbreviationProfileType) -> AbbreviationProfileType
            Gets the profile abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationProfileType - The type of settings to get.
        """
        pass
    
    
    def SetProfileAbbreviation(self):
        """
        SetProfileAbbreviation(type: Autodesk.Civil.Settings.AbbreviationProfileType, newValue: System.String) -> AbbreviationProfileType
            Sets the profile abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationProfileType - The type of settings to set.
            newValue: System.String - The value to set.
        """
        pass
    
    pass

class SettingsAbbreviationSuperelevation(object):
    """
    Abbreviations Settings for Superelevation
    """
    def GetSuperelevationAbbreviation(self):
        """
        GetSuperelevationAbbreviation(type: Autodesk.Civil.Settings.AbbreviationSuperelevationType) -> AbbreviationSuperelevationType
            Gets the superelevation abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationSuperelevationType - The type of settings to get.
        """
        pass
    
    
    def SetSuperelevationAbbreviation(self):
        """
        SetSuperelevationAbbreviation(type: Autodesk.Civil.Settings.AbbreviationSuperelevationType, newValue: System.String) -> AbbreviationSuperelevationType
            Sets the superelevation abbreviation settings
            type: Autodesk.Civil.Settings.AbbreviationSuperelevationType - The type of settings to set.
            newValue: System.String - The value to set.
        """
        pass
    
    pass

class SettingsAlignment(SettingsAmbient):
    """
    Settings for Alignment.
    """
    AutomaticWideningAroundCurves = None
    CantOptions = None
    ConstraintEditing = None
    CriteriaBasedDesignOptions = None
    Data = None
    DefaultNameFormat = None
    DynamicAlignmentHighlight = None
    ImpliedPointOfIntersection = None
    RailOptions = None
    StationIndexing = None
    StyleSettings = None
    SuperelevationOptions = None
    pass

class SettingsAlignment.SettingsAutomaticWideningAroundCurves(object):
    """
    
    """
    AutomaticWideningAtCurves = None
    ManualTransitionLength = None
    ManualWideningWidth = None
    WheelbaseLength = None
    WideningApplySide = None
    WideningMethod = None
    pass

class SettingsAlignment.SettingsCantOptions(object):
    """
    Cant options setting class.
    """
    DesignSpeedLookupMethod = None
    EquationRoundingOption = None
    EquilibriumCantFormula = None
    MaxAppliedCantOnTangent = None
    MaxDeficiencyFormula = None
    PivotMethod = None
    RadiusLookupMethod = None
    SpiralSpiralCurve = None
    StationRoundingOption = None
    TangentTangentCurve = None
    pass

class SettingsAlignment.SettingsConstraintEditing(object):
    """
    Constraint editing options settings class.
    """
    AlwaysPerformImpliedSwapping = None
    LockInitialParameters = None
    pass

class SettingsAlignment.SettingsCriteriaBasedDesignOptions(object):
    """
    Criteria Based Design options settings class.
    """
    DefaultDesignCheckSet = None
    DefaultDesignCheckSetId = None
    DesignSpeed = None
    DesignSpeedLookupMethod = None
    RadiusLookupMethod = None
    UseCriteriaBasedDesignOption = None
    UseDesignChecksOption = None
    UseDesignCriteriaFileOption = None
    pass

class SettingsAlignment.SettingsData(object):
    """
    Criteria Based Design options settings class.
    """
    CriteriaBasedDesignOption = None
    pass

class SettingsAlignment.SettingsDefaultNameFormat(object):
    """
    Default name format settings class.
    """
    AlignmentNameTemplate = None
    OffsetAlignmentNameTemplate = None
    pass

class SettingsAlignment.SettingsDynamicAlignmentHighlight(object):
    """
    Dynamic alignment highlight setting class.
    """
    CurbReturnFilletRegionColor = None
    CurbReturnFilletRegionLineweight = None
    OffsetRegionColor = None
    OffsetRegionLineweight = None
    ParentAlignmentColor = None
    ParentAlignmentLineweight = None
    ParentAlignmentTrackerColor = None
    ParentAlignmentTrackerLineweight = None
    TransitionRegionColor = None
    TransitionRegionLineweight = None
    pass

class SettingsAlignment.SettingsImpliedPointOfIntersection(object):
    """
    Implied Point Of Intersection settings class.
    """
    DisplayMethod = None
    pass

class SettingsAlignment.SettingsRailAlignmentOptions(object):
    """
    Rail Alignment options setting class.
    """
    MeasureRailCurvesAlongChords = None
    TrackWidth = None
    pass

class SettingsAlignment.SettingsStationIndexing(object):
    """
    Station indexing settings class.
    """
    DefaultStationIndexIncrement = None
    pass

class SettingsAlignment.SettingsStyles(object):
    """
    Default styles settings class.
    """
    AlignmentLabelSet = None
    AlignmentLabelSetId = None
    AlignmentStyle = None
    AlignmentStyleId = None
    CurveLabelStyle = None
    CurveLabelStyleId = None
    LineLabelStyle = None
    LineLabelStyleId = None
    MarkerStyle = None
    MarkerStyleId = None
    PointOfIntersectLabelStyle = None
    SpiralLabelStyle = None
    SpiralLabelStyleId = None
    StationOffsetLabelStyle = None
    StationOffsetLabelStyleId = None
    TangentIntersectLabelStyle = None
    pass

class SettingsAlignment.SettingsSuperelevationOptions(object):
    """
    Superelevation options settings class.
    """
    CorridorType = None
    CrossSectionShape = None
    DividedCrownedMedianTreatment = None
    DividedCrownedPivotMethod = None
    DividedPlanarMedianTreatment = None
    DividedPlanarPivotMethod = None
    HighsideLocation = None
    InsideEdgeShoulderTreatmentInHighSide = None
    InsideEdgeShoulderTreatmentInLowSide = None
    InsideShoulderMethod = None
    MaximumShoulderRollover = None
    NominalWidth = None
    NormalLaneSlope = None
    NormalShoulderSlope = None
    OutsideEdgeShoulderTreatmentInHighSide = None
    OutsideEdgeShoulderTreatmentInLowSide = None
    OutsideShoulderMethod = None
    StationRoundingOption = None
    UndividedCrownedPivotMethod = None
    UndividedPlanarPivotMethod = None
    pass

class SettingsAmbient(SettingsAlignment):
    """
    Specifies default ambient (background) settings for units of measurement. 
    These units are used throughout Autodesk Civil 3D, unless they are overridden 
    at the feature or command level.
    """
    Acceleration = None
    Angle = None
    Area = None
    Coordinate = None
    DegreeOfCurvature = None
    Dimension = None
    Direction = None
    Distance = None
    Elevation = None
    General = None
    Grade = None
    GradeSlope = None
    GridCoordinate = None
    Labeling = None
    LatLong = None
    Pressure = None
    Slope = None
    Speed = None
    Station = None
    Time = None
    TransparentCommands = None
    Unitless = None
    Volume = None
    pass

class SettingsAmbient.SettingsAcceleration(SettingsUnitlessNumber):
    """
    Specifies how to display acceleration.
    """

    pass

class SettingsAmbient.SettingsAngle(SettingsUnitlessNumber):
    """
    Specifies how to display deflection angles between two vectors.
    """
    DropDecimalForWholeNumbers = None
    DropLeadingZerosForDegrees = None
    pass

class SettingsAmbient.SettingsArea(SettingsUnitlessNumber):
    """
    Specifies how to display surface areas.
    """

    pass

class SettingsAmbient.SettingsCoordinate(SettingsUnitlessNumber):
    """
    Specifies how to display X and Y coordinates.
    """

    pass

class SettingsAmbient.SettingsDegreeOfCurvature(object):
    """
    Specifies unit chord length and unit arc length.
    """
    UnitArcLength = None
    UnitChordLength = None
    pass

class SettingsAmbient.SettingsDimension(SettingsUnitlessNumber):
    """
    Specifies how to display linear dimensions.
    """

    pass

class SettingsAmbient.SettingsDirection(SettingsUnitlessNumber):
    """
    Specifies how to display directions.
    """
    BearingQuadrant = None
    Capitalization = None
    Direction = None
    DropDecimalForWholeNumbers = None
    DropLeadingZerosForDegrees = None
    MeasurementType = None
    pass

class SettingsAmbient.SettingsDistance(SettingsUnitlessNumber):
    """
    Specifies how to display linear distances.
    """

    pass

class SettingsAmbient.SettingsElevation(SettingsUnitlessNumber):
    """
    Specifies how to display surface elevations.
    """

    pass

class SettingsAmbient.SettingsFormatNumber(SettingsUnitlessNumber):
    """
    Representing a formattable number's settings, this is the base class for many other formattable number measurement.
    """
    Format = None
    pass

class SettingsAmbient.SettingsGeneral(object):
    """
    Specifies how to display text, numbers, and units.
    """
    DrivingDirection = None
    IndependentLayerOn = None
    NewEntityToolTipState = None
    PlottedUnitDisplay = None
    SaveCommandChangesToSettings = None
    ShowEventViewer = None
    ShowToolTips = None
    pass

class SettingsAmbient.SettingsGrade(SettingsUnitlessNumber):
    """
    Specifies how to display grade measurements.
    """

    pass

class SettingsAmbient.SettingsGradeSlope(SettingsUnitlessNumber):
    """
    Specifies how to display grade and slope measurements.
    """

    pass

class SettingsAmbient.SettingsGridCoordinate(SettingsUnitlessNumber):
    """
    The GridCoordinate settings class
    """

    pass

class SettingsAmbient.SettingsLabeling(object):
    """
    Specifies the default method for prompting for objects when inserting labels that contain Referenced Text components.
    """
    PromptMethod = None
    pass

class SettingsAmbient.SettingsLatLong(SettingsUnitlessNumber):
    """
    Specifies how to display latitude and longitude.
    """
    Capitalization = None
    Direction = None
    DropDecimalForWholeNumbers = None
    DropLeadingZerosForDegrees = None
    pass

class SettingsAmbient.SettingsPressure(SettingsUnitlessNumber):
    """
    Specifies how to display pressure measurements.
    """

    pass

class SettingsAmbient.SettingsSlope(SettingsUnitlessNumber):
    """
    Specifies how to display slope measurements.
    """

    pass

class SettingsAmbient.SettingsSpeed(SettingsUnitlessNumber):
    """
    Specifies how to display speeds for design criteria.
    """

    pass

class SettingsAmbient.SettingsStation(SettingsUnitlessNumber):
    """
    Specifies how to display linear features that use station or chainage.
    """
    DropDecimalForWholeNumbers = None
    DropLeadingZerosRightOfStationCharacter = None
    MinimumDisplayWidth = None
    StationDelimiterCharacter = None
    StationDelimiterPosition = None
    pass

class SettingsAmbient.SettingsTime(object):
    """
    These settings specify how to display time.
    """
    Precision = None
    Rounding = None
    Unit = None
    pass

class SettingsAmbient.SettingsTransparentCommands(object):
    """
    Specifies the prompting behavior of transparent commands across all features. 
    The formats used to prompt for grade and slope values are set using the Grade and 
    Slope ambient settings.
    """
    PromptFor3DPoints = None
    PromptForEastingThenNorthing = None
    PromptForLongitudeThenLatitude = None
    PromptForYBeforeX = None
    pass

class SettingsAmbient.SettingsUnitFormatNumber(SettingsUnitlessNumber):
    """
    Representing a formattable unit number's settings, this is the base class for many other formattable unit number measurement.
    """
    Format = None
    Unit = None
    pass

class SettingsAmbient.SettingsUnitNumber(SettingsUnitlessNumber):
    """
    Representing a unit number's settings, this is the base class for many other unit number based measurement
    """
    Unit = None
    pass

class SettingsAmbient.SettingsUnitless(SettingsUnitlessNumber):
    """
    These settings specify how to display numeric values that are not specifically defined by the unit type.
    """

    pass

class SettingsAmbient.SettingsUnitlessNumber(SettingsFormatNumber):
    """
    Representing a unitless number's settings, this is the base class for many other number based measurement
    """
    Precision = None
    Rounding = None
    Sign = None
    pass

class SettingsAmbient.SettingsVolume(SettingsUnitlessNumber):
    """
    Specifies how to display terrain volumes.
    """

    pass

class SettingsAssembly(SettingsAmbient):
    """
    Settings for Assembly.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsAssembly.SettingsNameFormat(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    Assembly = None
    Group = None
    Offset = None
    pass

class SettingsAssembly.SettingsStyles(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    Assembly = None
    AssemblyStyleId = None
    CodeSet = None
    CodeSetStyleId = None
    pass

class SettingsBuildingSite(SettingsAmbient):
    """
    Settings for ViewFrameGroup.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsBuildingSite.SettingsNameFormat(object):
    """
    default name format for new building sites.
    """
    BuildingSite = None
    pass

class SettingsBuildingSite.SettingsStyles(object):
    """
    default styles for new building sites.
    """
    BuildingSite = None
    BuildingSiteStyleId = None
    pass

class SettingsCantView(SettingsAmbient):
    """
    Encapsulates settings for CantView.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsCantView.SettingsNameFormat(object):
    """
    Settings for CantView default NameFormat.
    """
    CantView = None
    pass

class SettingsCantView.SettingsStyles(object):
    """
    Settings for CantView default Styles.
    """
    CantViewStyle = None
    CantViewStyleId = None
    pass

class SettingsCatchment(SettingsAmbient):
    """
    Settings for Catchment.
    """
    NameTemplate = None
    Styles = None
    pass

class SettingsCatchment.SettingsStyles(object):
    """
    Settings for catchment styles.
    """
    CatchmentLabelStyle = None
    CatchmentLabelStyleId = None
    CatchmentStyle = None
    CatchmentStyleId = None
    FlowSegmentLabelStyle = None
    FlowSegmentLabelStyleId = None
    pass

class SettingsCmdAddAlignPointOfIntLbl(SettingsAmbient):
    """
    Settings for AddAlignPointOfIntLbl command.
    """

    pass

class SettingsCmdAddAlignPointOfIntLbls(SettingsAmbient):
    """
    Settings for AddAlignPointOfIntLbls command.
    """

    pass

class SettingsCmdAddAlignSegLbl(SettingsAmbient):
    """
    Settings for AddAlignSegLbl command.
    """

    pass

class SettingsCmdAddAlignSegLbls(SettingsAmbient):
    """
    Settings for AddAlignSegLbls command.
    """

    pass

class SettingsCmdAddAlignTagentLbl(SettingsAmbient):
    """
    Settings for AddAlignTagentLbl command.
    """

    pass

class SettingsCmdAddAlignTagentLbls(SettingsAmbient):
    """
    Settings for AddAlignTagentLbls command.
    """

    pass

class SettingsCmdAddAlignmentCurveTable(SettingsAmbient):
    """
    Settings for AddAlignmentCurveTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddAlignmentCurveTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddAlignmentCurveTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddAlignmentLineTable(SettingsAmbient):
    """
    Settings for AddAlignmentLineTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddAlignmentLineTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddAlignmentLineTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddAlignmentOffLbl(SettingsAmbient):
    """
    Settings for AddAlignmentOffLbl command.
    """

    pass

class SettingsCmdAddAlignmentOffXYLbl(SettingsAmbient):
    """
    Settings for AddAlignmentOffXYLbl command.
    """

    pass

class SettingsCmdAddAlignmentSegmentTable(SettingsAmbient):
    """
    Settings for AddAlignmentSegmentTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddAlignmentSegmentTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddAlignmentSegmentTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddAlignmentSpiralTable(SettingsAmbient):
    """
    Settings for AddAlignmentSpiralTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddAlignmentSpiralTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddAlignmentSpiralTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddContourLabeling(SettingsAmbient):
    """
    Settings for AddContourLabeling command.
    """

    pass

class SettingsCmdAddContourLabelingGroup(SettingsAmbient):
    """
    Settings for AddContourLabelingGroup command.
    """
    AddContourLabeling = None
    pass

class SettingsCmdAddContourLabelingGroup.SettingsCmdAddContourLabeling(object):
    """
    Settings that specify the defaults assigned to surface labels.
    """
    IntervalAlongContour = None
    pass

class SettingsCmdAddContourLabelingSingle(SettingsAmbient):
    """
    Settings for AddContourLabelingSingle command.
    """

    pass

class SettingsCmdAddIntersectionLabel(SettingsAmbient):
    """
    Settings for AddIntersectionLabel command.
    """

    pass

class SettingsCmdAddLineBetweenPoints(SettingsAmbient):
    """
    Encapsulates settings for the AddLineBetweenPoints command.
    """

    pass

class SettingsCmdAddMaterialVolumeTable(SettingsAmbient):
    """
    Settings for AddMaterialVolumeTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddMaterialVolumeTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for command AddMaterialVolumeTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddNetworkPartPlanLabel(SettingsAmbient):
    """
    Settings for AddNetworkPartPlanLabel command.
    """

    pass

class SettingsCmdAddNetworkPartProfLabel(SettingsAmbient):
    """
    Settings for AddNetworkPartProfLabel command.
    """

    pass

class SettingsCmdAddNetworkPartSectLabel(SettingsAmbient):
    """
    Settings for AddNetworkPartSectLabel command.
    """

    pass

class SettingsCmdAddNetworkPartsToProf(SettingsAmbient):
    """
    Settings for AddNetworkPartsToProf command.
    """

    pass

class SettingsCmdAddNetworkPipeTable(SettingsAmbient):
    """
    Settings for AddNetworkPlanTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddNetworkPipeTable.SettingsCmdTableCreation(object):
    """
    Settings for alignment type option.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddNetworkPlanLabels(SettingsAmbient):
    """
    Settings for AddNetworkPlanLabels command.
    """

    pass

class SettingsCmdAddNetworkProfLabels(SettingsAmbient):
    """
    Settings for AddNetworkProfLables command.
    """

    pass

class SettingsCmdAddNetworkSectLabels(SettingsAmbient):
    """
    Settings for AddNetworkSectLables command.
    """

    pass

class SettingsCmdAddNetworkStructTable(SettingsAmbient):
    """
    Settings for AddNetworkStructTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddNetworkStructTable.SettingsCmdTableCreation(object):
    """
    Settings for alignment type option.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddNoteLabel(SettingsAmbient):
    """
    Settings for AddNoteLabel command.
    """

    pass

class SettingsCmdAddParcelAreaLabel(SettingsAmbient):
    """
    Settings for AddParcelAreaLabel command.
    """

    pass

class SettingsCmdAddParcelCurveTable(SettingsAmbient):
    """
    Settings for AddParcelCurveTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddParcelCurveTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddParcelCurveTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddParcelLineLabel(SettingsAmbient):
    """
    Settings for AddParcelLineLabel command.
    """

    pass

class SettingsCmdAddParcelLineTable(SettingsAmbient):
    """
    Settings for AddParcelLineTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddParcelLineTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddParcelLineTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddParcelSegmentLabels(SettingsAmbient):
    """
    Settings for AddParcelSegmentLabels command.
    """
    Options = None
    pass

class SettingsCmdAddParcelSegmentLabels.SettingsCmdOptions(object):
    """
    Settings that specify defaults for creating labels with parcel segments.
    """
    LabelingDirection = None
    pass

class SettingsCmdAddParcelSegmentTable(SettingsAmbient):
    """
    Settings for AddParcelSegmentTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddParcelSegmentTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddParcelSegmentTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddParcelTable(SettingsAmbient):
    """
    Settings for AddParcelTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddParcelTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddParcelTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddPointCloudPoints(SettingsAmbient):
    """
    Settings for AddPointCloudPoints command.
    """
    DefaultFileFormat = None
    pass

class SettingsCmdAddPointTable(SettingsAmbient):
    """
    Settings for AddPointTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddPointTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for the command AddPointTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddPointsToSurface(SettingsAmbient):
    """
    Settings for AddPointsToSurface command.
    """
    MidOrdinateDistance = None
    RegionOption = None
    SurfaceOption = None
    pass

class SettingsCmdAddProfileViewDepthLbl(SettingsAmbient):
    """
    Settings for AddProfileViewDepthLbl command.
    """

    pass

class SettingsCmdAddProfileViewStaElevLbl(SettingsAmbient):
    """
    Settings for AddProfileViewStaElevLbl command.
    """

    pass

class SettingsCmdAddSectionViewGradeLbl(SettingsAmbient):
    """
    Settings for AddSectionViewGradeLbl command.
    """

    pass

class SettingsCmdAddSectionViewOffElevLbl(SettingsAmbient):
    """
    Settings for AddSectionViewOffElevLbl command.
    """

    pass

class SettingsCmdAddSegmentLabel(SettingsAmbient):
    """
    Settings for AddSegmentLabel command.
    """

    pass

class SettingsCmdAddSegmentLabels(SettingsAmbient):
    """
    Settings for AddSegmentLabels command.
    """

    pass

class SettingsCmdAddSpanningPipePlanLabel(SettingsAmbient):
    """
    Settings for AddSpanningPipePlanLabel command.
    """

    pass

class SettingsCmdAddSpanningPipeProfLabel(SettingsAmbient):
    """
    Settings for AddSpanningPipeProfLabel command.
    """

    pass

class SettingsCmdAddSpotElevLabelsOnGrid(SettingsAmbient):
    """
    Settings for AddSpotElevLabelsOnGrid command.
    """

    pass

class SettingsCmdAddSurfaceBoundaries(SettingsAmbient):
    """
    Settings for AddSurfaceBoundaries command.
    """
    DataOptions = None
    pass

class SettingsCmdAddSurfaceBoundaries.SettingsCmdAddDataOptions(object):
    """
    Settings that specify the defaults assigned when adding contours, boundaries, and breaklines to a surface.
    """
    BoundaryType = None
    MidOrdinateDistance = None
    NonDestructive = None
    pass

class SettingsCmdAddSurfaceBreaklines(SettingsAmbient):
    """
    Settings for AddSurfaceBreaklines command.
    """
    DataOptions = None
    pass

class SettingsCmdAddSurfaceBreaklines.SettingsCmdAddDataOptions(object):
    """
    Settings that specify the defaults assigned when adding contours, boundaries, and breaklines to a surface.
    """
    ApplySupplementing = None
    ApplyWeeding = None
    MidOrdinateDistance = None
    SupplementingDistance = None
    WeedingAngle = None
    WeedingDistance = None
    pass

class SettingsCmdAddSurfaceContours(SettingsAmbient):
    """
    Settings for AddSurfaceContours command.
    """
    AddDataOptions = None
    pass

class SettingsCmdAddSurfaceContours.SettingsCmdAddDataOptions(object):
    """
    Settings that specify the defaults assigned when adding contours, boundaries, and breaklines to a surface.
    """
    AddPointsToFlatEdges = None
    AddPointsToFlatTriangles = None
    FillGapsInContourData = None
    MidOrdinateDistance = None
    SupplementingDistance = None
    SwapEdges = None
    WeedingAngle = None
    WeedingDistance = None
    pass

class SettingsCmdAddSurfaceDemFile(SettingsAmbient):
    """
    Settings for AddSurfaceDemFile command.
    """
    ImportOptions = None
    pass

class SettingsCmdAddSurfaceDemFile.SettingsCmdImportOptions(object):
    """
    Settings that specify the defaults assigned when creating surfaces.
    """
    NullElevation = None
    UseCustomNullElevation = None
    pass

class SettingsCmdAddSurfaceDrawingObjects(SettingsAmbient):
    """
    Settings for AddSurfaceDrawingObjects command.
    """
    DataOptions = None
    pass

class SettingsCmdAddSurfaceDrawingObjects.SettingsCmdAddDataOptions(object):
    """
    Settings that specify the defaults assigned when adding contours, boundaries, and breaklines to a surface.
    """
    HasMaintainedges = None
    pass

class SettingsCmdAddSurfaceFigSurveyQuery(SettingsAmbient):
    """
    Settings for the AddSurfaceFigSurveyQuery command.
    """
    DataOptions = None
    pass

class SettingsCmdAddSurfaceFigSurveyQuery.SettingsCmdAddDataOptions(object):
    """
    Settings that specify the defaults assigned when adding a figure survey query to a surface.
    """
    MidOrdinateDistance = None
    pass

class SettingsCmdAddSurfacePointSurveyQuery(SettingsAmbient):
    """
    Encapsulates settings for the AddSurfacePointSurveyQuery command.
    """

    pass

class SettingsCmdAddSurfaceSlopeLabel(SettingsAmbient):
    """
    Settings for AddSurfaceSlopeLabel command.
    """

    pass

class SettingsCmdAddSurfaceSpotElevLabel(SettingsAmbient):
    """
    Settings for AddSurfaceSpotElevLabel command.
    """

    pass

class SettingsCmdAddSvFigureLabel(SettingsAmbient):
    """
    This class ecapsulates settings for the AddSvFigureLabel command.
    """

    pass

class SettingsCmdAddSvFigureSegmentLabel(SettingsAmbient):
    """
    This class encapuslates settings for the AddSvFigureSegmentLabel command.
    """

    pass

class SettingsCmdAddSvFigureSegmentLabels(SettingsAmbient):
    """
    This class encapuslates settings for the AddSvFigureSegmentLabels command.
    """

    pass

class SettingsCmdAddTotalVolumeTable(SettingsAmbient):
    """
    Settings for AddTotalVolumeTable command.
    """
    TableCreation = None
    pass

class SettingsCmdAddTotalVolumeTable.SettingsCmdTableCreation(object):
    """
    Settings of table creation for command AddTotalVolumeTable.
    """
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SplitTable = None
    TableSpacing = None
    TableStyle = None
    TableStyleId = None
    TileDirection = None
    pass

class SettingsCmdAddWidening(SettingsAmbient):
    """
    Settings for AddWidening command.
    """
    LinearTransitionAroundCurves = None
    WideningOptions = None
    pass

class SettingsCmdAddWidening.SettingsCmdLinearTransitionAroundCurves(object):
    """
    Settings for the alignment linear transition around curves.
    """
    NumberOfSegments = None
    TransitionSegmentType = None
    pass

class SettingsCmdAddWidening.SettingsCmdWideningOptions(object):
    """
    Settings for the alignment widening options.
    """
    RadiusForCurve1 = None
    RadiusForCurve2 = None
    RadiusForCurve3 = None
    TaperInputType = None
    TaperRatio = None
    TransitionLength = None
    TransitionType = None
    WideningOffset = None
    WideningSegmentLength = None
    pass

class SettingsCmdAssignPayItemToArea(SettingsAmbient):
    """
    Settings for AssignPayItemToArea command.
    """
    AssignPayItemToAreaOption = None
    pass

class SettingsCmdAssignPayItemToArea.SettingsCmdAssignPayItemToAreaOptions(object):
    """
    Settings of pay item assignment for command AssignPayItemToArea.
    """
    ColorForHatch = None
    LayerForHatch = None
    UseAcadLayerAndColor = None
    pass

class SettingsCmdCatchmentArea(SettingsAmbient):
    """
    Settings for CatchmentArea command.
    """
    DischargePointStyle = None
    DischargePointStyleId = None
    DisplayDisChargePoint = None
    Layer = None
    ObjectType = None
    pass

class SettingsCmdComputeMaterials(SettingsAmbient):
    """
    Settings for ComputeMaterials command.
    """
    DefineMaterialOption = None
    pass

class SettingsCmdComputeMaterials.SettingsCmdDefineMaterial(object):
    """
    Settings of material definition for command ComputeMaterials.
    """
    ApplyCurveCorrection = None
    CurveCorrectionTolerance = None
    pass

class SettingsCmdConvertPointstoSdskPoints(SettingsAmbient):
    """
    Settings for ConvertPointstoSdskPoints command.
    """
    Layer = None
    pass

class SettingsCmdConvertPointstoSdskPoints.SettingsCmdLayer(object):
    """
    Settings that specify defaults for Layer.
    """
    Layer = None
    pass

class SettingsCmdCorridorExtractSurfaces(SettingsAmbient):
    """
    Settings for CorridorExtractSurfaces command.
    """

    pass

class SettingsCmdCreateAlignFromCorridor(SettingsAmbient):
    """
    Settings for CreateAlignFromCorridor command.
    """
    AlignmentTypeOption = None
    CriteriaBasedDesignOptions = None
    ProfileCreationOption = None
    pass

class SettingsCmdCreateAlignFromCorridor.SettingsCmdAlignmentTypeOption(object):
    """
    Settings for alignment type option.
    """
    AlignmentType = None
    pass

class SettingsCmdCreateAlignFromCorridor.SettingsCmdCriteriaBasedDesignOptions(object):
    """
    Settings for criteria based design options.
    """
    DefaultDesignCheckSet = None
    DefaultDesignCheckSetId = None
    DesignSpeed = None
    DesignSpeedLookupMethod = None
    RadiusLookupMethod = None
    UseCriteriaBasedDesignOption = None
    UseDesignChecksOption = None
    UseDesignCriteriaFileOption = None
    pass

class SettingsCmdCreateAlignFromCorridor.SettingsCmdProfileCreationOption(object):
    """
    Settings for profile creation option.
    """
    CreateProfileFromCorridor = None
    pass

class SettingsCmdCreateAlignFromNetwork(SettingsAmbient):
    """
    Settings for CreateAlignFromNetwork command.
    """
    AlignmentTypeOption = None
    pass

class SettingsCmdCreateAlignFromNetwork.SettingsCmdAlignmentTypeOption(object):
    """
    Settings for alignment type option.
    """
    AlignmentType = None
    pass

class SettingsCmdCreateAlignmentEntities(SettingsAmbient):
    """
    Settings for CreateAlignmentEntities command.
    """
    AlignmentTypeOption = None
    CreateFromEntities = None
    pass

class SettingsCmdCreateAlignmentEntities.SettingsCmdAlignmentTypeOption(object):
    """
    Settings for alignment type option when creating alignment entities.
    """
    AlignmentType = None
    pass

class SettingsCmdCreateAlignmentEntities.SettingsCmdCreateFromEntities(object):
    """
    Settings for creating alignment entities.
    """
    AddCurveBetweenTangents = None
    EraseExistingEntities = None
    Radius = None
    pass

class SettingsCmdCreateAlignmentLayout(SettingsAmbient):
    """
    Settings for CreateAlignmentLayout command.
    """
    AlignmentTypeOption = None
    CurveAndSpiralSettings = None
    CurveTessellationOption = None
    RegressionGraphOption = None
    pass

class SettingsCmdCreateAlignmentLayout.SettingsCmdAlignmentTypeOption(object):
    """
    Settings of alignment type option for the command CreateAlignmentLayout.
    """
    AlignmentType = None
    pass

class SettingsCmdCreateAlignmentLayout.SettingsCmdCurveAndSpiralSettings(object):
    """
    Settings of curve and spiral for the command CreateAlignmentLayout.
    """
    CurveRadiusForSCSGroup = None
    SpiralInAValue = None
    SpiralInLength = None
    SpiralOutAValue = None
    SpiralOutLength = None
    SpiralType = None
    UseCurve = None
    UseSpiralIn = None
    UseSpiralOut = None
    pass

class SettingsCmdCreateAlignmentLayout.SettingsCmdCurveTessellationOption(object):
    """
    Settings of curve tessellation option for the command CreateAlignmentLayout.
    """
    MidOrdinateTolerance = None
    TessellateCurve = None
    pass

class SettingsCmdCreateAlignmentLayout.SettingsCmdRegressionGraphOption(object):
    """
    Settings of tegression graph option for the command CreateAlignmentLayout.
    """
    SplineFitForRegressionAnalysisGraph = None
    pass

class SettingsCmdCreateAlignmentReference(SettingsAmbient):
    """
    Settings for CreateAlignmentReference command.
    """

    pass

class SettingsCmdCreateArcByBestFit(SettingsAmbient):
    """
    Settings for CreateArcByBestFit command.
    """
    CurveTessellationOption = None
    RegressionGraphOption = None
    pass

class SettingsCmdCreateArcByBestFit.SettingsCmdCurveTessellationOption(object):
    """
    Use these settings to specify the default behavior when curve entities are used as an input option for best fit arc creation.
    """
    MidOrdinateTolerance = None
    TessellateCurve = None
    pass

class SettingsCmdCreateArcByBestFit.SettingsCmdRegressionGraphOption(object):
    """
    Use this setting to specify the default behavior for regression analysis graphs in best fit arc creation.
    """
    SplineFitForRegressionAnalysisGraph = None
    pass

class SettingsCmdCreateAssembly(SettingsAmbient):
    """
    Settings for CreateAssembly command.
    """

    pass

class SettingsCmdCreateAssemblyTool(SettingsAmbient):
    """
    Settings for CreateAssemblyTool command.
    """

    pass

class SettingsCmdCreateCantView(SettingsAmbient):
    """
    Settings for the CreateCantView command.
    """

    pass

class SettingsCmdCreateCatchmentFromObject(SettingsAmbient):
    """
    Settings for CreateCatchmentFromObject command.
    """
    Catchment = None
    ChannelFlow = None
    HydrologicalProperties = None
    ShallowConcentratedFlow = None
    SheetFlow = None
    TimeOfConcentrationMethod = None
    pass

class SettingsCmdCreateCatchmentFromObject.SettingsCmdCatchment(object):
    """
    Settings for catchment properties.
    """
    Style = None
    pass

class SettingsCmdCreateCatchmentFromObject.SettingsCmdChannelFlow(object):
    """
    Settings for channel flow.
    """
    CrossSectionalArea = None
    Length = None
    ManningCoefficient = None
    Segments = None
    WetPerimeter = None
    pass

class SettingsCmdCreateCatchmentFromObject.SettingsCmdHydrologicalProperties(object):
    """
    Settings for hydrological properties.
    """

    pass

class SettingsCmdCreateCatchmentFromObject.SettingsCmdShallowConcentratedFlow(object):
    """
    Settings for shallow concentrated flow.
    """
    Length = None
    Segments = None
    SurfaceType = None
    pass

class SettingsCmdCreateCatchmentFromObject.SettingsCmdSheetFlow(object):
    """
    Settings for sheet flow.
    """
    Length = None
    ManningCoefficient = None
    RainIntensity = None
    Segments = None
    pass

class SettingsCmdCreateCatchmentFromSurface(SettingsAmbient):
    """
    Settings for CreateCatchmentFromObject command.
    """
    Catchment = None
    ChannelFlow = None
    HydrologicalProperties = None
    ShallowConcentratedFlow = None
    SheetFlow = None
    TimeOfConcentrationMethod = None
    pass

class SettingsCmdCreateCatchmentFromSurface.SettingsCmdCatchment(object):
    """
    Settings for catchment properties.
    """
    Style = None
    pass

class SettingsCmdCreateCatchmentFromSurface.SettingsCmdChannelFlow(object):
    """
    Settings for channel flow.
    """
    CrossSectionalArea = None
    Length = None
    ManningCoefficient = None
    Segments = None
    WetPerimeter = None
    pass

class SettingsCmdCreateCatchmentFromSurface.SettingsCmdHydrologicalProperties(object):
    """
    Settings for hydrological properties.
    """

    pass

class SettingsCmdCreateCatchmentFromSurface.SettingsCmdShallowConcentratedFlow(object):
    """
    Settings for shallow concentrated flow.
    """
    Length = None
    Segments = None
    SurfaceType = None
    pass

class SettingsCmdCreateCatchmentFromSurface.SettingsCmdSheetFlow(object):
    """
    Settings for sheet flow.
    """
    Length = None
    ManningCoefficient = None
    RainIntensity = None
    Segments = None
    pass

class SettingsCmdCreateCatchmentGroup(SettingsAmbient):
    """
    Settings for CreateCatchmentGroup command.
    """

    pass

class SettingsCmdCreateCorridor(SettingsAmbient):
    """
    Settings for CreateCorridor command.
    """
    AssemblyInsertion = None
    pass

class SettingsCmdCreateCorridor.SettingsCmdAssemblyInsertion(object):
    """
    Settings for alignment type option.
    """
    CorridorAlongCurvesOption = None
    CorridorAlongOffsetTargetCurvesOption = None
    CorridorRegionLockMode = None
    FrequencyAlongCurves = None
    FrequencyAlongOffsetTargetCurves = None
    FrequencyAlongProfileCurves = None
    FrequencyAlongSpirals = None
    FrequencyAlongTangents = None
    HorizontalGeometryPoints = None
    MODAlongCurves = None
    MODAlongOffsetTargetCurves = None
    OffsetTargetGeometryPoints = None
    OffsetTargetStartEnd = None
    ProfileGeometryPoints = None
    ProfileHighLowPoints = None
    SuperelevationCriticalPoints = None
    pass

class SettingsCmdCreateFeatureLineFromAlign(SettingsAmbient):
    """
    Settings for CreateFeatureLineFromAlign command.
    """
    FeatureLineCreation = None
    pass

class SettingsCmdCreateFeatureLineFromAlign.SettingsCmdFeatureLineCreation(object):
    """
    Settings that specify the default behavior for creating feature lines from alignments.
    """
    CreateDynamicLink = None
    LayerSetting = None
    MidOrdinateDistance = None
    SpiralTessellationFactor = None
    UseFeatureLineName = None
    UseFeatureLineStyle = None
    WeedPoints = None
    pass

class SettingsCmdCreateFeatureLines(SettingsAmbient):
    """
    Settings for CreateFeatureLines command.
    """
    FeatureLineCreation = None
    pass

class SettingsCmdCreateFeatureLines.SettingsCmdFeatureLineCreation(object):
    """
    Settings that specify the default behavior for creating feature lines from objects.
    """
    AssignElevations = None
    ElevationSource = None
    EraseExistingEntities = None
    IncludeMidElevationBreaks = None
    LayerSetting = None
    UseFeatureLineName = None
    UseFeatureLineStyle = None
    WeedPoints = None
    pass

class SettingsCmdCreateFlowSegment(SettingsAmbient):
    """
    Settings for CreateFlowSegment command.
    """
    ChannelFlow = None
    ShallowConcentratedFlow = None
    SheetFlow = None
    pass

class SettingsCmdCreateFlowSegment.SettingsCmdChannelFlow(object):
    """
    Settings for channel flow.
    """
    CrossSectionalArea = None
    WetPerimeter = None
    pass

class SettingsCmdCreateFlowSegment.SettingsCmdShallowConcentratedFlow(object):
    """
    Settings for shallow concentrated flow.
    """
    SurfaceType = None
    pass

class SettingsCmdCreateFlowSegment.SettingsCmdSheetFlow(object):
    """
    Settings for sheet flow.
    """
    RainIntensity = None
    pass

class SettingsCmdCreateGrading(SettingsAmbient):
    """
    Settings for CreateGrading command.
    """
    GradingCreation = None
    pass

class SettingsCmdCreateGrading.SettingsCmdGradingCreation(object):
    """
    Settings that specify the default behavior for creating grading.
    """
    TransitionRegionLength = None
    pass

class SettingsCmdCreateGradingGroup(SettingsAmbient):
    """
    Settings for CreateGradingGroup command.
    """
    GradingGroupCreation = None
    pass

class SettingsCmdCreateGradingGroup.SettingsCmdGradingGroupCreation(object):
    """
    Settings that specify the default behavior for creating grading.
    """
    GradingSurfaceCreation = None
    SurfaceConeTessellationAngle = None
    SurfaceStyle = None
    SurfaceStyleId = None
    SurfaceTessellationIncrement = None
    UseGroupName = None
    pass

class SettingsCmdCreateInterferenceCheck(SettingsAmbient):
    """
    Settings for CreateInterferenceCheck command.
    """
    InterferenceCriteria = None
    pass

class SettingsCmdCreateInterferenceCheck.SettingsCmdInterferenceCriteria(object):
    """
    Settings for interference criteria.
    """
    Apply3DProximityCheck = None
    Distance = None
    ScaleFactor = None
    UseDistanceOrScaleFactor = None
    pass

class SettingsCmdCreateIntersection(SettingsAmbient):
    """
    Settings for CreateIntersection command.
    """
    AssemblyInsertion = None
    CrossSlopes = None
    CurbReturnParameters = None
    CurbReturnProfileRules = None
    IntersectionOptions = None
    Offsets = None
    SecondaryRoadProfileRules = None
    WideningParameters = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdAssemblyInsertion(object):
    """
    Settings for the default assembly insertion of new intersection
    """
    CorridorRegionLockMode = None
    FrequencyAlongCurves = None
    FrequencyAlongProfileCurves = None
    FrequencyAlongSpirals = None
    FrequencyAlongTangents = None
    HorizontalGeometryPoints = None
    ProfileGeometryPoints = None
    ProfileHighLowPoints = None
    SuperelevationCriticalPoints = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdCrossSlopes(object):
    """
    Settings for the default cross slopes of new intersection
    """
    PrimaryRoadLeftCrossSlope = None
    PrimaryRoadRightCrossSlope = None
    SecondaryRoadLeftCrossSlope = None
    SecondaryRoadRightCrossSlope = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdCurbReturnParameters(object):
    """
    Settings for the default curb return parameters of new intersection
    """
    ChamferFilletLengthAlongIncomingLane = None
    ChamferFilletLengthAlongOutgoingLane = None
    CircularFilletRadius = None
    CurbReturnType = None
    LengthOfCurve1 = None
    LengthOfCurve3 = None
    RadiusOfCurve1 = None
    RadiusOfCurve2 = None
    RadiusOfCurve3 = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdCurbReturnProfileRules(object):
    """
    Settings for the default curb return profile rules of new intersection
    """
    DefineCurbReturnProfileBy = None
    ExtendProfileAlongIncomingLane = None
    ExtendProfileAlongOutgoingLane = None
    LengthToExtendAlongIncomingLane = None
    LengthToExtendAlongOutgoingLane = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdIntersectionOptions(object):
    """
    Settings for the default intersection options of new intersection
    """
    CreateCurbReturnAlignments = None
    CreateCurbReturnProfiles = None
    CreateIntersectionCorridors = None
    IntersectionType = None
    PrimaryRoadDefaultExitAndEntryLength = None
    SecondaryRoadDefaultExitAndEntryLength = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdOffsets(object):
    """
    Settings for the default offsets of new intersection
    """
    OffsetLengthOptions = None
    PrimaryRoadLeftOffset = None
    PrimaryRoadRightOffset = None
    SecondaryRoadLeftOffset = None
    SecondaryRoadRightOffset = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdSecondaryRoadProfileRules(object):
    """
    Settings for the default secondary road profile rules of new intersection
    """
    ApplyGradeRules = None
    DistanceRuleToAdjusttheGrade = None
    DistanceValue = None
    MaximumGrade = None
    MaximumGradeChange = None
    pass

class SettingsCmdCreateIntersection.SettingsCmdWideningParameters(object):
    """
    Settings for the default widening parameters of new intersection
    """
    LinearTransitionType = None
    RadiusofCurve1 = None
    RadiusofCurve2 = None
    RadiusOfReverseCurve = None
    TaperRation = None
    TransitionLength = None
    TransitionType = None
    WidenedOffset = None
    WideningAtIncomingLane = None
    WideningAtOutgoingLane = None
    WideningSegmentLength = None
    pass

class SettingsCmdCreateLineByBestFit(SettingsAmbient):
    """
    Settings for CreateLineByBestFit command.
    """
    CurveTessellationOption = None
    RegressionGraphOption = None
    pass

class SettingsCmdCreateLineByBestFit.SettingsCmdCurveTessellationOption(object):
    """
    Use these settings to specify the default behavior when curve entities are used as an input option for best fit line creation.
    """
    MidOrdinateTolerance = None
    TessellateCurve = None
    pass

class SettingsCmdCreateLineByBestFit.SettingsCmdRegressionGraphOption(object):
    """
    Use this setting to specify the default behavior for regression analysis graphs in best fit line creation.
    """
    SplineFitForRegressionAnalysisGraph = None
    pass

class SettingsCmdCreateMassHaulDiagram(SettingsAmbient):
    """
    Settings for CreateMassHallDiagram command.
    """
    MassHaulCreation = None
    pass

class SettingsCmdCreateMassHaulDiagram.SettingsCmdMassHaulCreation(object):
    """
    Settings for the table creation.
    """
    BorrowPitCapacity = None
    DumpSiteCapacity = None
    FreeHaulDistance = None
    pass

class SettingsCmdCreateMultipleProfileView(SettingsAmbient):
    """
    Settings for CreateMultipleProfileView command.
    """
    MultipleProfileViewCreation = None
    pass

class SettingsCmdCreateMultipleProfileView.SettingsCmdMultipleProfileViewCreation(object):
    """
    Settings that specify defaults for creating multiple profile views.
    """
    ColumnSpacing = None
    DefaultProfileViewHeight = None
    DefaultProfileViewLength = None
    PlotPattern = None
    ProfileViewDatumBy = None
    ProfileViewsInRowOrColumn = None
    RowSpacing = None
    StartCorner = None
    pass

class SettingsCmdCreateMultipleSectionView(SettingsAmbient):
    """
    Settings for CreateMultipleSectionView command.
    """
    MultipleSectionViewCreation = None
    TableCreation = None
    pass

class SettingsCmdCreateMultipleSectionView.SettingsCmdMultipleSectionViewCreation(object):
    """
    Settings for the table creation.
    """
    PlacementOption = None
    SectionViewHeight = None
    SpecifyMultipleSectionViewStationRange = None
    pass

class SettingsCmdCreateMultipleSectionView.SettingsCmdTableCreation(object):
    """
    Settings for table creation.
    """
    MaterialVolumeTableStyle = None
    MaterialVolumeTableStyleId = None
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SectionViewAnchor = None
    SplitTable = None
    TableAnchor = None
    TableLayout = None
    TableSpacing = None
    TileDirection = None
    TotalVolumeTableStyle = None
    TotalVolumeTableStyleId = None
    XOffset = None
    YOffset = None
    pass

class SettingsCmdCreateNetwork(SettingsAmbient):
    """
    Settings for CreateNetwork command.
    """
    DefaultLayoutCommand = None
    LabelNewParts = None
    pass

class SettingsCmdCreateNetwork.SettingsCmdLabelNewParts(object):
    """
    Settings for alignment type option.
    """
    CrossPipeProfile = None
    PipeInPlan = None
    PipeProfile = None
    StructureInPlan = None
    StructureProfile = None
    pass

class SettingsCmdCreateNetworkFromObject(SettingsAmbient):
    """
    Settings for CreateNetworkFromObject command.
    """

    pass

class SettingsCmdCreateNetworkPartsList(SettingsAmbient):
    """
    Settings for CreateNetworkPartsList command.
    """

    pass

class SettingsCmdCreateNetworkPartsListFull(SettingsAmbient):
    """
    Settings for CreateNetworkPartsListFull command.
    """

    pass

class SettingsCmdCreateNetworkReference(SettingsAmbient):
    """
    Settings for CreateNetworkReference command.
    """

    pass

class SettingsCmdCreateOffsetAlignment(SettingsAmbient):
    """
    Settings for CreateOffsetAlignment command.
    """
    OffsetAlignmentOptions = None
    pass

class SettingsCmdCreateOffsetAlignment.SettingsCmdOffsetAlignmentOptions(object):
    """
    Settings for the offset alignment options.
    """
    FromParentAlignmentStart = None
    IncrementalOffsetValueLeftSide = None
    IncrementalOffsetValueRightSide = None
    NumberOfOffsetsLeftSide = None
    NumberOfOffsetsRightSide = None
    ToParentAlignmentEnd = None
    pass

class SettingsCmdCreateParabolaByBestFit(SettingsAmbient):
    """
    Settings for CreateParabolaByBestFit command.
    """
    CurveTessellationOption = None
    RegressionGraphOption = None
    pass

class SettingsCmdCreateParabolaByBestFit.SettingsCmdCurveTessellationOption(object):
    """
    Use these settings to specify the default behavior when curve entities are used as an input option for best fit parabola creation.
    """
    MidOrdinateTolerance = None
    TessellateCurve = None
    pass

class SettingsCmdCreateParabolaByBestFit.SettingsCmdRegressionGraphOption(object):
    """
    Use this setting to specify the default behavior for regression analysis graphs in best fit parabola creation.
    """
    SplineFitForRegressionAnalysisGraph = None
    pass

class SettingsCmdCreateParcelByLayout(SettingsAmbient):
    """
    Settings for CreateParcelByLayout command.
    """
    AutomaticLayout = None
    ConvertFromEntities = None
    ParcelSizing = None
    PreviewGraphics = None
    pass

class SettingsCmdCreateParcelByLayout.SettingsCmdAutomaticLayout(object):
    """
    Settings that specify defaults for automatic parcel layout.
    """
    AutomaticMode = None
    RemainderDistributionType = None
    pass

class SettingsCmdCreateParcelByLayout.SettingsCmdConvertFromEntities(object):
    """
    Settings that specify defaults for creation of parcels.
    """
    AutoAddSegmentLabel = None
    pass

class SettingsCmdCreateParcelByLayout.SettingsCmdParcelSizing(object):
    """
    Settings that specify defaults for sizing parcels.
    """
    FrontageOffset = None
    MaximumDepth = None
    MinimumArea = None
    MinimumDepth = None
    MinimumFrontage = None
    MinimumWidth = None
    SelectionMethod = None
    SolutionPreference = None
    UseMaximumDepth = None
    UseMinimumFrontageAtOffset = None
    pass

class SettingsCmdCreateParcelByLayout.SettingsCmdPreviewGraphics(object):
    """
    Settings that specify defaults for temporary parcel layout preview graphics.
    """
    FrontageColor = None
    FrontageOffsetColor = None
    MinimumDepthColor = None
    MinimumFrontageColor = None
    MinimumWidthColor = None
    NewParcelColor = None
    pass

class SettingsCmdCreateParcelFromObjects(SettingsAmbient):
    """
    Settings for CreateParcelFromObjects command.
    """
    ConvertFromEntities = None
    pass

class SettingsCmdCreateParcelFromObjects.SettingsCmdConvertFromEntities(object):
    """
    Settings that specify defaults for creation of parcels.
    """
    AutoAddSegmentLabels = None
    EraseAllExistingEntities = None
    pass

class SettingsCmdCreateParcelROW(SettingsAmbient):
    """
    Settings for CreateParcelROW command.
    """
    CleanupAtAlignmentIntersections = None
    CleanupAtParcelBoundaries = None
    CreateParcelRightOfWay = None
    pass

class SettingsCmdCreateParcelROW.SettingsCmdCleanupAtAlignmentIntersections(object):
    """
    Settings that specify default offset for cleanup at alignment intersections.
    """
    CleanupMethodFillet = None
    FilletRadiusAtAlignmentIntersections = None
    pass

class SettingsCmdCreateParcelROW.SettingsCmdCleanupAtParcelBoundaries(object):
    """
    Settings that specify default offset for cleanup at parcel boundaries.
    """
    CleanupMethodFillet = None
    FilletRadiusAtParcelBoundaryIntersections = None
    pass

class SettingsCmdCreateParcelROW.SettingsCmdCreateParcelRightOfWay(object):
    """
    Setting that specify default offset for creation of parcel rights of way.
    """
    OffsetFromAlignment = None
    pass

class SettingsCmdCreatePointCloud(SettingsAmbient):
    """
    Settings for CreatePointCloud command.
    """
    DefaultLayer = None
    FileFormat = None
    pass

class SettingsCmdCreatePointCloud.SettingsCmdDefaultLayer(object):
    """
    
    """
    LayerName = None
    pass

class SettingsCmdCreatePointGroup(SettingsAmbient):
    """
    Settings for CreatePointGroup command.
    """

    pass

class SettingsCmdCreatePoints(SettingsAmbient):
    """
    Settings for CreatePoints command.
    """
    Layer = None
    PointIdentity = None
    PointsCreation = None
    pass

class SettingsCmdCreatePoints.SettingsCmdLayer(object):
    """
    Default layer settings for the CreatePoints command.
    """
    Layer = None
    pass

class SettingsCmdCreatePoints.SettingsCmdPointIdentity(object):
    """
    Settings that specify defaults for Point Identity.
    """
    AssignPointNamesOption = None
    ForceNames = None
    HandleSuppliedPointNumbersOption = None
    NextPointNumber = None
    PointNumberOffset = None
    ResolveDuplicatePointNamesOption = None
    ResolveDuplicatePointNumbersOption = None
    StartPointNumber = None
    UseSequentialNumbering = None
    pass

class SettingsCmdCreatePoints.SettingsCmdPointsCreation(object):
    """
    Settings that specify defaults for Points Creation.
    """
    DefaultDescription = None
    DefaultElevation = None
    DisableDescriptionKeys = None
    EchoCoordinatesToCommandLine = None
    GeographicCoordinates = None
    GridCoordinates = None
    LocalCoordinates = None
    MatchOnDescriptionParameters = None
    PromptForDescriptions = None
    PromptForElevations = None
    PromptForPointNames = None
    pass

class SettingsCmdCreatePointsFromCorridor(SettingsAmbient):
    """
    Settings for CreatePointsFromCorridor command.
    """

    pass

class SettingsCmdCreatePolylineFromCorridor(SettingsAmbient):
    """
    Settings for CreatePolylineFromCorridor command.
    """

    pass

class SettingsCmdCreatePolylineFromSuper(SettingsAmbient):
    """
    Settings for CreatePolylineFromSuper command.
    """

    pass

class SettingsCmdCreateProfileFromCorridor(SettingsAmbient):
    """
    Settings for CreateProfileFromCorridor command.
    """
    CriteriaBasedDesignOptions = None
    pass

class SettingsCmdCreateProfileFromCorridor.SettingsCmdCriteriaBasedDesignOptions(object):
    """
    Settings that specify the defaults used when creating a profile using design criteria.
    """
    DefaultDesignCheckSet = None
    DefaultDesignCheckSetId = None
    UseDesignChecksOption = None
    UseDesignCriteriaFileOption = None
    pass

class SettingsCmdCreateProfileFromFile(SettingsAmbient):
    """
    Settings for CreateProfileFromFile command.
    """

    pass

class SettingsCmdCreateProfileFromSurface(SettingsAmbient):
    """
    Settings for CreateProfileFromSurface command.
    """
    Geometry = None
    pass

class SettingsCmdCreateProfileFromSurface.SettingsCmdGeometry(object):
    """
    Settings that specify the geometry setting.
    """
    ProfileSampleOffsetsCommandSetting = None
    pass

class SettingsCmdCreateProfileLayout(SettingsAmbient):
    """
    Settings for CreateProfileLayout command.
    """
    CurveTessellationOption = None
    RegressionGraphOption = None
    pass

class SettingsCmdCreateProfileLayout.SettingsCmdCurveTessellationOption(object):
    """
    Settings that specify the default behavior when curve entities are used as an input option for best fit arc, line, and parabola creation.
    """
    MidOrdinateTolerance = None
    TessellateCurve = None
    pass

class SettingsCmdCreateProfileLayout.SettingsCmdRegressionGraphOption(object):
    """
    Setting that specifies the default behavior for regression analysis graphs in best fit arc, line, and parabola creation.
    """
    SplineFitForRegressionAnalysisGraph = None
    pass

class SettingsCmdCreateProfileReference(SettingsAmbient):
    """
    Settings for CreateProfileReference command.
    """

    pass

class SettingsCmdCreateProfileView(SettingsAmbient):
    """
    Settings for CreateProfileView command.
    """

    pass

class SettingsCmdCreateQuickProfile(SettingsAmbient):
    """
    Settings for CreateQuickProfile command.
    """
    QuickProfile = None
    pass

class SettingsCmdCreateQuickProfile.SettingsCmdQuickProfile(object):
    """
    Settings that specify the default settings for quick profile creation.
    """
    Draw3DEntityProfile = None
    SelectAllSurfaces = None
    pass

class SettingsCmdCreateSampleLines(SettingsAmbient):
    """
    Settings for CreateSampleLines command.
    """
    AdditionalSampleControls = None
    Miscellaneous = None
    SamplingIncrements = None
    SwathWidths = None
    pass

class SettingsCmdCreateSampleLines.SettingsCmdAdditionalSampleControls(object):
    """
    Settings that specify the default behavior for additional sample controls.
    """
    AtHorizontalGeometryPoints = None
    AtRangeEnd = None
    AtRangeStart = None
    AtSuperelevationCriticalStations = None
    EndRangeAtAlignmentEnd = None
    StartRangeAtAlignmentStart = None
    pass

class SettingsCmdCreateSampleLines.SettingsCmdMiscellaneous(object):
    """
    Setting that specifies miscellaneous default behavior for sample lines.
    """
    LockTostation = None
    pass

class SettingsCmdCreateSampleLines.SettingsCmdSamplingIncrements(object):
    """
    Settings that specify the default behavior for sampling increments.
    """
    IncrementAlongCurves = None
    IncrementAlongSpirals = None
    IncrementAlongTangents = None
    UseSamplingIncrements = None
    pass

class SettingsCmdCreateSampleLines.SettingsCmdSwathWidths(object):
    """
    Settings that specify the default behavior for sample line swath width.
    """
    LeftSwathWidth = None
    RightSwathWidth = None
    pass

class SettingsCmdCreateSectionSheets(SettingsAmbient):
    """
    Settings for CreateSectionSheets command.
    """
    SheetCreation = None
    pass

class SettingsCmdCreateSectionSheets.SettingsCmdSheetCreation(object):
    """
    Settings for sheet creation.
    """
    SheetSetUse = None
    pass

class SettingsCmdCreateSectionView(SettingsAmbient):
    """
    Settings for CreateSectionView command.
    """
    TableCreation = None
    pass

class SettingsCmdCreateSectionView.SettingsCmdTableCreation(object):
    """
    Settings for the table creation.
    """
    MaterialVolumeTableStyle = None
    MaterialVolumeTableStyleId = None
    MaximumNumberOfRows = None
    MaximumTablesPerStack = None
    SectionViewAnchor = None
    SplitTable = None
    TableAnchor = None
    TableLayout = None
    TableSpacing = None
    TileDirection = None
    TotalVolumeTableStyle = None
    TotalVolumeTableStyleId = None
    XOffset = None
    YOffset = None
    pass

class SettingsCmdCreateSheets(SettingsAmbient):
    """
    Settings for CreateSheets command.
    """
    SheetCreation = None
    pass

class SettingsCmdCreateSheets.SettingsCmdSheetCreation(object):
    """
    Settings for the sheet creation.
    """
    AddNetworkLabels = None
    AddToVault = None
    AlignNorthArrow = None
    AlignProfileAndPlanViewType = None
    ExistingSheetSetName = None
    NorthArrowBlockName = None
    NumberOfLayoutsPerDrawing = None
    SheetCreateMethod = None
    UseExistingSheetSet = None
    pass

class SettingsCmdCreateSimpleCorridor(SettingsAmbient):
    """
    Settings for CreateSimpleCorridor command.
    """
    AssemblyInsertion = None
    pass

class SettingsCmdCreateSimpleCorridor.SettingsCmdAssemblyInsertion(object):
    """
    Settings that establish the defaults assigned to corridor creation.
    """
    CorridorRegionLockMode = None
    FrequencyAlongCurves = None
    FrequencyAlongProfileCurves = None
    FrequencyAlongSpirals = None
    FrequencyAlongTangents = None
    HorizontalGeometryPoints = None
    ProfileGeometryPoints = None
    ProfileHighLowPoints = None
    SuperelevationCriticalPoints = None
    pass

class SettingsCmdCreateSite(SettingsAmbient):
    """
    Settings for CreateSite command.
    """
    Alignment = None
    FeatureLine = None
    Parcel = None
    pass

class SettingsCmdCreateSite.SettingsCmdAlignment(object):
    """
    Settings that specify default increments for alignment tag numbering.
    """
    AlignmentCurveNextAutomaticTagCounter = None
    AlignmentCurveNextManualTagCounter = None
    AlignmentLineNextAutomaticTagCounter = None
    AlignmentLineNextManualTagCounter = None
    AlignmentSpiralNextAutomaticTagCounter = None
    AlignmentSpiralNextManualTagCounter = None
    pass

class SettingsCmdCreateSite.SettingsCmdFeatureLine(object):
    """
    Settings that specify defaults for feature line style priority.
    """
    FeatureLineStyle = None
    pass

class SettingsCmdCreateSite.SettingsCmdParcel(object):
    """
    Settings that specify default increments for parcel numbering.
    """
    ParcelCurveNextAutomaticTagCounter = None
    ParcelCurveNextManualTagCounter = None
    ParcelLineNextAutomaticTagCounter = None
    ParcelLineNextManualTagCounter = None
    ParcelNextAutomaticAreaCounter = None
    ParcelNextManualAreaCounter = None
    pass

class SettingsCmdCreateSubFromPline(SettingsAmbient):
    """
    Settings for CreateSubFromPline command.
    """
    CreateFromEntities = None
    pass

class SettingsCmdCreateSubFromPline.SettingsCmdCreateFromEntities(object):
    """
    Settings that specifies the default behavior for creating subassemblies from polylines.
    """
    LinkCreation = None
    MidOrdinateDistance = None
    pass

class SettingsCmdCreateSubassemblyTool(SettingsAmbient):
    """
    Settings for CreateSubassemblyTool command.
    """
    SubassemblyOptions = None
    pass

class SettingsCmdCreateSubassemblyTool.SettingsCmdSubassemblyOptions(object):
    """
    Settings
    """
    AssemblyGroupName = None
    AssemblyGroupNamePrompt = None
    AutoDetectSide = None
    CurrentSide = None
    SubassemblyName = None
    SubassemblyNamePrompt = None
    pass

class SettingsCmdCreateSuperelevationView(SettingsAmbient):
    """
    Settings for CreateSuperelevationView command.
    """

    pass

class SettingsCmdCreateSurface(SettingsAmbient):
    """
    Settings for CreateSurface command.
    """
    BuildOptions = None
    NameFormat = None
    SurfaceCreation = None
    pass

class SettingsCmdCreateSurface.SettingsCmdBuildOptions(object):
    """
    Settings that specify the build options assigned when creating surfaces.
    """
    AllowCrossingBreaklines = None
    ConvertProximityBreaklinesToStandard = None
    CopyDeletedDependentObjects = None
    ElevationGreaterThan = None
    ElevationLessThan = None
    ElevationToUse = None
    ExcludeElevationsGreaterThan = None
    ExcludeElevationsLessThan = None
    MaximumAngleBetweenAdjacentTINLines = None
    MaximumTriangleLength = None
    UseMaximumAngle = None
    UseMaximumTriangleLength = None
    pass

class SettingsCmdCreateSurface.SettingsCmdSurfaceCreation(object):
    """
    Settings that specify the defaults assigned when creating surfaces.
    """
    CutFactor = None
    DefaultType = None
    FillFactor = None
    GridSurfaceOrientation = None
    GridSurfaceXSpacing = None
    GridSurfaceYSpacing = None
    pass

class SettingsCmdCreateSurface.SettingsNameFormat(object):
    """
    Settings that specify name format for the command.
    """
    Surface = None
    pass

class SettingsCmdCreateSurfaceFromTIN(SettingsAmbient):
    """
    Settings for CreateSurfaceFromTIN command.
    """

    pass

class SettingsCmdCreateSurfaceGridFromDEM(SettingsAmbient):
    """
    Settings for CreateSurfaceGridFromDEM command.
    """
    BuildOptions = None
    ImportOptions = None
    pass

class SettingsCmdCreateSurfaceGridFromDEM.SettingsCmdBuildOptions(object):
    """
    Settings that specify the build options assigned when creating surfaces.
    """
    CopyDeletedDependentObjects = None
    ElevationGreaterThan = None
    ElevationLessThan = None
    ExcludeElevationsGreaterThan = None
    ExcludeElevationsLessThan = None
    pass

class SettingsCmdCreateSurfaceGridFromDEM.SettingsCmdImportOptions(object):
    """
    Settings that specify the defaults assigned when creating surfaces.
    """
    NullElevation = None
    UseCustomNullElevation = None
    pass

class SettingsCmdCreateSurfaceReference(SettingsAmbient):
    """
    Settings for CreateSurfaceReference command.
    """
    NameFormat = None
    pass

class SettingsCmdCreateSurfaceReference.SettingsNameFormat(object):
    """
    Settings that specify name format for the command.
    """
    Surface = None
    pass

class SettingsCmdCreateSurfaceWaterdrop(SettingsAmbient):
    """
    Settings for CreateSurfaceWaterdrop command.
    """
    WaterdropMarker = None
    WaterdropPath = None
    pass

class SettingsCmdCreateSurfaceWaterdrop.SettingsCmdWaterdropMarker(object):
    """
    Settings that specify the default water drop marker options for surfaces.
    """
    PlaceMarkerAtStartPoint = None
    StartPointMarkerStyle = None
    StartPointMarkerStyleId = None
    pass

class SettingsCmdCreateSurfaceWaterdrop.SettingsCmdWaterdropPath(object):
    """
    Settings that specify the default water drop path options for surfaces.
    """
    PathLayer = None
    PathObjectType = None
    pass

class SettingsCmdCreateViewFrames(SettingsAmbient):
    """
    Settings for CreateViewFrames command.
    """
    ViewFrameCreation = None
    pass

class SettingsCmdCreateViewFrames.SettingsCmdViewFrameCreation(object):
    """
    Settings for the view frame creation.
    """
    AlignmentStationRangeSpecifiedByUser = None
    EnableFirstViewFrameOffset = None
    FirstViewFrameOffsetDistance = None
    InsertMatchLines = None
    MatchLineRepositioning = None
    MatchLineRepositioningValue = None
    MatchLineSnapStation = None
    MatchLineSnapStationValue = None
    SheetType = None
    ViewFrameOrientation = None
    pass

class SettingsCmdDrawFeatureLine(SettingsAmbient):
    """
    Settings for DrawFeatureLine command.
    """
    FeatureLineCreation = None
    pass

class SettingsCmdDrawFeatureLine.SettingsCmdFeatureLineCreation(object):
    """
    Settings that specify the default behavior for creating featureline.
    """
    LayerSetting = None
    UseFeatureLineName = None
    UseFeatureLineStyle = None
    pass

class SettingsCmdEditFlowSegments(SettingsAmbient):
    """
    Settings for EditFlowSegment command.
    """
    ChannelFlow = None
    ShallowConcentratedFlow = None
    SheetFlow = None
    pass

class SettingsCmdEditFlowSegments.SettingsCmdChannelFlow(object):
    """
    Settings for channel flow.
    """
    CrossSectionalArea = None
    WetPerimeter = None
    pass

class SettingsCmdEditFlowSegments.SettingsCmdShallowConcentratedFlow(object):
    """
    Settings for shallow concentrated flow.
    """
    SurfaceType = None
    pass

class SettingsCmdEditFlowSegments.SettingsCmdSheetFlow(object):
    """
    Settings for sheet flow.
    """
    RainIntensity = None
    pass

class SettingsCmdEditInStormSewers(SettingsAmbient):
    """
    Settings for EditInStormSewers command.
    """

    pass

class SettingsCmdEditSVGroupStyle(SettingsAmbient):
    """
    Settings for EditSVGroupStyle command.
    """

    pass

class SettingsCmdExportParcelAnalysis(SettingsAmbient):
    """
    Settings for ExportParcelAnalysis command.
    """
    ParcelAnalysis = None
    pass

class SettingsCmdExportParcelAnalysis.SettingsCmdParcelAnalysis(object):
    """
    Settings that specify defaults for parcel analysis.
    """
    AnalysisType = None
    EnableMapcheckAcrossChord = None
    ProcessCounterClockwise = None
    pass

class SettingsCmdExportStormSewerData(SettingsAmbient):
    """
    Settings for ExportStormSewerData command.
    """

    pass

class SettingsCmdFeatureLinesFromCorridor(SettingsAmbient):
    """
    Settings for FeatureLinesFromCorridor command.
    """
    FeatureLineCreation = None
    pass

class SettingsCmdFeatureLinesFromCorridor.SettingsCmdFeatureLineCreation(object):
    """
    Default settings for the Feature Line Creation command.
    """
    CreateDynamicLink = None
    FeatureLineName = None
    HorizontalDeviation = None
    InclusionDistance = None
    LayerSetting = None
    SmoothTheFeatureLine = None
    UseFeatureLineStyle = None
    WeedingDistance = None
    pass

class SettingsCmdFitCurveFeature(SettingsAmbient):
    """
    Settings for FitCurveFeature command.
    """
    FeatureLineFitCurve = None
    pass

class SettingsCmdFitCurveFeature.SettingsCmdFeatureLineFitCurve(object):
    """
    Settings that specify the default behavior for feature line fit curve.
    """
    MinimumNumberOfSegments = None
    Tolerance = None
    pass

class SettingsCmdGenerateQuantitiesReport(SettingsAmbient):
    """
    Settings for GenerateQuantitiesReport command.
    """
    DisplayXmlReport = None
    pass

class SettingsCmdGradingElevEditor(SettingsAmbient):
    """
    Settings for GradingElevEditor command.
    """
    GradingElevationEditor = None
    pass

class SettingsCmdGradingElevEditor.SettingsCmdGradingElevationEditor(object):
    """
    Settings that specify the default behavior for grading elevation editor.
    """
    RaiseLowerIncrement = None
    ShowGradeBreaksOnly = None
    pass

class SettingsCmdGradingTools(SettingsAmbient):
    """
    Settings for GradingTools command.
    """
    GradingLayoutTools = None
    pass

class SettingsCmdGradingTools.SettingsCmdGradingLayoutTools(object):
    """
    Settings that specify the default behavior for grading layout tools.
    """
    Criteria = None
    CriteriaId = None
    GradingCriteriaSet = None
    GradingCriteriaSetId = None
    pass

class SettingsCmdGradingVolumeTools(SettingsAmbient):
    """
    Settings for GradingVolumeTools command.
    """
    LimitFeatureSelectionToCurrentGroup = None
    RaiseLowerElevationIncrement = None
    pass

class SettingsCmdImportBuildingSite(SettingsAmbient):
    """
    Settings for ImportBuildingSite command.
    """

    pass

class SettingsCmdImportGISData(SettingsAmbient):
    """
    Settings for ImportGISData command.
    """
    PipeNetwork = None
    pass

class SettingsCmdImportGISData.SettingsCmdPipeNetwork(object):
    """
    Enapsulates settings used to specify the default behavior for a PipeNetwork.
    """
    NetworkNameTemplate = None
    PartsList = None
    PartsListId = None
    PipeLabelStyle = None
    PipeLabelStyleId = None
    PipeNameTemplate = None
    SnappingTolerance = None
    StructureLabelStyle = None
    StructureLabelStyleId = None
    StructureNameTemplate = None
    pass

class SettingsCmdImportStormSewerData(SettingsAmbient):
    """
    Settings for ImportStormSewerData command.
    """

    pass

class SettingsCmdJoinFeatures(SettingsAmbient):
    """
    Settings for JoinFeatures command.
    """
    FeatureLineJoin = None
    pass

class SettingsCmdJoinFeatures.SettingsCmdFeatureLineJoin(object):
    """
    Settings that specify the default behavior for featureline join.
    """
    Tolerance = None
    pass

class SettingsCmdLayoutSectionViewGroup(SettingsAmbient):
    """
    Settings for LayoutSectionViewGroup command.
    """

    pass

class SettingsCmdMapCheck(SettingsAmbient):
    """
    Settings for MapCheck command.
    """
    Mapcheck = None
    pass

class SettingsCmdMapCheck.SettingsCmdMapcheck(object):
    """
    Use these settings to specify the default behavior for Mapcheck.
    """
    CurrentMapcheckColor = None
    CurrentPointofBeginningColor = None
    CurrentSideColor = None
    DefaultAngleType = None
    DefaultCurveDirection = None
    DefaultCurveTraverseMethod = None
    DefaultSideType = None
    MapcheckColor = None
    UseCommandLineInput = None
    pass

class SettingsCmdMinimizeSurfaceFlatAreas(SettingsAmbient):
    """
    Settings for MinimizeSurfaceFlatAreas command.
    """
    AddPointsToFlatEdges = None
    AddPointsToFlatTriangles = None
    FillGapsInContour = None
    SwapEdges = None
    pass

class SettingsCmdMoveBlocksToSurface(SettingsAmbient):
    """
    Settings for MoveBlocksToSurface command.
    """

    pass

class SettingsCmdMoveBlockstoAttribElev(SettingsAmbient):
    """
    Settings for MoveBlockstoAttribElev command.
    """

    pass

class SettingsCmdMoveTextToElevation(SettingsAmbient):
    """
    Settings for MoveTextToElevation command.
    """

    pass

class SettingsCmdProjectObjectsToMultiSect(SettingsAmbient):
    """
    Settings for ProjectObjectsToMultiSect command.
    """
    ObjectSelectionOptions = None
    pass

class SettingsCmdProjectObjectsToMultiSect.SettingsCmdObjectSelectionOptions(object):
    """
    Settings for Object Selection Options.
    """
    DistanceAfterCurrentSampleLine = None
    DistanceBeforeCurrentSampleLine = None
    PercentageAfterCurrentSampleLine = None
    PercentageBeforeCurrentSampleLine = None
    ProjecitonRuleType = None
    pass

class SettingsCmdProjectObjectsToProf(SettingsAmbient):
    """
    Settings for ProjectObjectsToProf command.
    """

    pass

class SettingsCmdProjectObjectsToSect(SettingsAmbient):
    """
    Settings for ProjectObjectsToSect command.
    """

    pass

class SettingsCmdReAddParcelAreaLabel(SettingsAmbient):
    """
    Settings for ReAddParcelAreaLabel command.
    """

    pass

class SettingsCmdReAddParcelSegmentLabels(SettingsAmbient):
    """
    Settings for ReAddParcelSegmentLabels command.
    """

    pass

class SettingsCmdRenamePipeNetworkParts(SettingsAmbient):
    """
    Settings for RenamePipeNetworkParts command.
    """

    pass

class SettingsCmdResetAnchorPipe(SettingsAmbient):
    """
    Settings for ResetAnchorPipe command.
    """

    pass

class SettingsCmdReverseAlignmentDirection(SettingsAmbient):
    """
    Settings for ReverseAlignmentDirection command.
    """

    pass

class SettingsCmdShowGeodeticCalculator(SettingsAmbient):
    """
    Settings for ShowGeodeticCalculator command.
    """

    pass

class SettingsCmdShowPointGroupProperties(SettingsAmbient):
    """
    Settings for ShowPointGroupProperties command.
    """

    pass

class SettingsCmdShowSpanningPipes(SettingsAmbient):
    """
    Settings for ShowSpanningPipes command.
    """

    pass

class SettingsCmdSimplifySurface(SettingsAmbient):
    """
    Settings for SimplifySurface command.
    """
    MaximumChangeInElevation = None
    PercentageOfPointsToRemove = None
    RegionOptions = None
    SimplifyMethod = None
    UseMaximumChangeInElevation = None
    UsePercentageOfPointsToRemove = None
    pass

class SettingsCmdSuperimposeProfile(SettingsAmbient):
    """
    Settings for SuperimposeProfile command.
    """
    SuperimposeProfile = None
    pass

class SettingsCmdSuperimposeProfile.SettingsCmdSuperimposeProfileOption(object):
    """
    Settings that specify the default values for the mid-ordinate distances that the system uses when tessellating (approximating) the shape of curves in superimposed profiles.
    """
    HorizontalMidOrdinateDistance = None
    VerticalMidOrdinateDistance = None
    pass

class SettingsCmdSurfaceExportToDem(SettingsAmbient):
    """
    Settings for SurfaceExportToDem command.
    """
    ExportOptions = None
    pass

class SettingsCmdSurfaceExportToDem.SettingsCmdExportOptions(object):
    """
    Settings that specify the defaults assigned when exporting surfaces to a DEM file.
    """
    GridSpacing = None
    NullElevation = None
    UseCustomNullElevation = None
    pass

class SettingsCmdSurfaceExtractObjects(SettingsAmbient):
    """
    Settings for SurfaceExtractObjects command.
    """

    pass

class SettingsCmdTakeOff(SettingsAmbient):
    """
    Settings for TakeOff command.
    """
    ComputeTakeOffOption = None
    pass

class SettingsCmdTakeOff.SettingsCmdComputeTakeOff(object):
    """
    Settings of take off computation for command TakeOff.
    """
    DefaultReportStyle = None
    DrawingBasedReportTableFont = None
    IncludeFormulasInReports = None
    LengthComputeType = None
    LimitToAlignmentStation = None
    PipeLengthType = None
    ReportExtentsType = None
    ReportSelectedPayItemOnly = None
    ReportType = None
    pass

class SettingsCmdViewEditCorridorSection(SettingsAmbient):
    """
    Settings for ViewEditCorridorSection command.
    """
    GridSettings = None
    GridTextSettings = None
    SectionSliderInMultipleViewports = None
    ViewEditOptions = None
    pass

class SettingsCmdViewEditCorridorSection.SettingsCmdGridSettings(object):
    """
    Settings for the Grid Settings section of the ViewEditCorridorSection command.
    """
    CenterAxisColor = None
    DisplayCenterAxis = None
    DisplayHorizontalGrid = None
    DisplayVerticalGrid = None
    GridColor = None
    HorizontalGridInterval = None
    VerticalGridInterval = None
    pass

class SettingsCmdViewEditCorridorSection.SettingsCmdGridTextSettings(object):
    """
    Settings for the Grid Text Settings section of the ViewEditCorridorSection command.
    """
    AnnotateCenterAxis = None
    TextColor = None
    TextHeightRelativeToScreen = None
    TextStyle = None
    pass

class SettingsCmdViewEditCorridorSection.SettingsCmdSectionSliderInMultipleViewports(object):
    """
    Settings for section slider in multiple viewports of the ViewEditCorridorSection command.
    """
    AlignmentSliderColor = None
    NeedSlider = None
    ProfileViewSliderColor = None
    pass

class SettingsCmdViewEditCorridorSection.SettingsCmdViewEditOptions(object):
    """
    Settings for the View/Edit Options section of the ViewEditCorridorSection command.
    """
    ApplyViewportConfiguration = None
    BackClip = None
    DefaultViewScale = None
    FrontClip = None
    RebuildOnEdit = None
    StationTrackerInMultipleViewports = None
    TurnOffUnassociatedLayers = None
    UndefinedSectionWidth = None
    pass

class SettingsCmdVolumesDashboard(SettingsAmbient):
    """
    Settings for VolumesDashboard command.
    """
    BoundedVolumeCreation = None
    BuildOptions = None
    DynamicHighlightOptions = None
    VolumeSurfaceCreation = None
    pass

class SettingsCmdVolumesDashboard.SettingsCmdBoundedVolumeCreation(object):
    """
    Settings that specify the defaults assigned when create bounded volume surfaces.
    """
    MidOrdinateDistance = None
    pass

class SettingsCmdVolumesDashboard.SettingsCmdBuildOptions(object):
    """
    Settings that specifies the defaults of build options.
    """
    AllowCrossingBreaklines = None
    ConvertProximityBreaklinesToStandard = None
    CopyDeletedDependentObjects = None
    ElevationGreaterThan = None
    ElevationLessThan = None
    ElevationToUse = None
    ExcludeElevationsGreaterThan = None
    ExcludeElevationsLessThan = None
    MaximumTriangleLength = None
    UseMaximumTriangleSideLength = None
    pass

class SettingsCmdVolumesDashboard.SettingsCmdDynamicHighlightOptions(object):
    """
    Settings that specifies the defaults of dynamic highlight options.
    """
    BoundaryPolygonColor = None
    BoundaryPolygonlineweight = None
    SurfaceBorderColor = None
    SurfaceBorderLineweight = None
    pass

class SettingsCmdVolumesDashboard.SettingsCmdVolumeSurfaceCreation(object):
    """
    Settings that specify the defaults assigned when create volume surfaces.
    """
    CutFactor = None
    DefaultType = None
    FillFactor = None
    GridSurfaceOrientation = None
    GridSurfaceXSpacing = None
    GridSurfaceYSpacing = None
    VolumeSurfaceNameTemplate = None
    pass

class SettingsCmdWeedFeatures(SettingsAmbient):
    """
    Settings for WeedFeatures command.
    """
    FeatureLineWeed = None
    pass

class SettingsCmdWeedFeatures.SettingsCmdFeatureLineWeed(object):
    """
    Settings that specify the default behavior for grading layout tools.
    """
    AngleFactor = None
    ApplyAngleFactor = None
    ApplyGradeFactor = None
    ApplyLengthFactor = None
    ClosePoint3DDistance = None
    ClosePointRemoval = None
    GradeFactor = None
    LengthFactor = None
    pass

class SettingsCoordinateSystem(object):
    """
    Encapsulates coordinate system settings.
    """
    Category = None
    Code = None
    Datum = None
    Description = None
    Projection = None
    Unit = None
    pass

class SettingsCorridor(SettingsAmbient):
    """
    Controls ambient settings for corridors.
    """
    NameFormat = None
    RegionHighlightGraphics = None
    Styles = None
    pass

class SettingsCorridor.SettingsNameFormat(object):
    """
    Settings to specify the default name formats for corridors and 
    corridor surfaces, as well as for alignments and profiles from feature lines.
    """
    AlignmentFromFeatureLine = None
    Corridor = None
    CorridorBaseline = None
    CorridorRegion = None
    CorridorSurface = None
    FeatureLine = None
    ProfileFromFeatureLine = None
    pass

class SettingsCorridor.SettingsRegionHighlightGraphics(object):
    """
    Settings for Corridor styles.
    """
    BaselineColor = None
    BaselineLineweight = None
    HighlightBaseline = None
    HighlightHorizontalTargets = None
    HighlightInteriorAssemblies = None
    HighlightRegionBoundary = None
    HorizontalTargetsColor = None
    HorizontalTargetsLineweight = None
    InteriorAssembliesColor = None
    InteriorAssembliesLineweight = None
    RegionBoundaryColor = None
    RegionBoundaryLineweight = None
    pass

class SettingsCorridor.SettingsStyles(object):
    """
    Settings to establish the default styles assigned to corridor components.
    """
    Alignment = None
    AlignmentLabelSet = None
    AlignmentLabelSetId = None
    AlignmentStyleId = None
    Corridor = None
    CorridorCodeSet = None
    CorridorCodeSetId = None
    CorridorStyleId = None
    CorridorSurface = None
    CorridorSurfaceStyleId = None
    FeatureLine = None
    FeatureLineStyleId = None
    Profile = None
    ProfileLabelSet = None
    ProfileLabelSetId = None
    ProfileStyleId = None
    RenderMaterial = None
    SlopePattern = None
    SlopePatternStyleId = None
    pass

class SettingsDrawing(object):
    """
    Contains settings that apply to the drawing, as specified in the Drawing Settings dialog box.
    """
    AbbreviationsSettings = None
    AmbientSettings = None
    ApplyTransformSettings = None
    ObjectLayerSettings = None
    TransformationSettings = None
    UnitZoneSettings = None
    pass

class SettingsGeneral(SettingsAmbient):
    """
    Settings for General.
    """
    Styles = None
    pass

class SettingsGeneral.SettingsStyles(object):
    """
    default styles.setting class.
    """
    CurveLabel = None
    CurveLabelStyleId = None
    LineLabel = None
    LineLabelStyleId = None
    NoteLabel = None
    NoteLabelStyleId = None
    pass

class SettingsGrading(SettingsAmbient):
    """
    Settings for Grading.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsGrading.SettingsNameFormat(object):
    """
    default name format for  new feature lines and grading groups.
    """
    FeatureLine = None
    GradingGroup = None
    pass

class SettingsGrading.SettingsStyles(object):
    """
    default styles for new slope grading.
    """
    CutSlopeGrading = None
    CutSlopeGradingStyleId = None
    FeatureLineStyle = None
    FeatureLineStyleId = None
    FillSlopeGrading = None
    FillSlopeGradingStyleId = None
    GradingStyle = None
    GradingStyleId = None
    pass

class SettingsIntersection(SettingsAmbient):
    """
    Settings for Intersection.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsIntersection.SettingsNameFormat(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    CorridorRegion = None
    CurbReturnAlignment = None
    CurbReturnProfile = None
    Intersection = None
    IntersectionQuadrant = None
    OffsetAlignment = None
    OffsetProfile = None
    pass

class SettingsIntersection.SettingsStyles(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    CurbReturnAlignment = None
    CurbReturnAlignmentLabelSet = None
    CurbReturnAlignmentLabelSetId = None
    CurbReturnAlignmentStyleId = None
    CurbReturnProfile = None
    CurbReturnProfileLabelSet = None
    CurbReturnProfileStyleId = None
    Intersection = None
    IntersectionLabel = None
    IntersectionLabelStyleId = None
    IntersectionStyleId = None
    OffsetAlignment = None
    OffsetAlignmentLabelSet = None
    OffsetAlignmentLabelSetId = None
    OffsetAlignmentStyleId = None
    OffsetProfile = None
    OffsetProfileLabelSet = None
    OffsetProfileStyleId = None
    pass

class SettingsLandXML(object):
    """
    Settings that define how data is imported from LandXML file.
    """
    Export = None
    Import = None
    pass

class SettingsLandXMLExport(object):
    """
    Settings that define how data is exported from LandXML file.
    """
    AlignmentExport = None
    Data = None
    Identification = None
    ParcelExport = None
    PointExport = None
    SurfaceExport = None
    pass

class SettingsLandXMLExport.SettingsAlignmentExport(object):
    """
    Alignment Settings for LandXML export.
    """
    ExportCrossSections = None
    pass

class SettingsLandXMLExport.SettingsData(object):
    """
    Data Settings for LandXML export.
    """
    AngleDirectionFormat = None
    CreateReadOnlyFile = None
    ImperialUnits = None
    pass

class SettingsLandXMLExport.SettingsIdentification(object):
    """
    Identification Settings for LandXML export.
    """
    Company = None
    CompanyURL = None
    Creator = None
    EmailAddress = None
    WriteIdentificationElements = None
    pass

class SettingsLandXMLExport.SettingsParcelExport(object):
    """
    Parcel Settings for LandXML export.
    """
    ParcelDirection = None
    pass

class SettingsLandXMLExport.SettingsPointExport(object):
    """
    Point Settings for LandXML export.
    """
    CodeAttribute = None
    DescAttribute = None
    ExportDescriptionKeys = None
    ExportPointReferences = None
    PointReferenceTolerance = None
    SkipFullWhenSameAsRaw = None
    pass

class SettingsLandXMLExport.SettingsSurfaceExport(object):
    """
    Surface Settings for LandXML export.
    """
    SurfaceData = None
    Watersheds = None
    pass

class SettingsLandXMLImport(object):
    """
    Settings that define how data is imported from LandXML file.
    """
    AlignmentImport = None
    ConflictResolution = None
    DiameterUnits = None
    PipeNetwork = None
    PointImport = None
     = None
    Rotation = None
    SurfaceImport = None
    Translation = None
    pass

class SettingsLandXMLImport.SettingsAlignmentImport(object):
    """
    Alignment settings for LandXML importing.
    """
    ElementConstraintAssignment = None
    pass

class SettingsLandXMLImport.SettingsConflictResolution(object):
    """
    ConflictResolution settings for LandXML importing.
    """
    ConflictResolution = None
    pass

class SettingsLandXMLImport.SettingsDiameterUnits(object):
    """
    On import, Autodesk Civil 3D reads the LandXML.Units.diameterUnits, and if they are defined, 
    those units are used for both pipes and structures. If units are not defined, 
    the following unit settings are applied. Either the Imperial or Metric diameter settings 
    are applied, based on the defined LandXML.Units.linearUnit in the file.
    """
    Imperial = None
    Metric = None
    pass

class SettingsLandXMLImport.SettingsPipeNetwork(object):
    """
    PipeNetwork settings for LandXML importing.
    """
    MatchChannelShapedPipesWith = None
    MatchCircularPipesWith = None
    MatchCircularStructuresWith = None
    MatchConnectionStructuresWith = None
    MatchEggShapedPipesWith = None
    MatchEllipticalShapedPipesWith = None
    MatchInletOutletStructuresWith = None
    MatchRectangleShapedPipesWith = None
    MatchRectangleStructuresWith = None
    PartsListForPartFamilySizeMatching = None
    pass

class SettingsLandXMLImport.SettingsPointImport(object):
    """
    PointImport settings for LandXML importing.
    """
    PointDescription = None
    pass

class SettingsLandXMLImport.SettingsPropertySetData(object):
    """
    PropertySetData settings for LandXML importing.
    """
    CreateAll = None
    pass

class SettingsLandXMLImport.SettingsRotation(object):
    """
    Rotation settings for LandXML importing.
    """
    Angle = None
    Direction = None
    Rotate = None
    pass

class SettingsLandXMLImport.SettingsSurfaceImport(object):
    """
    SurfaceImport settings for LandXML importing.
    """
    BreakLinesType = None
    ConvertSurveyFootToInternationalFoot = None
    CreateBreakLines = None
    CreateSnapshotAfterImport = None
    CreateSourceDataInDrawing = None
    SurfaceData = None
    pass

class SettingsLandXMLImport.SettingsTranslation(object):
    """
    Translation settings for LandXML importing.
    """
    BasePointEasting = None
    BasePointElevation = None
    BasePointNorthing = None
    Translate = None
    TranslatedCoordinateEasting = None
    TranslatedCoordinateElevation = None
    TranslatedCoordinateNorthing = None
    pass

class SettingsMassHaulLine(SettingsAmbient):
    """
    Settings for MassHaulLine.
    """

    pass

class SettingsMassHaulView(SettingsAmbient):
    """
    Settings for MassHaulView.
    """
    MassHaulCreation = None
    NameFormat = None
    Styles = None
    pass

class SettingsMassHaulView.SettingsMassHaulCreation(object):
    """
    default settings which are available when accessing the settings from the CreateMassHaul command, to establish the default settings when you create a mass haul diagram.
    """
    BorrowPitCapacity = None
    DumpSiteCapacity = None
    pass

class SettingsMassHaulView.SettingsNameFormat(object):
    """
    default name format for new mass haul lines and new mass haul views.
    """
    MassHaulLine = None
    MassHaulView = None
    pass

class SettingsMassHaulView.SettingsStyles(object):
    """
    default styles.for mass haul components.
    """
    MassHaulLine = None
    MassHaulLineStyleId = None
    MassHaulView = None
    MassHaulViewStyleId = None
    pass

class SettingsMatchLine(SettingsAmbient):
    """
    Settings for MatchLine.
    """

    pass

class SettingsObjectLayer(object):
    """
    SettingsObjectLayer class specifies layers for individual object in Autodesk Civil 3D.
    """
    LayerId = None
    LayerName = None
    Locked = None
    Modifier = None
    ModifierValue = None
    ObjectType = None
    pass

class SettingsObjectLayerType():
    """
    
    """
    pass

class SettingsObjectLayers(object):
    """
    The SettingsObjectLayers class is to specify layers for various objects in Autodesk Civil 3D. For example, 
    you can specify that you want all alignments on layer C-ROAD, all parcels on C-PROP,
    and so on. You can also specify prefixes and suffixes for the layer names.
    """
    ObjectControlledByLayer = None
    def GetObjectLayerSetting(self):
        """
        GetObjectLayerSetting(settingsType: Autodesk.Civil.Settings.SettingsObjectLayerType) -> SettingsObjectLayer
            Gets a SettingsObjectLayer object by specifying its type.
            settingsType: Autodesk.Civil.Settings.SettingsObjectLayerType
        """
        pass
    
    pass

class SettingsParcel(SettingsAmbient):
    """
    Settings for Parcel.
    """
    Styles = None
    pass

class SettingsParcel.SettingsStyles(object):
    """
    default styles for creating and labeling parcels.
    """
    Parcel = None
    ParcelAreaLabelStyle = None
    ParcelAreaLabelStyleId = None
    ParcelCurveLabel = None
    ParcelCurveLabelStyleId = None
    ParcelLineLabel = None
    ParcelLineLabelStyleId = None
    ParcelStyleId = None
    pass

class SettingsPipe(SettingsAmbient):
    """
    Settings for Pipe.
    """

    pass

class SettingsPipeNetwork(SettingsAmbient):
    """
    Settings for PipeNetwork.
    """
    Default = None
    NameFormat = None
    ProfileLabelPlacement = None
    Rules = None
    SectionLabelPlacement = None
    StormSewersMigration = None
    Styles = None
    pass

class SettingsPipeNetwork.SettingsDefault(object):
    """
    Settings for PipeNetwork default Settings.
    """
    UsePartListDescriptionForNewParts = None
    pass

class SettingsPipeNetwork.SettingsNameFormat(object):
    """
    Settings for PipeNetwork NameFormat.
    """
    AlignmentFromNetwork = None
    Interference = None
    InterferenceCheck = None
    Network = None
    Pipe = None
    Structure = None
    pass

class SettingsPipeNetwork.SettingsProfileLabelPlacement(object):
    """
    Settings for PipeNetwork ProfileLabelPlacement.
    """
    DimensionAnchorElevationValueForPipes = None
    DimensionAnchorElevationValueForStructures = None
    DimensionAnchorOptionForPipes = None
    DimensionAnchorOptionForStructures = None
    DimensionAnchorPlotHeightValueForPipes = None
    DimensionAnchorPlotHeightValueForStructures = None
    StructureLabelPlacement = None
    pass

class SettingsPipeNetwork.SettingsRules(object):
    """
    Settings for PipeNetwork Rules.
    """
    Pipe = None
    PipeStyleId = None
    Structure = None
    StructureStyleId = None
    pass

class SettingsPipeNetwork.SettingsSectionLabelPlacement(object):
    """
    Settings for PipeNetwork SectionLabelPlacement.
    """
    DimensionAnchorElevationValueForPipes = None
    DimensionAnchorElevationValueForStructures = None
    DimensionAnchorOptionForPipes = None
    DimensionAnchorOptionForStructures = None
    DimensionAnchorPlotHeightValueForPipes = None
    DimensionAnchorPlotHeightValueForStructures = None
    PipeSectionLabel = None
    StructureLabelPlacement = None
    pass

class SettingsPipeNetwork.SettingsStormSewersMigration(object):
    """
    Settings for PipeNetwork StormSewersMigration.
    """
    PartMatching = None
    PartMatchingId = None
    PartsListIdUsedForMigration = None
    PartsListUsedForMigration = None
    pass

class SettingsPipeNetwork.SettingsStyles(object):
    """
    Settings for PipeNetwork Styles.
    """
    Interference = None
    InterferenceRenderMaterial = None
    InterferenceStyleId = None
    PartsList = None
    PartsListId = None
    Pipe = None
    PipePlanLabel = None
    PipePlanLabelStyleId = None
    PipeProfileLabel = None
    PipeProfileLabelStyleId = None
    PipeSectionLabel = None
    PipeSectionLabelStyleId = None
    PipeStyleId = None
    RenderMaterial = None
    Structure = None
    StructurePlanLabel = None
    StructurePlanLabelStyleId = None
    StructureProfileLabel = None
    StructureProfileLabelStyleId = None
    StructureSectionLabel = None
    StructureSectionLabelStyleId = None
    StructureStyleId = None
    pass

class SettingsPoint(SettingsAmbient):
    """
    Settings for Point.
    """
    NameFormat = None
    Styles = None
    UpdatePoints = None
    pass

class SettingsPoint.SettingsNameFormat(object):
    """
    default name format for new points and point groups.
    """
    Point = None
    PointGroup = None
    pass

class SettingsPoint.SettingsStyles(object):
    """
    default styles assigned to points and points labels.
    """
    Point = None
    PointLabel = None
    PointLabelStyleId = None
    PointStyleId = None
    pass

class SettingsPoint.SettingsUpdatePoints(object):
    """
    specify whether you can change local copies of project points without checking them out.
    """
    AllowCheckedInPointsToBeModified = None
    pass

class SettingsPointCloud(SettingsAmbient):
    """
    Settings for PointCloud.
    """
    DefaultNameFormat = None
    StyleSettings = None
    pass

class SettingsPointCloud.SettingsDefaultNameFormat(object):
    """
    default name format setting class
    """
    PointCloudNameTemplate = None
    pass

class SettingsPointCloud.SettingsStyles(object):
    """
    default styles setting class
    """
    PointCloudStyle = None
    PointCloudStyleId = None
    pass

class SettingsProfile(SettingsAmbient):
    """
    Settings for Profile.
    """
    CriteriaBasedDesignOptions = None
    DefaultNameFormat = None
    ProfilesCreation = None
    StyleSettings = None
    pass

class SettingsProfile.SettingsCriteriaBasedDesignOptions(object):
    """
    criteria Based Design options setting class
    """
    DefaultDesignCheckSet = None
    DefaultDesignCheckSetId = None
    UseDesignChecksOption = None
    UseDesignCriteriaFileOption = None
    pass

class SettingsProfile.SettingsDefaultNameFormat(object):
    """
    default name format setting class
    """
    OffsetProfileNameTemplate = None
    ProfileNameTemplate = None
    SuperimposedProfileNameTemplate = None
    ThreeDEntityProfileNameTemplate = None
    pass

class SettingsProfile.SettingsProfileCreation(object):
    """
    default values for vertical curve sub-entities
    """
    AsymmetricalCrestCurveLength1 = None
    AsymmetricalCrestCurveLength2 = None
    AsymmetricalSagCurveLength1 = None
    AsymmetricalSagCurveLength2 = None
    CircularCrestCurveConstraint = None
    CircularCrestCurveLength = None
    CircularCrestCurveRadius = None
    CircularSagCurveConstraint = None
    CircularSagCurveLength = None
    CircularSagCurveRadius = None
    DefaultVerticalCurve = None
    HeadlightAngle = None
    HeadlightHeight = None
    ParabolicCrestCurveKValue = None
    ParabolicCrestCurveLength = None
    ParabolicCrestVerticalConstraint = None
    ParabolicSagCurveKValue = None
    ParabolicSagCurveLength = None
    ParabolicSagVerticalConstraint = None
    PassingEyeHeight = None
    PassingObjectHeight = None
    StopEyeHeight = None
    StopObjectHeight = None
    pass

class SettingsProfile.SettingsStyles(object):
    """
    default styles.setting class
    """
    ProfileLabelSet = None
    ProfileLabelSetId = None
    ProfileStyle = None
    ProfileStyleId = None
    pass

class SettingsProfileView(SettingsAmbient):
    """
    Settings for ProfileView.
    """
    Creation = None
    NameFormat = None
    ProjectionLabelPlacement = None
    SplitOptions = None
    StackedOptions = None
    Styles = None
    pass

class SettingsProfileView.SettingsCreation(object):
    """
    Settings for ProfileView default Creation.
    """
    PipeNetworkParts = None
    SpecifyProfileElevationRange = None
    SpecifyProfileStationRange = None
    pass

class SettingsProfileView.SettingsNameFormat(object):
    """
    Settings for ProfileView default NameFormat.
    """
    CutArea = None
    FillArea = None
    MultipleBoundaryArea = None
    ProfileView = None
    pass

class SettingsProfileView.SettingsProjectionLabelPlacement(object):
    """
    Settings for ProfileView default ProjectionLabelPlacement.
    """
    DimensionAnchorElevationValueForProjections = None
    DimensionAnchorOption = None
    DimensionAnchorPlotHeightValueForProjections = None
    pass

class SettingsProfileView.SettingsSplitOptions(object):
    """
    Settings for ProfileView default SplitOptions.
    """
    SplitDatumOption = None
    SplitProfileViews = None
    SplitStationOption = None
    pass

class SettingsProfileView.SettingsStackedOptions(object):
    """
    Settings for ProfileView default StackedOptions.
    """
    GapBetweenViews = None
    NumberOfStackedViews = None
    StackedViews = None
    pass

class SettingsProfileView.SettingsStyles(object):
    """
    Settings for ProfileView default Styles.
    """
    BottomStackViewStyle = None
    BottomStackViewStyleId = None
    CutAreaShapeStyle = None
    CutAreaShapeStyleId = None
    FillAreaShapeStyle = None
    FillAreaShapeStyleId = None
    FirstSplitViewStyle = None
    FirstSplitViewStyleId = None
    IntermediateSplitViewStyle = None
    IntermediateSplitViewStyleId = None
    LastSplitViewStyle = None
    LastSplitViewStyleId = None
    MarkerStyle = None
    MarkerStyleId = None
    MiddleStackViewStyle = None
    MiddleStackViewStyleId = None
    MultipleBoundaryAreaShapeStyle = None
    MultipleBoundaryAreaShapeStyleId = None
    ProfileDepthLabelStyle = None
    ProfileDepthLabelStyleId = None
    ProfileLabelSet = None
    ProfileLabelSetId = None
    ProfileLabelStyle = None
    ProfileProjectionLabelStyle = None
    ProfileProjectionLabelStyleId = None
    ProfileStationAndElevationLabelStyle = None
    ProfileStationAndElevationLabelStyleId = None
    ProfileViewBandStyle = None
    ProfileViewBandStyleId = None
    ProfileViewStyle = None
    ProfileViewStyleId = None
    ProjectionStyle = None
    ProjectionStyleId = None
    TopStackViewStyle = None
    TopStackViewStyleId = None
    pass

class SettingsQuantityTakeoff(SettingsAmbient):
    """
    Settings for QuantityTakeoff.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsQuantityTakeoff.SettingsNameFormat(object):
    """
    Settings to establish the default name format to quantity takeoff.
    """
    Material = None
    MaterialList = None
    pass

class SettingsQuantityTakeoff.SettingsStyles(object):
    """
    Settings to establish the default styles assigned to quantity takeoff.
    """
    MaterialShape = None
    MaterialShapeId = None
    QuantityTakeoffCriteria = None
    QuantityTakeoffCriteriaId = None
    pass

class SettingsRoot(object):
    """
    The root of the settings hierarchy.
    """
    AssociateShortcutProjectId = None
    DrawingSettings = None
    LandXMLSettings = None
    TagSettings = None
    def GetSettings(T)(self):
        """
        GetSettings(T)() -> SettingsAmbient
            Gets feature settings or command settings by specifying a type.
        """
        pass
    
    pass

class SettingsSampleLine(SettingsAmbient):
    """
    Settings for SampleLine.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsSampleLine.SettingsNameFormat(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    SampleLine = None
    SampleLineGroup = None
    pass

class SettingsSampleLine.SettingsStyles(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    SampleLine = None
    SampleLineLabel = None
    SampleLineLabelStyleId = None
    SampleLineStyleId = None
    pass

class SettingsSection(SettingsAmbient):
    """
    Settings for Section.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsSection.SettingsNameFormat(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    Section = None
    pass

class SettingsSection.SettingsStyles(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    Section = None
    SectionStyleId = None
    pass

class SettingsSectionView(SettingsAmbient):
    """
    Settings to specify the default styles assigned to section view components
    """
    NameFormat = None
    ProjectionLabelPlacement = None
    SectionViewCreation = None
    Styles = None
    pass

class SettingsSectionView.SettingsNameFormat(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    CrossSectionSheetLayout = None
    SectionView = None
    pass

class SettingsSectionView.SettingsProjectionLabelPlacement(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    DimensionAnchorElevationValueForProjections = None
    DimensionAnchorOption = None
    DimensionAnchorPlotHeightValueForProjections = None
    pass

class SettingsSectionView.SettingsSectionViewCreation(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    SectionGroupElevationRange = None
    SpecifySectionViewHeight = None
    SpecifySectionViewOffsetRange = None
    pass

class SettingsSectionView.SettingsStyles(object):
    """
    Settings to establish the default styles assigned to assembly components.
    """
    GroupPlot = None
    GroupPlotStyleId = None
    Marker = None
    MarkerStyleId = None
    Projection = None
    ProjectionStyleId = None
    SectionLabelSet = None
    SectionLabelSetId = None
    SectionProjectionLabel = None
    SectionProjectionLabelStyleId = None
    SectionView = None
    SectionViewBandSet = None
    SectionViewBandSetId = None
    SectionViewDepthGradeLabel = None
    SectionViewDepthGradeLabelStyleId = None
    SectionViewOffsetElevationLabel = None
    SectionViewOffsetElevationLabelStyleId = None
    SectionViewStyleId = None
    pass

class SettingsStructure(SettingsAmbient):
    """
    Settings for Structure.
    """

    pass

class SettingsSubassembly(SettingsAmbient):
    """
    Contains settings that apply to the assembly feature, as specified in the Edit Feature Settings dialog box.
    """
    DefaultStyles = None
    NameFormat = None
    pass

class SettingsSubassembly.SettingsDefaultStyles(object):
    """
    Settings for subassembly default styles.
    """
    CodeSetStyle = None
    CodeSetStyleId = None
    pass

class SettingsSubassembly.SettingsNameFormat(object):
    """
    Settings for Subassembly NameFormat.
    """
    CreateFromEntities = None
    CreateFromMacro = None
    pass

class SettingsSuperelevationView(SettingsAmbient):
    """
    Settings for SuperelevationView.
    """
    NameFormat = None
    Styles = None
    pass

class SettingsSuperelevationView.SettingsNameFormat(object):
    """
    Settings for SuperelevationView default NameFormat.
    """
    SuperelevationView = None
    pass

class SettingsSuperelevationView.SettingsStyles(object):
    """
    Settings for SuperelevationView default Styles.
    """
    SuperelevationViewStyle = None
    SuperelevationViewStyleId = None
    pass

class SettingsSurface(SettingsAmbient):
    """
    Settings for Surface.
    """
    ContourLabeling = None
    Defaults = None
    Styles = None
    pass

class SettingsSurface.SettingsContourLabeling(object):
    """
    Defaults assigned to surface labels.
    """
    DisplayContourLabelLine = None
    LabelMask = None
    SurfaceContourLabelStyleIdMajor = None
    SurfaceContourLabelStyleIdMinor = None
    SurfaceContourLabelStyleIdUserDefined = None
    SurfaceContourLabelStyleMajor = None
    SurfaceContourLabelStyleMinor = None
    SurfaceContourLabelStyleUserDefined = None
    pass

class SettingsSurface.SettingsDefaults(object):
    """
    Default name format for new surfaces.
    """
    AutoRebuild = None
    pass

class SettingsSurface.SettingsStyles(object):
    """
    Default styles.assigned to surfaces and surface-related labels.
    """
    Marker = None
    MarkerStyleId = None
    RenderMaterial = None
    Surface = None
    SurfaceSlopeLabel = None
    SurfaceSlopeLabelStyleId = None
    SurfaceSpotElevationLabel = None
    SurfaceSpotElevationLabelStyleId = None
    SurfaceStyleId = None
    pass

class SettingsSurvey(SettingsAmbient):
    """
    Settings for Survey.
    """
    Styles = None
    pass

class SettingsSurvey.SettingsStyles(object):
    """
    default styles.setting class.
    """
    CurveLabel = None
    CurveLabelStyleId = None
    Figure = None
    FigureLabel = None
    FigureLabelStyleId = None
    FigureStyleId = None
    LineLabel = None
    LineLabelStyleId = None
    Network = None
    NetworkStyleId = None
    pass

class SettingsTag(object):
    """
    The Settings specify how line, curve and spiral components are numbered and renumbered.
    """
    Creation = None
    Renumbering = None
    pass

class SettingsTag.SettingsCreation(object):
    """
    Settings of creation for the SettingsTag.
    """
    CurvesIncrement = None
    CurvesStartingNumber = None
    LinesIncrement = None
    LinesStartingNumber = None
    SpiralsIncrement = None
    SpiralsStartingNumber = None
    pass

class SettingsTag.SettingsRenumbering(object):
    """
    Settings of renumbering for the SettingsTag.
    """
    CurvesIncrement = None
    CurvesStartingNumber = None
    LinesIncrement = None
    LinesStartingNumber = None
    SpiralsIncrement = None
    SpiralsStartingNumber = None
    pass

class SettingsTransformation(object):
    """
    The SettingsTransformation class use to transform the coordinate system to local specifications.
    """
    ApplySeaLevelScaleFactor = None
    GridReferencePoint = None
    GridRotationPoint = None
    GridScaleFactor = None
    GridScaleFactorComputation = None
    LocalReferencePoint = None
    LocalRotationPoint = None
    RotationToGridAzimuth = None
    RotationToGridNorth = None
    SeaLevelScaleElevation = None
    SpecifyRotationType = None
    SpheroidRadius = None
    pass

class SettingsUnitZone(object):
    """
    The settings class for the unit zone.
    """
    AngularUnits = None
    CoordinateSystemCode = None
    DrawingScale = None
    DrawingUnits = None
    ImperialToMetricConversion = None
    MatchAutoCADVariables = None
    ScaleObjectsFromOtherDrawings = None
    def GetAllCodes(self):
        """
        GetAllCodes() -> string[]
            Gets an array that specifies all avilable code strings.
        """
        pass
    
    
    def GetCoordinateSystemByCode(self):
        """
        GetCoordinateSystemByCode(code: System.String) -> SettingsCoordinateSystem
            Gets an coordinate system by an code string.
            code: System.String
        """
        pass
    
    pass

class SettingsViewFrame(SettingsAmbient):
    """
    Settings for ViewFrame.
    """

    pass

class SettingsViewFrameGroup(SettingsAmbient):
    """
    Settings for ViewFrameGroup.
    """
    Information = None
    NameFormat = None
    Styles = None
    pass

class SettingsViewFrameGroup.SettingsInformation(object):
    """
    default match line label location setting class.
    """
    pass

class SettingsViewFrameGroup.SettingsNameFormat(object):
    """
    default name format for view frame group components.
    """
    Layout = None
    MatchLine = None
    SheetFile = None
    ViewFrame = None
    ViewFrameGroup = None
    pass

class SettingsViewFrameGroup.SettingsStyles(object):
    """
    default styles assigned to view frame group components.
    """
    MatchLine = None
    MatchLineLabelLeft = None
    MatchLineLabelRight = None
    MatchLineLabelStyleIdLeft = None
    MatchLineLabelStyleIdRight = None
    MatchLineLeftLabelLocation = None
    MatchLineRightLabelLocation = None
    MatchLineStyleId = None
    ProfileView = None
    ProfileViewBandSet = None
    ProfileViewBandSetId = None
    ProfileViewStyleId = None
    ViewFrame = None
    ViewFrameLabel = None
    ViewFrameLabelLocation = None
    ViewFrameLabelStyleId = None
    ViewFrameStyleId = None
    pass

class SpecifyRotationType():
    """
    An enumeration that use to specify a rotation about the reference point in one of two ways: specify a rotation point, or apply a grid rotation angle.
    """
    pass

class TableAnchorType():
    """
    Defines types of table anchors.
    """
    pass

class TableLayoutType():
    """
    Defines table layout directions.
    """
    pass

class TileDirectionType():
    """
    Defines tile directions.
    """
    pass