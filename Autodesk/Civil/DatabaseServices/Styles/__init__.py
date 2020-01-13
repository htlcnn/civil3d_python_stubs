class AlignmentDesignCheckSet(DBObject):
    """
    A collection of alignment design checks, which can be applied to an alignment.
    """

    def AddDesignCheck(self):
        """
        AddDesignCheck(type: Autodesk.Civil.AlignmentDesignCheckType, name: System.String) -> AlignmentDesignCheck
            Add one design check into this AlignmentDesignCheckSet.
            type: Autodesk.Civil.AlignmentDesignCheckType - The type of design check.
            name: System.String - The name of design check.
        """
        pass
    
    
    def GetAllDesignChecks(self):
        """
        GetAllDesignChecks() -> AlignmentDesignCheck
            Gets all design checks in this AlignmentDesignCheckSet.
        """
        pass
    
    
    def RemoveAllDesignCheck(self):
        """
        RemoveAllDesignCheck()
            Remove all design checks from this AlignmentDesignCheckSet.
        """
        pass
    
    
    def RemoveDesignCheck(self):
        """
        RemoveDesignCheck(designCheck: Autodesk.Civil.AlignmentDesignCheck) -> AlignmentDesignCheck
            Remove one design check from this AlignmentDesignCheckSet.
            designCheck: Autodesk.Civil.AlignmentDesignCheck - The design check needed to be removed.
        RemoveDesignCheck(type: Autodesk.Civil.AlignmentDesignCheckType, name: System.String) -> AlignmentDesignCheckType
            Remove one design check from this AlignmentDesignCheckSet.
            type: Autodesk.Civil.AlignmentDesignCheckType - The type of design check.
            name: System.String - The name of design check.
        """
        pass
    
    pass

class AlignmentDesignCheckSetCollection(StyleCollectionBase):
    """
    The AlignmentDesignCheckSetCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class AlignmentDisplayStyleType():
    """
    Defines AlignmentStyle display style type.
    """
    pass

class AlignmentLabelSetItem(BaseLabelSetItem):
    """
    The predefined label properties for alignments.
    """
    Increment = None
    def GetLabeledAlignmentGeometryPoints(self):
        """
        GetLabeledAlignmentGeometryPoints() -> AlignmentPointType
            Gets the alignment geometry points from the alignment label set item.
        """
        pass
    
    
    def GetLabeledProfileGeometryPoints(self):
        """
        GetLabeledProfileGeometryPoints() -> ProfilePointType
            Gets the profile geometry points from the alignment label set item.
        """
        pass
    
    
    def GetLabeledSuperelevationTransitionPoints(self):
        """
        GetLabeledSuperelevationTransitionPoints() -> SuperelevationPointType
            Gets the superelevation criteria geometry points from the alignment label set item.
        """
        pass
    
    
    def SetLabeledAlignmentGeometryPoints(self):
        """
        SetLabeledAlignmentGeometryPoints(pointTypes: System.Collections.Generic.Dictionary) -> AlignmentPointType
            Sets the alignment geometry points for the alignment label set item.
            pointTypes: System.Collections.Generic.Dictionary - A Dictionary collection of AlignmentPointType / bool pairs, indicating whether
            that alignment point type is set.
        """
        pass
    
    
    def SetLabeledProfileGeometryPoints(self):
        """
        SetLabeledProfileGeometryPoints(pointTypes: System.Collections.Generic.Dictionary) -> ProfilePointType
            Sets the profile geometry points for the alignment label set item.
            pointTypes: System.Collections.Generic.Dictionary - A Dictionary collection of ProfilePointType / bool pairs, indicating whether
            that profile point type is set.
        """
        pass
    
    
    def SetLabeledSuperelevationTransitionPoints(self):
        """
        SetLabeledSuperelevationTransitionPoints(pointTypes: System.Collections.Generic.Dictionary) -> SuperelevationPointType
            Sets the superelevation criteria geometry points for the alignment label set item.
            pointTypes: System.Collections.Generic.Dictionary - A Dictionary collection of SuperelevationPointType / bool pairs, indicating whether
            the superelevation point type is set.
        """
        pass
    
    pass

class AlignmentLabelSetStyle(DBObject):
    """
    The predefined label properties for stations, lines, and curves.
    """
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> AlignmentLabelSetItem
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class AlignmentLabelSetStyleCollection(StyleCollectionBase):
    """
    The AlignmentLabelStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class AlignmentStyle(DBObject):
    """
    Specifies properties for the various alignment components.
    """
    ArrowHeadOption = None
    BeginPointMarkerStyle = None
    CompoundCurveIntersectPointMarkerStyle = None
    CurveLineIntersectPointMarkerStyle = None
    CurveSpiralIntersectPointMarkerStyle = None
    EnableRadiusSnap = None
    EndPointMarkerStyle = None
    IntersectionPointMarkerStyle = None
    LineCurveIntersectPointMarkerStyle = None
    LineMarkerDisplayStyleSection = None
    LineSpiralIntersectPointMarkerStyle = None
    MidPointMarkerStyle = None
    RadiusSnapValue = None
    ReverseCurveIntersectPointMarkerStyle = None
    ReverseSpiralIntersectPointMarkerStyle = None
    SpiralCurveIntersectPointMarkerStyle = None
    SpiralLineIntersectPointMarkerStyle = None
    SpiralSpiralIntersectPointMarkerStyle = None
    StationReferencePointMarkerStyle = None
    ThroughPointMarkerStyle = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.AlignmentDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties for the Alignment component.
            type: Autodesk.Civil.DatabaseServices.Styles.AlignmentDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.AlignmentDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the Alignment component.
            type: Autodesk.Civil.DatabaseServices.Styles.AlignmentDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection() -> DisplayStyle
            Gets the DisplayStyle object that specifies the line marker in section display properties for the Alignment component.
            Remarks: Replace for the property: LineMarkerDisplayStyleSection.
        """
        pass
    
    
    def GetLineMarkerDisplayStyleSection(self):
        """
        GetLineMarkerDisplayStyleSection() -> DisplayStyle
            Gets the display style for line markers in section view orientation.
        """
        pass
    
    pass

class AlignmentStyleCollection(StyleCollectionBase):
    """
    A collection of AlignmentStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class ArrowHeadOption(object):
    """
    Display options for arrows in AlignmentStyle and ProfileStyle.
    """
    ArrowBlockName = None
    ArrowType = None
    Fit = None
    FixedScaleX = None
    FixedScaleY = None
    FixedScaleZ = None
    SizeOption = None
    SizeValue = None
    pass

class AssemblyStyle(DBObject):
    """
    Used to control the visual style of an Assembly object.
    """
    MarkerStyleAtAssemblyOriginId = None
    MarkerStyleAtMainBaselineId = None
    MarkerStyleAtMainBaselineOriginId = None
    MarkerStyleAtOffsetBaselineId = None
    MarkerStyleAtOffsetBaselineOriginId = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.AssemblyDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the corridor model display components.
            type: Autodesk.Civil.AssemblyDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.AssemblyDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the corridor plan display components.
            type: Autodesk.Civil.AssemblyDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class AssemblyStyleCollection(StyleCollectionBase):
    """
    A collection of AssemblyStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class AxisPosition():
    """
    Defines profile view, section view axis position.
    """
    pass

class AxisStyle(object):
    """
    Controls the use of tick marks on the horizontal and vertical axes of the profile view or cross section view.
    """
    HorizontalGeometryTickStyle = None
    MajorTickStyle = None
    MinorTickStyle = None
    ShowTickAndLabel = None
    TitleStyle = None
    pass

class AxisTickJustificationType():
    """
    Specifies the position of the tick relative to the axis.
    """
    pass

class AxisTickStyle(object):
    """
    Controls the title location and display on the horizontal and vertical axes of the profile view or cross section view.
    """
    Interval = None
    Justification = None
    LabelText = None
    OffsetX = None
    OffsetY = None
    Rotation = None
    Size = None
    TextHeight = None
    TextStyle = None
    TickAndLabelStartElevation = None
    pass

class AxisTickType():
    """
    Defines profile view, section view axis tick type.
    """
    pass

class AxisTitleLocationType():
    """
    Specifies the location of the axis title in relation to the view grid.
    """
    pass

class AxisTitleStyle(object):
    """
    The AxisTitleStyle class, which defines the text, text style, size etc. of an axis title.
    """
    Location = None
    OffsetX = None
    OffsetY = None
    Rotation = None
    Text = None
    TextHeight = None
    TextStyle = None
    pass

class BandLabelStyleType():
    """
    Defines the band label style type.
    """
    pass

class BandSetItem(ProfileViewBandSetItem):
    """
    This class encapsulates a single view data band, serves as a base class for the band item in the profile/section view.
    """
    BandStyleId = None
    BandType = None
    Gap = None
    Location = None
    MajorInterval = None
    MinorInterval = None
    ShowLabels = None
    StaggerLabel = None
    StaggerLineHeight = None
    Weeding = None
    pass

class BandSetItemCollection(ProfileViewBandItemCollection):
    """
    This class stores all the band items, serves as a base class for the profile/section view band items collection.
    """
    Count = None
    Location = None
    def Add(self):
        """
        Add(bandStyleId: ObjectId)
            Creates a new band item with the given bandStyle ObjectId, adds it to the collection.
            bandStyleId: ObjectId - The band style ObjectId.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the BandSetItemCollection
        """
        pass
    
    
    def RemoveAll(self):
        """
        RemoveAll()
            Removes all the band items from the current collection.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes an band item from the current collection.
            index: System.Int32 - The index of the band item in the current collection.
        """
        pass
    
    
    def Swap(self):
        """
        Swap(index1: System.Int32, index2: System.Int32)
            Switchs the position of band item by index.
            index1: System.Int32
            index2: System.Int32
        """
        pass
    
    pass

class BandSetStyle(DBObject):
    """
    This class serves as a base class for the profile/section bandset style.
    """
    MatchIncrementToGridIntervals = None

    pass

class BandStyle(DBObject):
    """
    Specifies style properties for data bands, the graphic frames that are associated with a profile view object or section view object.
    """
    BandHeight = None
    BandType = None
    OffsetFromBand = None
    Text = None
    TextBoxPosition = None
    TextBoxWidth = None
    TextHeight = None
    TextLocation = None
    TextStyle = None
    TitleTextLabelStyleId = None
    WeedingFactor = None
    def GetBandStyleId(self):
        """
        GetBandStyleId(database: Database, bandType: Autodesk.Civil.BandType, bandStyleName: System.String) -> BandType
            Get the ObjectId of BandStyle with the specified bandType and bandStyleName from the specified database.
            database: Database - The database where to get the band styleId.
            bandType: Autodesk.Civil.BandType - The band type.
            bandStyleName: System.String - The name of band style.
        """
        pass
    
    pass

class BandStyleCollection(StyleCollectionBase):
    """
    A collection of BandStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class BandStylesRoot(object):
    """
    The root object that contains collections of the various band styles in a document.
    """
    ProfileViewHorizontalGeometryBandStyles = None
    ProfileViewPipeNetworkBandStyles = None
    ProfileViewProfileDataBandStyles = None
    ProfileViewSectionalDataBandStyles = None
    ProfileViewSuperElevationBandStyles = None
    ProfileViewVerticalGeometryBandStyles = None
    SectionViewSectionDataBandStyles = None
    SectionViewSegmentsBandStyles = None
    pass

class BandTickStyle(object):
    """
    Specifies the type and location of ticks for profile or section view data bands.
    """
    IncrementSmallTicksAtBottom = None
    IncrementSmallTicksAtMiddle = None
    IncrementSmallTicksAtTop = None
    IncrementTicksToFullHeight = None
    SmallTicksAtBottomSize = None
    SmallTicksAtMiddleSize = None
    SmallTicksAtTopSize = None
    pass

class BandTitleBoxPosition():
    """
    Defines the band title box postion.
    """
    pass

class BandTitleTextLocation():
    """
    Defines the band title text location.
    """
    pass

class BaseLabelSetItem(AlignmentLabelSetItem):
    """
    The base class for alignment label set items.
    """
    LabelStyleId = None
    LabelStyleName = None
    LabelStyleType = None
    pass

class BaseLabelSetStyle(DBObject):
    """
    The base class for alignment label set styles.
    """
    Count = None
    def Add(self):
        """
        Add(labelStyleId: ObjectId)
            Creates a label set item with the given object id, adds it to the collection.
            Remarks: Use the alignment related label style types in the AlignmentLabelSetStyle class.Use the profile related label style types in the ProfileLabelSetStyle class.Use the section related label style types in the SectionLabelSetStyle class.Cannot be used with these label style types: Autodesk.Civil.DatabaseServices.LabelType.AlignmentMinorStation, ProfileMinorStation, and SectionMinorOffset.
            labelStyleId: ObjectId - The object id of label style.
        Add(majorStation: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetItem, minorStationLabelStyleId: ObjectId) -> BaseLabelSetItem
            Creates a minor label set item with the an major station label set item and an minor station label style id, adds it to the collection.
            majorStation: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetItem - An label set itm withe a major station label style type.
            minorStationLabelStyleId: ObjectId - The object id of label style.
        Add(majorStation: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetItem, minorStationLabelStyleName: System.String) -> BaseLabelSetItem
            Creates a minor label set item with the an major station label set item and an minior lable style name, adds it to the collection.
            majorStation: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetItem - An label set itm withe a major station label style type.
            minorStationLabelStyleName: System.String - The name of the label style with a type of minor station.
        Add(labelStyleType: Autodesk.Civil.DatabaseServices.Styles.LabelStyleType, labelStyleName: System.String) -> LabelStyleType
            Creates a label set item with the given lable style type and name, adds it to the collection.
            Remarks: Use the alignment related label style types in the AlignmentLabelSetStyle class.Use the profile related label style types except ProfileCurve in the ProfileLabelSetStyle class.Use the section related label style types in the SectionLabelSetStyle class.Cannot be used with these label style types: Autodesk.Civil.DatabaseServices.LabelType.AlignmentMinorStation, ProfileMinorStation, and SectionMinorOffset.
            labelStyleType: Autodesk.Civil.DatabaseServices.Styles.LabelStyleType - The type of label style.
            labelStyleName: System.String - The name of label style.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes an label set item from the collection.
            index: System.Int32 - Specified the label set item by index.
        """
        pass
    
    pass

class BuildingSiteDisplayStyleType():
    """
    An enumeration that defines BuildingSiteStyle display style type.
    """
    pass

class BuildingSiteStyle(DBObject):
    """
    Display options for building site objects.
    """
    MarkerStyleId = None
    MarkerStyleName = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties for the BuildingSite component.
            type: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the BuildingSite component.
            type: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class BuildingSiteStyleCollection(StyleCollectionBase):
    """
    A collection of BuildingSiteStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class CantViewStyle(DBObject):
    """
    The class to describe CantView object style.
    """
    AxisBottomMajorTickInterval = None
    AxisTopMajorTickInterval = None
    UseFullHeightTick = None
    UseSmallTicksAtBottom = None
    UseSmallTicksAtMiddle = None
    UseSmallTicksAtTop = None
    VerticalExaggeration = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.CantViewDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the Cant component.
            type: Autodesk.Civil.CantViewDisplayStyleType
        """
        pass
    
    pass

class CantViewStyleCollection(StyleCollectionBase):
    """
    The CantViewStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class CatchmentDisplayStylePlanType():
    """
    Specifies the display style type when the catchment area is displayed in plan view.
    """
    pass

class CatchmentStyle(DBObject):
    """
    Defines how a catchment area appears in plan view.
    """
    DischargePointMarkerStyle = None
    FlowSegmentStartPointMarkerStyle = None
    MostDistantPointMarkerStyle = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.CatchmentDisplayStylePlanType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the catchment area component.
            type: Autodesk.Civil.DatabaseServices.Styles.CatchmentDisplayStylePlanType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class CatchmentStyleCollection(StyleCollectionBase):
    """
    A collection of CatchmentStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class CenterMarkerSizeType():
    """
    Defines grading style center marker size type.
    """
    pass

class CodeSetStyle(DBObject):
    """
    A collection of CodeSetStyleItem objects.
    CodeSetStyleItem defines a code and related style,  where the style is the ObjectId of a LinkStyle or ShapeStyle.
    """
    Count = None
    Item = None
    SubentityStyleType = None
    def Add(self):
        """
        Add(code: System.String, styleId: ObjectId) -> CodeSetStyleItem
            Add method.
            Remarks: You can use the method to add the item which type is NormalItemType.
            code: System.String - 
            The name of this code.
            styleId: ObjectId - 
            The style of this code.
        """
        pass
    
    
    def GetCurrentStyleSetId(self):
        """
        GetCurrentStyleSetId() -> ObjectId
            Gets the ObjectId of the current CodeSetStyle.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CodeSetStyleItem
            Get the enumerator of this collection.
        """
        pass
    
    
    def GetItemBy(self):
        """
        GetItemBy(itemType: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleItemType, code: System.String) -> CodeSetStyleItem
            Indexer.
            Remarks: You can use the method to get the item which type is DefaultItemType or NoCodeItemType, and the code just affect the item which type is NormalItemType.
            itemType: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleItemType - 
            Indicate the item type.
            code: System.String - 
            The name of this code.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Get the enumerator of this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(code: System.String)
            Remove method.
            Remarks: You can use the method to remove the item which type is NormalItemType.
            code: System.String - 
            The name of this code.
        """
        pass
    
    pass

class CodeSetStyleCollection(StyleCollectionBase):
    """
    A collection of CodeSetStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class CodeSetStyleItem(object):
    """
    Defines the style to apply to a specific code.
    """
    Code = None
    CodeStyleId = None
    CodeStyleName = None
    Description = None
    FeatureLineStyleId = None
    FeatureLineStyleName = None
    ItemType = None
    LabelStyleId = None
    LabelStyleName = None
    MaterialAreaFillStyleId = None
    MaterialAreaFillStyleName = None
    PayItems = None
    RenderMaterialStyleId = None
    RenderMaterialStyleName = None
    StyleType = None
    pass

class CodeSetStyleItemType():
    """
    Specifies valid CodeSetStyleItem types.
    """
    pass

class ColorSchemeType():
    """
    Defines color scheme type
    """
    pass

class ColumnStyle(SegmentColumnStyle):
    """
    Defines column width and value properties for table style objects.
    """
    ColumnWidth = None
    ContentJustification = None
    ContentString = None
    ContentStringFormatted = None
    HeaderJustification = None
    HeaderString = None
    HeaderStringFormatted = None
    pass

class ColumnStyleCollection(object):
    """
    A collection of ColumnStyle objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add()
            Adds a ColumnStyle to the collection using column width and value, 0 width for auto width.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ColumnStyle
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes column style by index in the collection, the first column of the collection cannot be removed.
            index: System.Int32 - Index of the column style to remove.
        """
        pass
    
    pass

class ContourSmoothingType():
    """
    Defines how surface contours are smoothed.
    """
    pass

class ContourValues(object):
    """
    Defines how to display major and minor contour lines; used by the SurfaceContourStyle class.
    """
    MajorColor = None
    MajorLineTypeId = None
    MajorLineWeight = None
    MinorColor = None
    MinorLineTypeId = None
    MinorLineWeight = None
    pass

class CorridorDisplayStyleType():
    """
    
    """
    pass

class CorridorStyle(DBObject):
    """
    Defines the appearance of objects.
    """

    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.CorridorDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the corridor model display components.
            type: Autodesk.Civil.DatabaseServices.Styles.CorridorDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.CorridorDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the corridor plan display components.
            type: Autodesk.Civil.DatabaseServices.Styles.CorridorDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class CorridorStyleCollection(StyleCollectionBase):
    """
    A collection of CorridorStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class CustomMarkerSuperimposeType():
    """
    Specifies the custom point style marker as either none, a superimposed circle, a superimposed square, or both superimposed square and circle.
    """
    pass

class CustomMarkerType():
    """
    Specifies the custom point style marker as either a dot, a blank, two perpendicular lines (plus sign), two x-crossed lines, or a single vertical line.
    """
    pass

class DataBandingType():
    """
    Defines Data Banding Mode style type.
    """
    pass

class DataPartFamily(object):
    """
    Part family data that is queried from the catalog.
    """
    BoundingShape = None
    Description = None
    Domain = None
    GUID = None
    PartType = None
    SweptShape = None
    pass

class DisplayStyle(object):
    """
    Specifies display properties for the style, such as layer, color, and linetype.
    """
    Color = None
    Layer = None
    Linetype = None
    LinetypeScale = None
    Lineweight = None
    PlotStyle = None
    Visible = None
    pass

class Expression(object):
    """
    Encapsulates an expression used in label styles.
    """
    Description = None
    ExpressionString = None
    FormatResultAs = None
    Name = None
    pass

class ExpressionCollection(object):
    """
    A collection of Expression objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, description: System.String, expression: System.String) -> Expression
            Adds a Expression by specifying the name and expression string.
            name: System.String - The name of Expression.
            description: System.String - The description of Expression.
            expression: System.String - The expression string of Expression.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all Expressions from the collection.
            Remarks: This will remove all Expression objects in AlignmentExpressionSet or ProfileExpressionSet.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> Expression
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes an Expression from the collection by the specified index.
            Remarks: Removes the corresponding Expression from AlignmentExpressionSet or ProfileExpressionSet.
            index: System.Int32 - Specifies index in the collection to remove.
        """
        pass
    
    pass

class ExpressionFormatedType():
    """
    Defines the format type of the expression result.
    """
    pass

class FeatureLineDisplayStyleProfileType():
    """
    Defines FeatureLineStyle display style type.
    """
    pass

class FeatureLineStyle(DBObject):
    """
    Specifies default display and other characteristics for feature line features when they are created.
    """
    FeatureLineDisplayStyleModel = None
    FeatureLineDisplayStylePlan = None
    ProfileBeginningVertexMarkerStyleId = None
    ProfileBeginningVertexMarkerStyleName = None
    ProfileEndingVertexMarkerStyleId = None
    ProfileEndingVertexMarkerStyleName = None
    ProfileInternalVertexMarkerStyleId = None
    ProfileInternalVertexMarkerStyleName = None
    SectionMarkerDisplayStyleSection = None
    SectionMarkerStyleId = None
    SectionMarkerStyleName = None
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(type: Autodesk.Civil.DatabaseServices.Styles.FeatureLineDisplayStyleProfileType) -> DisplayStyle
            Gets the DisplayStyle object that specifies profile display properties for the FeatureLine component.
            type: Autodesk.Civil.DatabaseServices.Styles.FeatureLineDisplayStyleProfileType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetFeatureLineDisplayStyleModel(self):
        """
        GetFeatureLineDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle property that specifies, for the feature line, such Model display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetFeatureLineDisplayStylePlan(self):
        """
        GetFeatureLineDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle property that specifies, for the feature line, such Plan display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetSectionMarkerDisplayStyleSection(self):
        """
        GetSectionMarkerDisplayStyleSection() -> DisplayStyle
            Gets the DisplayStyle property that specifies, for the section marker, such Section display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    pass

class FeatureLineStyleCollection(StyleCollectionBase):
    """
    A collection of FeatureLineStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class GradingCriteria(DBObject):
    """
    Specifies grading criteria (a projection method and target) to create a finished grading surface.
    """
    CutSlope = None
    CutSlopeFormatType = None
    Distance = None
    DistanceProjectionType = None
    Elevation = None
    ElevationProjectionType = None
    FillSlope = None
    FillSlopeFormatType = None
    InteriorCornerOverlap = None
    ProjectionDistance = None
    ProjectionRelativeElevation = None
    RelativeElevation = None
    RelativeElevationProjectionType = None
    SearchOrder = None
    Slope = None
    SlopeFormatType = None
    SurfaceProjectionType = None
    Target = None
    def CopyAsSibling(self):
        """
        CopyAsSibling(criteriaName: System.String) -> ObjectId
            Copy the current grading criteria and add to the grading criteria set as a sibling.
            criteriaName: System.String - The name of the new grading criteria.
        """
        pass
    
    pass

class GradingCriteriaSet(DBObject):
    """
    A set of multiple related GradingCriteria objects.
    """
    Count = None
    Item = None
    def AddCriteria(self):
        """
        AddCriteria(criteriaName: System.String)
            Add a new grading criteria to the current set.
            criteriaName: System.String - The name of the grading criteria.
        """
        pass
    
    
    def GradingCriteriaIds(self):
        """
        GradingCriteriaIds() -> ObjectIdCollection
            Gets the objectId collection of all grading criteria objects in the set.
        """
        pass
    
    
    def MoveCriteria(self):
        """
        MoveCriteria(criteriaId: ObjectId, criteriaSetId: ObjectId)
            Move a grading criteria from the current grading criteria set to another set by object id.
            Remarks: OBJECTID TYPE: criteriaId = Autodesk.Civil.DatabaseServices.Style.GradingCriteria.
            OBJECTID TYPE: criteriaSetId = Autodesk.Civil.DatabaseServices.Style.GradingCriteriaSet.
            criteriaId: ObjectId - The object id of the grading criteria.
            criteriaSetId: ObjectId - The object id of the grading criteria set.
        MoveCriteria(criteriaName: System.String, criteriaSetName: System.String)
            Move a grading criteria from the current grading criteria set to another set by name.
            criteriaName: System.String - The name of the grading criteria.
            criteriaSetName: System.String - The name of the grading criteria set.
        """
        pass
    
    
    def RemoveCriteria(self):
        """
        RemoveCriteria(index: System.Int32)
            Removes a grading criteria by index from the current grading criteria set.
            index: System.Int32 - The index of the grading criteria to remove from the current grading criteria set.
        RemoveCriteria(criteriaName: System.String)
            Removes a grading criteria by name from the current grading criteria set.
            criteriaName: System.String - The name of the grading criteria to remove from the current grading criteria set.
        """
        pass
    
    pass

class GradingCriteriaSetCollection(StyleCollectionBase):
    """
    A collection of GradingCriteriaSet objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            Adds a GradingCriteriaSet to the collection by name.
            name: System.String
        """
        pass
    
    pass

class GradingDisplayStyleType():
    """
    Defines grading display style type.
    """
    pass

class GradingStyle(DBObject):
    """
    Specifies default display and other characteristics for grading features when they are created.
    """
    CenterMarker = None
    FixedSize = None
    PercentageOfScreen = None
    PlottedSize = None
    SlopePatternStyleId = None
    SlopePatternStyleName = None
    SlopeRangeMax = None
    SlopeRangeMin = None
    UseSlopePatternStyle = None
    UseSlopeRange = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.GradingDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the grading component Model display color, layer, linetype, etc.
            type: Autodesk.Civil.DatabaseServices.Styles.GradingDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.GradingDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the grading component Plan display color, layer, linetype, etc.
            type: Autodesk.Civil.DatabaseServices.Styles.GradingDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class GradingStyleCollection(StyleCollectionBase):
    """
    A collection of GradingStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    
    def SetCenterMarkerVisable(self):
        """
        SetCenterMarkerVisable(isVisable: System.Boolean)
            Specifies whether the center marker of all grading styles is visable in the current view port(Plan/Model).
            isVisable: System.Boolean
        """
        pass
    
    
    def SetSlopePatternVisable(self):
        """
        SetSlopePatternVisable(isVisable: System.Boolean)
            Specifies whether the slope pattern of all grading styles is visable in the current view port(Plan/Model).
            isVisable: System.Boolean
        """
        pass
    
    pass

class GraphDirectionType():
    """
    Specifies the direction of the profile in the profile view grid.
    """
    pass

class GraphStyle(object):
    """
    Specifies format and contents of the title, vertical exaggeration, and grid options for graphs.
    """
    CurrentHorizontalScale = None
    Direction = None
    TitleStyle = None
    VerticalExaggeration = None
    VerticalScale = None
    pass

class GraphTitleJustificationType():
    """
    Specifies the location of the graph title in relation to the view grid.
    """
    pass

class GraphTitleLocationType():
    """
    Specifies the location of the graph title in relation to the view grid.
    """
    pass

class GraphTitleStyle(object):
    """
    Specifies display characteristics for profile and section view graphs.
    """
    Border = None
    BorderGap = None
    Justification = None
    Location = None
    OffsetX = None
    OffsetY = None
    Text = None
    TextHeight = None
    TextStyle = None
    pass

class GridOptions(object):
    """
    Specifies various grid options used by GridStyle.
    """
    ClipToHighestProfile = None
    OmitGridInPaddingAreas = None
    UseClipGrid = None
    pass

class GridStyle(object):
    """
    Specifies display characteristics for profile and section view graph gridlines.
    """
    AxisOffsetAbove = None
    AxisOffsetBottom = None
    AxisOffsetLeft = None
    AxisOffsetRight = None
    GridPaddingAbove = None
    GridPaddingBottom = None
    GridPaddingLeft = None
    GridPaddingRight = None
    HorizontalGridOptions = None
    VerticalGridOptions = None
    pass

class GridType():
    """
    Defines clipping options on the profile view or section view grid.
    """
    pass

class GroupPlotAlignType():
    """
    Specifies how the section views are aligned.
    """
    pass

class GroupPlotCellSizeType():
    """
    Specifies how the size of each cell in the array will be determined.
    """
    pass

class GroupPlotDisplayStyleType():
    """
    Defines GroupPlotStyle display style type.
    """
    pass

class GroupPlotStartCornerType():
    """
    Specifies the starting corner for plotting the section views.
    """
    pass

class GroupPlotStyle(DBObject):
    """
    Specifies section view group plot style settings.
    """
    AlignType = None
    CellSizeType = None
    GapBetweenPages = None
    GridHorizontalMajor = None
    GridHorizontalMinor = None
    GridVerticalMajor = None
    GridVerticalMinor = None
    MaximumInColumn = None
    MaximumInRow = None
    PlotRule = None
    SpaceColumn = None
    SpaceRow = None
    StartCorner = None
    def GetDisplayPlan(self):
        """
        GetDisplayPlan(type: Autodesk.Civil.DatabaseServices.Styles.GroupPlotDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the SheetStyle component.
            type: Autodesk.Civil.DatabaseServices.Styles.GroupPlotDisplayStyleType
        """
        pass
    
    pass

class GroupPlotStyleCollection(StyleCollectionBase):
    """
    A collection of GroupPlotStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class HatchDisplayStyle(object):
    """
    Represents the hatch display properties for a component (such as parcels).
    """
    Angle = None
    HatchType = None
    IsDoubleHatch = None
    Pattern = None
    ScaleFactor = None
    Spacing = None
    UOffset = None
    UseAngleOfObject = None
    VOffset = None
    pass

class HatchType():
    """
    
    """
    pass

class HorizontalGeometryBandStyle(DBObject):
    """
    The style object specifying characteristics for profile view horizontal geometry data bands.
    """
    BandType = None
    CurveLabelStyleId = None
    CurveTickStyle = None
    PointOfIntersectionLabelStyleId = None
    PointOfIntersectionTickStyle = None
    SchematicLineType = None
    SpiralLabelStyleId = None
    SpiralTickStyle = None
    TangentLabelStyleId = None
    TangentTickStyle = None
    TitleTextLabelStyleId = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.HorizontalGeometryDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the HorizontalGeometry component.
            type: Autodesk.Civil.DatabaseServices.Styles.HorizontalGeometryDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class HorizontalGeometryDisplayStyleType():
    """
    Defines HorizontalGeometryBandStyle display style type.
    """
    pass

class InterferenceDisplayStyleType():
    """
    Specifies the display style type when the Structure is displayed in plan/model/section view.
    """
    pass

class InterferenceModelSizeOptionType():
    """
    Specifies the model size option.
    """
    pass

class InterferenceModelSizeType():
    """
    Specifies the size of the sphere in model view.
    """
    pass

class InterferenceModelType():
    """
    Specifies the type that will be used to visually identify interferences in model view.
    """
    pass

class InterferenceStyle(DBObject):
    """
    Defines how a pipe interference appears in plan, profile, section, and 3D view.
    """
    AbsoluteModelSize = None
    DrawingScaleModelSize = None
    MarkerStyle = None
    ModelOptions = None
    ModelSizeOptions = None
    ModelSizeType = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(component: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that defines the model style for the component indicated by the specified InterferenceDisplayStyleType value.
            component: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType - The interference display component to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(component: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Plan style for the component indicated by the specified InterferenceDisplayStyleType value.
            component: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType - The interference display component to get.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection(component: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Section style for the component indicated by the specified InterferenceDisplayStyleType value.
            component: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType - The interference display component to get.
        """
        pass
    
    pass

class InterferenceStyleCollection(StyleCollectionBase):
    """
    A collection of InterferenceStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class IntersectionStyle(DBObject):
    """
    The match line style wrapper class.
    """
    MarkerStyleId = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties for the intersection component.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the intersection component.
        """
        pass
    
    pass

class IntersectionStyleCollection(StyleCollectionBase):
    """
    The IntersectionStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class LabelDisplayModeType():
    """
    
    """
    pass

class LabelSetStylesRoot(object):
    """
    The root object for accessing label set style collections in the database.
    """
    AlignmentLabelSetStyles = None
    ProfileLabelSetStyles = None
    SectionLabelSetStyles = None
    pass

class LabelStyle(DBObject):
    """
    The master label style class, containing feature-specific label styles and associated information such as derived styles.
    """
    ChildrenCount = None
    Item = None
    ParentLabelStyleId = None
    Properties = None
    def AddChild(self):
        """
        AddChild(labelStyleName: System.String) -> ObjectId
            Add a new child label style to the current label style's node with the default setings' value.
            labelStyleName: System.String - The name of the label style.
        """
        pass
    
    
    def AddComponent(self):
        """
        AddComponent(name: System.String, type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType) -> LabelStyleComponentType
            Add a valid component into the label style.
            name: System.String - The name of component.
            type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType - The type of component.
        """
        pass
    
    
    def AddReferenceTextComponent(self):
        """
        AddReferenceTextComponent(name: System.String, selectedType: Autodesk.Civil.DatabaseServices.Styles.ReferenceTextComponentSelectedType) -> ReferenceTextComponentSelectedType
            Add ReferenceText component into the label style.
            name: System.String - The name of component.
            selectedType: Autodesk.Civil.DatabaseServices.Styles.ReferenceTextComponentSelectedType - The selected type of reference text component.
        """
        pass
    
    
    def AddTextForEachComponent(self):
        """
        AddTextForEachComponent(name: System.String, selectedType: Autodesk.Civil.DatabaseServices.Styles.TextForEachComponentSelectedType) -> TextForEachComponentSelectedType
            Add TextForEach component into the label style.
            name: System.String - The name of component.
            selectedType: Autodesk.Civil.DatabaseServices.Styles.TextForEachComponentSelectedType - The selected type of text for each component.
        """
        pass
    
    
    def GetComponents(self):
        """
        GetComponents(type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType) -> LabelStyleComponentType
            Gets the objectId collection of label style components that specify the appearance and behavior of labels.
            type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType - Type of label style component to get.
        """
        pass
    
    
    def GetComponentsCount(self):
        """
        GetComponentsCount() -> int
            The number of all components.
        GetComponentsCount(type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType) -> LabelStyleComponentType
            The number of a specific type of component.
            type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType - Type of label style component to count.
        """
        pass
    
    
    def GetComponentsDrawOrder(self):
        """
        GetComponentsDrawOrder() -> ObjectId[]
            Gets the supported components in draw order, component at the end(as UI list on the top) is drawn last.
        """
        pass
    
    
    def IsSupportedComponent(self):
        """
        IsSupportedComponent(type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType) -> LabelStyleComponentType
            Gets an bool value specifies whether the component type is supported in this label style.
            type: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType - Type of label style component to query.
        """
        pass
    
    
    def RemoveAllDescendants(self):
        """
        RemoveAllDescendants()
            Removes all the descendants under the current labelstyle node.
        """
        pass
    
    
    def RemoveChild(self):
        """
        RemoveChild(index: System.Int32)
            Removes a child label style by index from the current labelstyle node.
            index: System.Int32 - The index of the style to remove from the current labelstyle node.
        RemoveChild(labelStyleName: System.String)
            Removes a child label style by name from the current labelstyle node.
            labelStyleName: System.String - The name of the style to remove from the current labelstyle node.
        """
        pass
    
    
    def RemoveComponent(self):
        """
        RemoveComponent(name: System.String)
            Remove a component from the label style.
            name: System.String - The name of component.
        """
        pass
    
    
    def SetComponentsDrawOrder(self):
        """
        SetComponentsDrawOrder(componentIds: ObjectId)
            Sets the supported components' draw order.
            componentIds: ObjectId - The supported components' id.
        """
        pass
    
    
    def SwitchComponentsDrawOrder(self):
        """
        SwitchComponentsDrawOrder(index1: System.Int32, index2: System.Int32)
            Switch the supported components' draw order by index.
            index1: System.Int32 - The first index of the child label style under the current labelstyle node.
            index2: System.Int32 - The second index of the child label style under the current labelstyle node.
        """
        pass
    
    pass

class LabelStyleBase(object):
    """
    Base class for label style defaults.
    """
    Behavior = None
    DraggedStateComponents = None
    Label = None
    Leader = None
    PlanReadability = None
    pass

class LabelStyleBase.BaseBehavior(object):
    """
    The behavior related properties of the default label style.
    """
    InsertOption = None
    InsideCurveOption = None
    OrientationReference = None
    pass

class LabelStyleBase.BaseDraggedStateComponents(object):
    """
    The dragged state components related properties of the default label style.
    """
    BorderType = None
    BorderVisibility = None
    Color = None
    DisplayType = None
    Gap = None
    LeaderAttachment = None
    LeaderJustification = None
    Linetype = None
    Lineweight = None
    MaxTextWidth = None
    TextHeight = None
    UseBackgroundMask = None
    pass

class LabelStyleBase.BaseLabel(object):
    """
    The label related properties of the default label style.
    """
    DisplayMode = None
    Layer = None
    TextStyle = None
    Visibility = None
    pass

class LabelStyleBase.BaseLeader(object):
    """
    The leader related properties of the default label style.
    """
    ArrowheadSize = None
    ArrowheadStyle = None
    Color = None
    Linetype = None
    Lineweight = None
    Shape = None
    Visibility = None
    pass

class LabelStyleBase.BasePlanReadability(object):
    """
    The plan readability related properties of the default label style.
    """
    FlipAnchorsWithText = None
    PlanReadable = None
    PlanReadableBias = None
    pass

class LabelStyleBlockComponent(DBObject):
    """
    The lable style text component wrapper class.
    """
    Block = None
    General = None

    pass

class LabelStyleBlockComponent.StyleBlock(object):
    """
    Block style settings for label block components.
    """
    Attachment = None
    BlockHeight = None
    BlockName = None
    Color = None
    Linetype = None
    Lineweight = None
    RotationAngle = None
    XOffset = None
    YOffset = None
    pass

class LabelStyleBlockComponent.StyleGeneral(object):
    """
    General style settings for label block components.
    """
    AnchorComponent = None
    AnchorLocation = None
    AnchorPoint = None
    Name = None
    UsedIn = None
    Visible = None
    pass

class LabelStyleCollection(StyleCollectionBase):
    """
    A collection of LabelStyle objects.
    """
    DefaultLabelStyle = None
    Expressions = None
    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    
    def Remove(self):
        """
        Remove(index: System.Int32)
            Removes a label style by index from the collection.
            index: System.Int32 - The index of the label style to remove from the collection.
        Remove(styleName: System.String)
            Removes a label style by name from the collection.
            styleName: System.String - The name of the label style to remove from the collection.
        """
        pass
    
    pass

class LabelStyleComponent(DBObject):
    """
    The lable style component wrapper class.
    """


    pass

class LabelStyleComponentType():
    """
    Defines the label style components type.
    """
    pass

class LabelStyleDefault(object):
    """
    The settings class for the label style default.
    """
    Behavior = None
    Components = None
    DraggedStateComponents = None
    Label = None
    Leader = None
    PlanReadability = None
    pass

class LabelStyleDefault.DefaultBehavior(object):
    """
    The behavior related properties of the default label style settings.
    """
    InsertOption = None
    InsideCurveOption = None
    OrientationReference = None
    pass

class LabelStyleDefault.DefaultComponents(object):
    """
    The component related properties of the default label style settings.
    """
    Color = None
    Linetype = None
    Lineweight = None
    TextHeight = None
    pass

class LabelStyleDefault.DefaultDraggedStateComponents(object):
    """
    The dragged state components related properties of the default label style settings.
    """
    BorderType = None
    BorderVisibility = None
    Color = None
    DisplayType = None
    Gap = None
    LeaderAttachment = None
    LeaderJustification = None
    Linetype = None
    Lineweight = None
    MaxTextWidth = None
    TextHeight = None
    UseBackgroundMask = None
    pass

class LabelStyleDefault.DefaultLabel(object):
    """
    The label related properties of the default label style settings.
    """
    Layer = None
    TextStyle = None
    Visibility = None
    pass

class LabelStyleDefault.DefaultLeader(object):
    """
    The leader related properties of the default label style settings.
    """
    ArrowheadSize = None
    ArrowheadStyle = None
    Color = None
    Linetype = None
    Lineweight = None
    Shape = None
    Visibility = None
    pass

class LabelStyleDefault.DefaultPlanReadability(object):
    """
    The plan readability related properties of the default label style settings.
    """
    FlipAnchorsWithText = None
    PlanReadable = None
    PlanReadableBias = None
    pass

class LabelStyleDirectionArrowComponent(DBObject):
    """
    The lable style direction arrow component wrapper class.
    """
    DirectionArrow = None
    General = None

    pass

class LabelStyleDirectionArrowComponent.StyleDirectionArrow(object):
    """
    Direction arrow style settings for label direction arrow components.
    """
    ArrowheadSize = None
    ArrowheadStyle = None
    Color = None
    FixedLength = None
    LengthOrMinimumLength = None
    Linetype = None
    Lineweight = None
    RotationAngle = None
    XOffset = None
    YOffset = None
    pass

class LabelStyleDirectionArrowComponent.StyleGeneral(object):
    """
    General style settings for label direction arrow components.
    """
    AnchorComponent = None
    AnchorLocation = None
    AnchorPoint = None
    Name = None
    SpanOutsideSegments = None
    UsedIn = None
    Visible = None
    pass

class LabelStyleLineComponent(DBObject):
    """
    The lable style line component wrapper class.
    """
    General = None
    Line = None

    pass

class LabelStyleLineComponent.StyleGeneral(object):
    """
    General style settings for line labels.
    """
    EndAnchorPoint = None
    EndPointAnchorComponent = None
    EndPointAnchorPoint = None
    Name = None
    StartAnchorPoint = None
    StartPointAnchorComponent = None
    StartPointAnchorPoint = None
    UsedIn = None
    UseEndPointAnchor = None
    Visible = None
    pass

class LabelStyleLineComponent.StyleLine(object):
    """
    Line style settings for line labels.
    """
    Angle = None
    Color = None
    EndPointXOffset = None
    EndPointYOffset = None
    FixedLength = None
    Length = None
    LengthType = None
    Linetype = None
    Lineweight = None
    PercentLength = None
    StartPointXOffset = None
    StartPointYOffset = None
    pass

class LabelStyleReferenceTextComponent(DBObject):
    """
    The lable style reference text component wrapper class.
    """
    Border = None
    General = None
    Text = None

    pass

class LabelStyleReferenceTextComponent.StyleGeneral(StyleGeneral):
    """
    General style settings for label reference text components.
    """
    ReferenceTextObjectType = None
    pass

class LabelStyleTextComponent(DBObject):
    """
    Specifies the appearance and behavior of text feature labels in the drawing. Controls the appearance of the text itself.
    """
    Border = None
    General = None
    Text = None

    pass

class LabelStyleTextComponent.StyleBorder(StyleBorder):
    """
    Border style settings for label text components.
    """
    BackgroundMask = None
    BorderType = None
    Color = None
    Gap = None
    Linetype = None
    Lineweight = None
    Visible = None
    pass

class LabelStyleTextComponent.StyleGeneral(StyleGeneral):
    """
    General style settings for label text components.
    """
    AnchorComponent = None
    AnchorLocation = None
    AnchorPoint = None
    Name = None
    SpanOutsideSegments = None
    UsedIn = None
    Visible = None
    pass

class LabelStyleTextComponent.StyleText(StyleText):
    """
    Text style settings for label text components.
    """
    Angle = None
    Attachment = None
    Color = None
    Contents = None
    Height = None
    Lineweight = None
    MaxWidth = None
    XOffset = None
    YOffset = None
    pass

class LabelStyleTextForEachComponent(DBObject):
    """
    The lable style reference text component wrapper class.
    """
    Border = None
    General = None
    Text = None

    pass

class LabelStyleTextForEachComponent.StyleBorder(StyleBorder):
    """
    
    """

    pass

class LabelStyleTextForEachComponent.StyleGeneral(StyleGeneral):
    """
    General style settings for text-for-each label components.
    """
    TextForEach = None
    pass

class LabelStyleTextForEachComponent.StyleText(StyleText):
    """
    
    """
    CurveContents = None
    SpiralContents = None
    pass

class LabelStyleTickComponent(DBObject):
    """
    The lable style tick component wrapper class.
    """
    General = None
    Tick = None

    pass

class LabelStyleTickComponent.StyleGeneral(object):
    """
    General style settings for label tick components.
    """
    Name = None
    Visible = None
    pass

class LabelStyleTickComponent.StyleTick(object):
    """
    Tick style settings for label tick components.
    """
    AlignWithObject = None
    BlockHeight = None
    BlockName = None
    Color = None
    Linetype = None
    Lineweight = None
    RotationAngle = None
    pass

class LabelStyleType():
    """
    Defines the label style type.
    """
    pass

class LabelStylesAlignmentRoot(LabelStylesNode):
    """
    All Alignment-related label styles.  These styles control the label display for alignment components, such as major and minor stations, station equations, geometry points, and so on.
    """
    CantCriticalPointsLabelStyles = None
    CurveLabelStyles = None
    DesignSpeedLabelStyles = None
    GeometryPointLabelStyles = None
    LineLabelStyles = None
    MajorStationLabelStyles = None
    MinorStationLabelStyles = None
    PointOfIntersectionLabelStyles = None
    SpiralLabelStyles = None
    StationEquationLabelStyles = None
    StationOffsetLabelStyles = None
    SuperelevationCriticalPointsLabelStyles = None
    TangentIntersectionLabelStyles = None
    VerticalGeometryPointLabelStyles = None
    pass

class LabelStylesCatchmentRoot(LabelStylesNode):
    """
    LabelStylesCatchmentRoot
    """
    AreaLabelStyles = None
    FlowSegmentLabelStyles = None
    pass

class LabelStylesIntersectionRoot(LabelStylesNode):
    """
    Root for all intersection label collections.
    """
    LocationLabelStyles = None
    pass

class LabelStylesMatchLineRoot(LabelStylesNode):
    """
    All styles associated with match line labels.
    """
    LeftLabelStyles = None
    RightLabelStyles = None
    pass

class LabelStylesNode(LabelStylesAlignmentRoot):
    """
    Base class for root label style classes, such as LabelStylesAlignmentRoot.
    """
    DefaultLabelStyle = None
    pass

class LabelStylesParcelRoot(LabelStylesNode):
    """
    LabelStylesParcelRoot
    """
    AreaLabelStyles = None
    CurveLabelStyles = None
    LineLabelStyles = None
    pass

class LabelStylesPipeRoot(LabelStylesNode):
    """
    Root object for pipe label styles.
    """
    CrossProfileLabelStyles = None
    CrossSectionLabelStyles = None
    PlanProfileLabelStyles = None
    pass

class LabelStylesPointRoot(LabelStylesNode):
    """
    LabelStylesPointRoot
    """
    LabelStyles = None
    pass

class LabelStylesProfileRoot(LabelStylesNode):
    """
    LabelStylesProfileRoot
    """
    CurveLabelStyles = None
    GradeBreadLabelStyles = None
    GradeBreakLabelStyles = None
    HorizontalGeometryPointLabelStyles = None
    LineLabelStyles = None
    MajorStationLabelStyles = None
    MinorStationLabelStyles = None
    pass

class LabelStylesProfileViewRoot(LabelStylesNode):
    """
    LabelStylesProfileViewRoot
    """
    DepthLabelStyles = None
    StationElevationLabelStyles = None
    pass

class LabelStylesProjectionRoot(LabelStylesNode):
    """
    LabelStylesProjectionRoot
    """
    ProfileViewProjectionLabelStyles = None
    SectionViewProjectionLabelStyles = None
    pass

class LabelStylesRoot(LabelStylesNode):
    """
    Root object for accessing all label styles in a CivilDocument.
    """
    AlignmentLabelStyles = None
    CatchmentLabelStyles = None
    GeneralCurveLabelStyles = None
    GeneralLineLabelStyles = None
    GeneralLinkLabelStyles = None
    GeneralMarkerLabelStyles = None
    GeneralNoteLabelStyles = None
    GeneralShapeLabelStyles = None
    IntersectionLabelStyles = None
    MatchLineLabelStyles = None
    ParcelLabelStyles = None
    PipeLabelStyles = None
    PointLabelStyles = None
    ProfileLabelStyles = None
    ProfileViewLabelStyles = None
    ProjectionLabelStyles = None
    SampleLineLabelStyles = None
    SectionLabelStyles = None
    SectionViewLabelStyles = None
    StructureLabelStyles = None
    SurfaceLabelStyles = None
    ViewFrameLabelStyles = None
    def GetSurveyLabelStyles(self):
        """
        GetSurveyLabelStyles() -> LabelStylesSurveyRoot
            Gets the collection of all survey label styles.
        """
        pass
    
    pass

class LabelStylesSampleLineRoot(LabelStylesNode):
    """
    LabelStylesSampleLineRoot
    """
    LabelStyles = None
    pass

class LabelStylesSectionRoot(LabelStylesNode):
    """
    LabelStylesSectionRoot
    """
    GradeBreakLabelStyles = None
    MajorOffsetLabelStyles = None
    MinorOffsetLabelStyles = None
    SegmentLabelStyles = None
    pass

class LabelStylesSectionViewRoot(LabelStylesNode):
    """
    LabelStylesSectionViewRoot
    """
    GradeLabelStyles = None
    OffsetElevationLabelStyles = None
    pass

class LabelStylesStructureRoot(LabelStylesNode):
    """
    Root object for structure label styles.
    """
    LabelStyles = None
    pass

class LabelStylesSurfaceRoot(LabelStylesNode):
    """
    LabelStylesSurfaceRoot
    """
    ContourLabelStyles = None
    SlopeLabelStyles = None
    SpotElevationLabelStyles = None
    WatershedLabelStyles = None
    pass

class LabelStylesSurveyRoot(LabelStylesNode):
    """
    LabelStylesSurveyRoot
    """
    CurveLabelStyles = None
    FigureLabelStyles = None
    LineLabelStyles = None
    pass

class LabelStylesViewFrameRoot(LabelStylesNode):
    """
    LabelStylesViewFrameRoot
    """
    LabelStyles = None
    pass

class LinkStyle(DBObject):
    """
    Used to control the visual style of a roadway link (Link) object.
    """
    LinkDisplayStyleModel = None
    LinkDisplayStylePlan = None
    StyleType = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle that specifies such Model display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle that specifies such Plan display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection() -> DisplayStyle
            Gets the DisplayStyle that specifies such Section display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetLinkDisplayStyleModel(self):
        """
        GetLinkDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle that specifies such Model display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetLinkDisplayStylePlan(self):
        """
        GetLinkDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle that specifies such Plan display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    pass

class LinkStyleCollection(StyleCollectionBase):
    """
    A collection of LinkStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class MarkerDisplayType():
    """
    Specifies the kind of marker to use: point, custom, symbol, or vertical line.
    """
    pass

class MarkerOrientationType():
    """
    Defines how the marker is oriented, for example, to object, to world, or to view.
    """
    pass

class MarkerSizeType():
    """
    Defines how the marker is sized, for example, relative to screen, or fixed scale.
    """
    pass

class MarkerStyle(DBObject):
    """
    Sets the style of a marker. Markers are used to mark locations along Alignment objects or survey figures (SurveyFigure), and can also used to indicate interferences in pipe networks (InterferenceChecks).
    """
    MarkerDisplayStyleProfile = None
    MarkerDisplayStyleSection = None
    MarkerType = None
    def GetMarkerDisplayStyleProfile(self):
        """
        GetMarkerDisplayStyleProfile() -> DisplayStyle
            Gets the marker display style for profile views.
        """
        pass
    
    
    def GetMarkerDisplayStyleSection(self):
        """
        GetMarkerDisplayStyleSection() -> DisplayStyle
            Gets the marker display style for section views.
        """
        pass
    
    pass

class MarkerStyleBase(DBObject):
    """
    The base class for marker and point styles.
    """
    CustomMarkerStyle = None
    CustomMarkerSuperimposeStyle = None
    MarkerDisplayStyleModel = None
    MarkerDisplayStylePlan = None
    MarkerFixedScale = None
    MarkerRotationAngle = None
    MarkerSize = None
    MarkerSymbolName = None
    Orientation = None
    SizeType = None
    def GetMarkerDisplayStyleModel(self):
        """
        GetMarkerDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle property that specifies the point style marker Model display styles such as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetMarkerDisplayStylePlan(self):
        """
        GetMarkerDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle property that specifies the point style marker Plan display styles such as color, linetype, plotstyle, etc.
        """
        pass
    
    pass

class MarkerStyleCollection(StyleCollectionBase):
    """
    A collection of MarkerStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class MassHaulLineStyle(DBObject):
    """
    The view frame style wrapper class.
    """
    FreeHaulOption = None
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(type: Autodesk.Civil.MassHaulLineDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies profile display properties for the MassHaulLine component.
            type: Autodesk.Civil.MassHaulLineDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetHatchDisplayStyleProfile(self):
        """
        GetHatchDisplayStyleProfile(type: Autodesk.Civil.MassHaulLineHatchDisplayStyleType) -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that specifies profile display properties for the MassHaulLine component.
            type: Autodesk.Civil.MassHaulLineHatchDisplayStyleType - The type of HatchDisplayStyle to get.
        """
        pass
    
    pass

class MassHaulLineStyleCollection(StyleCollectionBase):
    """
    The MassHaulLineStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class MassHaulViewStyle(DBObject):
    """
    The view frame style wrapper class.
    """
    BottomAxis = None
    GraphStyle = None
    GridStyle = None
    LeftAxis = None
    MiddleAxis = None
    RightAxis = None
    TopAxis = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.MassHaulViewDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the masshual view component plan display color, layer, linetype, etc.
            type: Autodesk.Civil.MassHaulViewDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class MassHaulViewStyleCollection(StyleCollectionBase):
    """
    The MassHaulViewStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class MatchLineStyle(DBObject):
    """
    The match line style wrapper class.
    """
    LinesDisplayStylePlan = None
    MatchLineMaskDisplayStylePlan = None
    MatchLineMaskHatchDisplayStyle = None
    def GetLinesDisplayStylePlan(self):
        """
        GetLinesDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle that specifies plan display properties for the match lines.
        """
        pass
    
    
    def GetMatchLineMaskDisplayStylePlan(self):
        """
        GetMatchLineMaskDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle that specifies plan display properties for the match line mask areas.
        """
        pass
    
    
    def GetMatchLineMaskHatchDisplayStyle(self):
        """
        GetMatchLineMaskHatchDisplayStyle() -> HatchDisplayStyle
            Gets the HatchDisplayStyle that specifies the hatch pattern for the match line mask areas.
        """
        pass
    
    pass

class MatchLineStyleCollection(StyleCollectionBase):
    """
    The MatchLineStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class NetworkRuleSetStyle(DBObject):
    """
    Base class for Pipe and Structure rule sets.
    """
    RulesCount = None
    def CloneAndAddRule(self):
        """
        CloneAndAddRule(sourceRuleId: ObjectId)
            Add a copy of input source rule to rule set.
            Remarks: the source rule will not be added into current rule set, instead a copy will be added.
            OBJECTID TYPE: Autodesk.Civil.DatabaseServices.NetworkRule
            sourceRuleId: ObjectId - ObjectId of source rule. 
        """
        pass
    
    
    def GetRuleIds(self):
        """
        GetRuleIds() -> ObjectIdCollection
            Gets the objectId collection of all rules belonging to this network rule set.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.NetworkRule
        """
        pass
    
    
    def RemoveAllRules(self):
        """
        RemoveAllRules()
            Remove all the rules belonging to the rule set.
        """
        pass
    
    
    def RemoveRule(self):
        """
        RemoveRule(ruleId: ObjectId)
            Remove the specified rule from rule set.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.NetworkRule
            ruleId: ObjectId - ObjectId of rule which is to be removed. 
        """
        pass
    
    pass

class ParcelDisplayStyleType():
    """
    Defines ParcelStyle display style type.
    """
    pass

class ParcelStyle(DBObject):
    """
    The parcel style wrapper class.
    """
    AreaFillHatchDisplayStyleModel = None
    AreaFillHatchDisplayStylePlan = None
    NameTemplate = None
    ObservePatternFillDistance = None
    ParcelSegmentsMarkerStyle = None
    PatternFillDistance = None
    def GetAreaFillHatchDisplayStyleModel(self):
        """
        GetAreaFillHatchDisplayStyleModel() -> HatchDisplayStyle
            Gets the AeccDisplayStyle property that specifies, for the area fill hatch pattern, such Model display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetAreaFillHatchDisplayStylePlan(self):
        """
        GetAreaFillHatchDisplayStylePlan() -> HatchDisplayStyle
            Gets the AeccDisplayStyle property that specifies, for the area fill hatch pattern, such Plan display styles as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.ParcelDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties for the Parcel component.
            type: Autodesk.Civil.DatabaseServices.Styles.ParcelDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.ParcelDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the Parcel component.
            type: Autodesk.Civil.DatabaseServices.Styles.ParcelDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection() -> DisplayStyle
            Gets the DisplayStyle object that specifies Section display properties for the Parcel component.
        """
        pass
    
    pass

class ParcelStyleCollection(StyleCollectionBase):
    """
    The ParcelStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class PartDataSourceType():
    """
    Specifies the source type of part data.
    """
    pass

class PartFamily(DBObject):
    """
    Each Part is a member of a PartFamily containing all size variations for a given part.
    """
    BoundingShape = None
    Description = None
    Domain = None
    GUID = None
    Item = None
    PartSizeCount = None
    PartSizeFilter = None
    PartType = None
    SweptShape = None
    def AddPartSize(self):
        """
        AddPartSize(partSizeFilter: Autodesk.Civil.DatabaseServices.Styles.SizeFilterRecord) -> SizeFilterRecord
            Adds part one or more part sizes to this part family.
            partSizeFilter: Autodesk.Civil.DatabaseServices.Styles.SizeFilterRecord - Specifies the filter part size property collection to tell what part sizes to add
        """
        pass
    
    
    def RemovePartSize(self):
        """
        RemovePartSize(partSizeId: ObjectId)
            Remove a part size of given object id from this parts family.
            partSizeId: ObjectId - Specifies the object id of the part size to remove
        RemovePartSize(index: System.Int32)
            Remove a part size at given index from this parts family.
            index: System.Int32 - Specifies the index of the part size to remove
        """
        pass
    
    pass

class PartSize(DBObject):
    """
    Pipe network part size filter.
    """
    MaterialStyleId = None
    PartStyleId = None
    PayItems = None
    RulesStyleId = None
    SizeDataRecord = None
    pass

class PartsList(DBObject):
    """
    List of pipe network parts (pipes and structures) used for a particular drawing.
    """
    Item = None
    PartFamilyCount = None
    def AddPartFamilyByDescription(self):
        """
        AddPartFamilyByDescription(domain: Autodesk.Civil.DatabaseServices.DomainType, description: System.String) -> DomainType
            Adds a part family referenced by unique description of current active catalog to this parts list.
            domain: Autodesk.Civil.DatabaseServices.DomainType - Specifies the domain of the part family to add
            description: System.String - Specifies the description of the part family to add, the decription string should be unique within a given catalog
        """
        pass
    
    
    def AddPartFamilyByGuid(self):
        """
        AddPartFamilyByGuid(domain: Autodesk.Civil.DatabaseServices.DomainType, guid: System.String) -> DomainType
            Adds a part family referenced by unique GUID of current active catalog to this parts list. 
            A parts list can only hold parts from the same catalog.
            domain: Autodesk.Civil.DatabaseServices.DomainType - Specifies the domain of the part family to add
            guid: System.String - Specifies the GUID of the part family to add
        """
        pass
    
    
    def GetAvailablePartFamilies(self):
        """
        GetAvailablePartFamilies(domain: Autodesk.Civil.DatabaseServices.DomainType) -> DataPartFamily
            Gets available part families of the current active catalog.
            domain: Autodesk.Civil.DatabaseServices.DomainType - Specifies the domain type.
        """
        pass
    
    
    def GetPartFamilyIdsByDomain(self):
        """
        GetPartFamilyIdsByDomain(domain: Autodesk.Civil.DatabaseServices.DomainType) -> DomainType
            Gets the object id collection of part families of specified domain under this parts list.
            domain: Autodesk.Civil.DatabaseServices.DomainType - Specifies the part domain (Pipe or Structure)
        """
        pass
    
    
    def RemovePartFamily(self):
        """
        RemovePartFamily(partFamilyId: ObjectId)
            Remove a part family referenced by its object id from this parts list
            partFamilyId: ObjectId - Specifies the object id of the part family to delete
        RemovePartFamily(description: System.String)
            Remove a part family referenced by unique description from this parts list.
            description: System.String - Specifies the description of the part family to delete
        """
        pass
    
    pass

class PartsListCollection(StyleCollectionBase):
    """
    A collection of PartsList objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            Create a new parts list named by the input string.
            The new parts list will automatically have the null structure part.
            name: System.String - Specifies the name of the new parts list. If it's empty, a dynamically generated name will be applied.
        """
        pass
    
    pass

class PipeCenterlineType():
    """
    Specifies the method that will be used to define and draw the dimensions of the pipe centerline.
    """
    pass

class PipeCenterlineWidthType():
    """
    Specifies the centerline width type.
    """
    pass

class PipeDisplayStylePlanType():
    """
    Specifies the display style type when the pipe is displayed in plan view.
    """
    pass

class PipeDisplayStyleProfileType():
    """
    Specifies the display style type when the pipe is displayed in profile view.
    """
    pass

class PipeDisplayStyleSectionType():
    """
    Specifies the display style type when the pipe is displayed in section view.
    """
    pass

class PipeEndSizeType():
    """
    Specifies the method that will be used to define and draw the dimensions of the pipe ends.
    """
    pass

class PipeHatchStyleProfileType():
    """
    Specifies the hatch display style type when the pipe is displayed in profile view.
    """
    pass

class PipeHatchType():
    """
    Specifies which components of the pipe shape display a hatch pattern.
    """
    pass

class PipeNetworkBandStyle(DBObject):
    """
    Band style in pipe network profile views.
    """
    BandType = None
    PipeLabelStyleId = None
    PipeTickStyle = None
    StructureLabelStyleId = None
    StructureTickStyle = None
    TitleTextLabelStyleId = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.PipeNetworkDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the PipeNetwork component.
            type: Autodesk.Civil.DatabaseServices.Styles.PipeNetworkDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class PipeNetworkDisplayStyleType():
    """
    Defines ProfileViewPipeNetworkBandStyle display style type.
    """
    pass

class PipeRuleSetStyle(DBObject):
    """
    A set of rules for pipe objects.
    """


    pass

class PipeRuleSetStyleCollection(StyleCollectionBase):
    """
    A collection of PipeRuleSetStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class PipeStyle(DBObject):
    """
    Defines how a pipe appears in plan, profile, section, and 3D view.
    """
    PlanOption = None
    ProfileOption = None
    SectionCrossingHatch = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle object that defines the Model style.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(component: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStylePlanType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Plan style for the component indicated by the specified PipeDisplayStylePlanType value.
            component: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStylePlanType - The pipe display component to get.  
        """
        pass
    
    
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(component: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleProfileType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Profile style for the component indicated by the specified PipeDisplayStyleProfileType value.
            component: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleProfileType - The pipe display component to get.  
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection(component: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleSectionType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Section style for the component indicated by the specified PipeDisplayStyleSectionType value.
            component: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleSectionType - The pipe display component to get.  
        """
        pass
    
    
    def GetHatchStylePlan(self):
        """
        GetHatchStylePlan() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that defines the Plan style.
        """
        pass
    
    
    def GetHatchStyleProfile(self):
        """
        GetHatchStyleProfile(component: Autodesk.Civil.DatabaseServices.Styles.PipeHatchStyleProfileType) -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that defines the Profile style for the component indicated by the specified PipeHatchStyleProfileType value.
            component: Autodesk.Civil.DatabaseServices.Styles.PipeHatchStyleProfileType - The pipe hatch component to get.  
        """
        pass
    
    
    def GetHatchStyleSection(self):
        """
        GetHatchStyleSection() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that defines the Section style.
        """
        pass
    
    pass

class PipeStyleCollection(StyleCollectionBase):
    """
    A collection of PipeStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class PipeStyleOptionBase(PipeStylePlanOption):
    """
    Base interface for settings that define the appearance of the pipe in a 2D plan view. Used by PipeStylePlanOption and PipeStyleProfileOption.
    """
    AlignHatchToPipe = None
    EndLineSize = None
    EndLineSizePercent = None
    EndSizeOptions = None
    EndSizeType = None
    HatchOptions = None
    InnerDiameter = None
    InnerDiameterPercent = None
    OuterDiameter = None
    OuterDiameterPercent = None
    PipeToPipeEndCleanup = None
    WallSizeOptions = None
    WallSizeType = None
    pass

class PipeStylePlanOption(PipeStyleOptionBase):
    """
    Settings that define the appearance of the pipe in a 2D plan view.
    """
    CenterlineOptions = None
    CenterlineSize = None
    CenterlineSizePercent = None
    CenterlineWidthOptions = None
    pass

class PipeStyleProfileOption(PipeStyleOptionBase):
    """
    Settings that define the appearance of the pipe in a profile view.
    """
    CrossingHatch = None
    pass

class PipeUserDefinedType():
    """
    Specifies the user defined type.
    """
    pass

class PipeWallSizeType():
    """
    Specifies which components of the pipe shape display a hatch pattern.
    """
    pass

class PointCloudClassificationInfo(object):
    """
    The PointCloudClassificationInfo class.
    """
    Color = None
    LayerId = None
    Selected = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the PointCloudClassificationInfo
        """
        pass
    
    pass

class PointCloudClassificationInfoCollection(object):
    """
    The PointCloudClassificationInfoCollection class.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> PointCloudClassificationInfo
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class PointCloudPointStyle(object):
    """
    The PointCloudPointStyle class is used to specify the size, number, and color of the point cloud points.
    """
    Display3dType = None
    ElevatinoRangeCreationType = None
    ElevationRangeInterval = None
    IntensityRangeMaximum = None
    IntensityRangeMinimum = None
    NumberOfElevationRanges = None
    PointElevation = None
    PointsColorScheme = None
    RangesColorScheme = None
    ScaledColorIntensityScheme = None
    ScaleFactor = None
    SingleColor = None
    SizeInPixels = None
    pass

class PointCloudStyle(DBObject):
    """
    The class to describe point cloud object style.
    """
    ClassificationInfos = None
    PointStyle = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.PointCloudDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies Model display properties for the point cloud component.
            type: Autodesk.Civil.PointCloudDisplayStyleType
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.PointCloudDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the point cloud component.
            type: Autodesk.Civil.PointCloudDisplayStyleType
        """
        pass
    
    pass

class PointCloudStyleCollection(StyleCollectionBase):
    """
    The PointCloudStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class PointDisplay3dType():
    """
    Specifies how point elevation is displayed.
    """
    pass

class PointDisplayStyleType():
    """
    An enumeration that defines PointStyle  display style type.
    """
    pass

class PointMarkerDisplayType():
    """
    Specifies the kind of marker to use, any of: point, custom, or symbol.
    """
    pass

class PointStyle(DBObject):
    """
    The point style class.
    """
    Display3dType = None
    Elevation = None
    LabelDisplayStyleModel = None
    LabelDisplayStylePlan = None
    MarkerType = None
    ScaleFactor = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.PointDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties for the point component.
            type: Autodesk.Civil.DatabaseServices.Styles.PointDisplayStyleType
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.PointDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the point component.
            type: Autodesk.Civil.DatabaseServices.Styles.PointDisplayStyleType
        """
        pass
    
    
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile() -> DisplayStyle
            Gets the DisplayStyle object that specifies profile display properties for the point component.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection() -> DisplayStyle
            Gets the DisplayStyle object that specifies section display properties for the point component.
        """
        pass
    
    
    def GetLabelDisplayStyleModel(self):
        """
        GetLabelDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle property that specifies the PointStyle label Model display styles such as color, linetype, plotstyle, etc.
        """
        pass
    
    
    def GetLabelDisplayStylePlan(self):
        """
        GetLabelDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle property that specifies the PointStyle label Plan display styles such as color, linetype, plotstyle, etc.
        """
        pass
    
    pass

class PointStyleCollection(StyleCollectionBase):
    """
    The PointStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class PointSymbolType():
    """
    Defines the symbology of the point display.
    """
    pass

class PrecisionRangeType():
    """
    Defines range precision for some surface styles.
    """
    pass

class ProfileDataBandStyle(DBObject):
    """
    The profile data band style wrapper class.
    """
    BandType = None
    HGPLabelStyleId = None
    HGPTickStyle = None
    IncrementalDistanceLabelStyleId = None
    MajorIncrementLabelStyleId = None
    MajorIncrementTickStyle = None
    MinorIncrementLabelStyleId = None
    MinorIncrementTickStyle = None
    StationEquationLabelStyleId = None
    StationEquationTickStyle = None
    TitleTextLabelStyleId = None
    VGPLabelStyleId = None
    VGPTickStyle = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.ProfileDataDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the ProfileData component.
            type: Autodesk.Civil.DatabaseServices.Styles.ProfileDataDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class ProfileDataDisplayStyleType():
    """
    Defines ProfileDataBandStyle display style type.
    """
    pass

class ProfileDesignCheckCurveType():
    """
    Design check curve type.
    """
    pass

class ProfileDesignCheckSet(DBObject):
    """
    A collection of profile design checks, which can be applied to an alignment.
    """

    def AddDesignCheck(self):
        """
        AddDesignCheck(type: Autodesk.Civil.AlignmentDesignCheckType, name: System.String) -> AlignmentDesignCheck
            This function is just used to override the base class's function, and will be removed in MadRiver version.
            type: Autodesk.Civil.AlignmentDesignCheckType
            name: System.String
        AddDesignCheck(type: Autodesk.Civil.ProfileDesignCheckType, name: System.String) -> ProfileDesignCheck
            Add one design check into this ProfileDesignCheckSet.
            type: Autodesk.Civil.ProfileDesignCheckType - The type of design check.
            name: System.String - The name of design check.
        """
        pass
    
    
    def GetAllDesignChecks(self):
        """
        GetAllDesignChecks() -> ProfileDesignCheck
            Gets all design checks in this ProfileDesignCheckSet.
        """
        pass
    
    
    def GetCurveDesignCheckType(self):
        """
        GetCurveDesignCheckType(name: System.String) -> ProfileDesignCheckCurveType
            This function will get the curve design check type.
            name: System.String
        """
        pass
    
    
    def RemoveAllDesignCheck(self):
        """
        RemoveAllDesignCheck()
            Remove all design checks from this ProfileDesignCheckSet.
        """
        pass
    
    
    def RemoveDesignCheck(self):
        """
        RemoveDesignCheck(type: Autodesk.Civil.AlignmentDesignCheck) -> AlignmentDesignCheck
            This function is just used to override the base class's function, and will be removed in MadRiver version.
            type: Autodesk.Civil.AlignmentDesignCheck
        RemoveDesignCheck(designCheck: Autodesk.Civil.ProfileDesignCheck) -> ProfileDesignCheck
            Remove one design check from this ProfileDesignCheckSet.
            designCheck: Autodesk.Civil.ProfileDesignCheck - The design check needed to be removed.
        RemoveDesignCheck(type: Autodesk.Civil.AlignmentDesignCheckType, name: System.String) -> AlignmentDesignCheckType
            This function is just used to override the base class's function, and will be removed in MadRiver version.
            type: Autodesk.Civil.AlignmentDesignCheckType
            name: System.String
        RemoveDesignCheck(type: Autodesk.Civil.ProfileDesignCheckType, name: System.String) -> ProfileDesignCheckType
            Remove one design check from this ProfileDesignCheckSet.
            type: Autodesk.Civil.ProfileDesignCheckType - The type of design check.
            name: System.String - The name of design check.
        """
        pass
    
    
    def SetCurveDesignCheckType(self):
        """
        SetCurveDesignCheckType(name: System.String, type: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckCurveType) -> ProfileDesignCheckCurveType
            This function will set the curve design check type.
            name: System.String
            type: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckCurveType
        """
        pass
    
    pass

class ProfileDesignCheckSetCollection(StyleCollectionBase):
    """
    The AlignmentStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class ProfileDisplayStyleProfileType():
    """
    Defines ProfileStyle display style type.
    """
    pass

class ProfileLabelSetItem(BaseLabelSetItem):
    """
    Predefined label properties for profiles.
    """
    DimensionAnchorOption = None
    DimensionAnchorValue = None
    Increment = None
    StaggerLabel = None
    StaggerLineHeight1 = None
    StaggerLineHeight2 = None
    Weeding = None
    def GetLabeledAlignmentGeometryPoints(self):
        """
        GetLabeledAlignmentGeometryPoints() -> AlignmentPointType
            Gets the geometry points from the current profile label set item.
        """
        pass
    
    
    def SetLabeledAlignmentGeometryPoints(self):
        """
        SetLabeledAlignmentGeometryPoints(pointTypes: System.Collections.Generic.Dictionary) -> AlignmentPointType
            Sets the geometry points for the current profile label set item.
            pointTypes: System.Collections.Generic.Dictionary
        """
        pass
    
    pass

class ProfileLabelSetStyle(DBObject):
    """
    The profile lable set wrapper class.
    """
    Item = None
    def AddCrestCurve(self):
        """
        AddCrestCurve(labelStyleId: ObjectId)
            Creates a label set item of type profile crest curve with the given profile curve object id, adds it to the collection.
            labelStyleId: ObjectId - The object id of profile curve label style.
        """
        pass
    
    
    def AddSagCurve(self):
        """
        AddSagCurve(labelStyleId: ObjectId)
            Creates a label set item of type profile sag curve with the given profile curve object id, adds it to the collection.
            labelStyleId: ObjectId - The object id of profile curve label style.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileLabelSetItem
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class ProfileLabelSetStyleCollection(StyleCollectionBase):
    """
    The ProfileLabelStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class ProfileStyle(DBObject):
    """
    The profile style wrapper class.
    """
    ArrowHeadOption = None
    BeginPointMarkerStyle = None
    Chain3DDisplayStyleModel = None
    ChainTessellationDistance3D = None
    EndPointMarkerStyle = None
    HighPointMarkerStyle = None
    LowPointMarkerStyle = None
    ProfileMarkerDisplayStyleSection = None
    ProfileMarkerSectionViewMarkerStyle = None
    ThroughPointMarkerStyle = None
    VCompoundCurveIntersectPointMarkerStyle = None
    VCurveTangentIntersectPointMarkerStyle = None
    VIntersectionPointMarkerStyle = None
    VReverseCurveIntersectPointMarkerStyle = None
    VTangentCurveIntersectPointMarkerStyle = None
    def GetChain3DDisplayStyleModel(self):
        """
        GetChain3DDisplayStyleModel() -> DisplayStyle
            Gets the AeccDisplayStyle for 3D chain display style in model view orientation.
        """
        pass
    
    
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(type: Autodesk.Civil.DatabaseServices.Styles.ProfileDisplayStyleProfileType) -> DisplayStyle
            Gets the DisplayStyle object that specifies profile display properties for the Profile component.
            type: Autodesk.Civil.DatabaseServices.Styles.ProfileDisplayStyleProfileType
        """
        pass
    
    
    def GetProfileMarkerDisplayStyleSection(self):
        """
        GetProfileMarkerDisplayStyleSection() -> DisplayStyle
            Gets the AeccDisplayStyle for marker display style in section view orientation.
        """
        pass
    
    pass

class ProfileStyleCollection(StyleCollectionBase):
    """
    The ProfileStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class ProfileViewBandSetItem(BandSetItem):
    """
    Encapsulates a single profile view data band.
    """
    BandStyleId = None
    LabelAtEndStation = None
    LabelAtStartStation = None
    MajorInterval = None
    MinorInterval = None
    def GetHorizontalGeometryPointsOptions(self):
        """
        GetHorizontalGeometryPointsOptions() -> GeometryPointSelector
            Gets a GeometryPointSelector containing the state of all AlignmentPointTypes that need to be labeled at the data band.
        """
        pass
    
    
    def GetVerticalGeometryPointsOptions(self):
        """
        GetVerticalGeometryPointsOptions() -> GeometryPointSelector
            Gets a GeometryPointSelector containing the state of all ProfilePointType that need to be labeled at the data band.
        """
        pass
    
    
    def SetHorizontalGeometryPointsOptions(self):
        """
        SetHorizontalGeometryPointsOptions(alignmentGeometryPoints: Autodesk.Civil.GeometryPointSelector) -> GeometryPointSelector
            Sets the state of all AlignmentPointTypes that need to be labeled at the data band.
            alignmentGeometryPoints: Autodesk.Civil.GeometryPointSelector
        """
        pass
    
    
    def SetVerticalGeometryPointsOptions(self):
        """
        SetVerticalGeometryPointsOptions(alignmentVerticalGeometryPoints: Autodesk.Civil.GeometryPointSelector) -> GeometryPointSelector
            Sets the state of all ProfilePointType that need to be labeled at the data band.
            alignmentVerticalGeometryPoints: Autodesk.Civil.GeometryPointSelector
        """
        pass
    
    pass

class ProfileViewBandSetItemCollection(BandSetItemCollection):
    """
    This class represents a collection that stores all the band items for a profile view bandset style object.
    """
    Item = None
    def Add(self):
        """
        Add(database: Database, bandType: Autodesk.Civil.BandType, profileBandStyleName: System.String) -> BandType
            Creates a new profile view band set item with the given band type and name, adds it to the collection.
            database: Database - The drawing database.
            bandType: Autodesk.Civil.BandType - The profile band type, only ProfileData, HorizontalGeometry, VerticalGeometry, Superelevation, ProfileViewPipeNetwork and ProfileViewSectionalData are valid here.
            profileBandStyleName: System.String - The profile band name.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileViewBandSetItem
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class ProfileViewBandSetStyle(DBObject):
    """
    This class represents a profile view band set style object.
    """

    def GetBottomBandSetItems(self):
        """
        GetBottomBandSetItems() -> ProfileViewBandSetItemCollection
            Gets the bottom band items collection from the current bandset style.
        """
        pass
    
    
    def GetTopBandSetItems(self):
        """
        GetTopBandSetItems() -> ProfileViewBandSetItemCollection
            Gets the top band items collection from the current bandset style.
        """
        pass
    
    
    def SetBottomBandSetItems(self):
        """
        SetBottomBandSetItems(bandSetItems: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItemCollection) -> ProfileViewBandSetItemCollection
            Sets the bottom band items collection to the current bandset style.
            bandSetItems: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItemCollection
        """
        pass
    
    
    def SetTopBandSetItems(self):
        """
        SetTopBandSetItems(bandSetItems: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItemCollection) -> ProfileViewBandSetItemCollection
            Sets the top band items collection to the current bandset style.
            bandSetItems: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItemCollection
        """
        pass
    
    pass

class ProfileViewBandSetStyleCollection(StyleCollectionBase):
    """
    The ProfileViewBandSetStyleCollection wrapper class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class ProfileViewDisplayStyleType():
    """
    Defines profile view components type.
    """
    pass

class ProfileViewStyle(DBObject):
    """
    The profile view style wrapper class.
    """
    BottomAxis = None
    GraphStyle = None
    GridStyle = None
    LeftAxis = None
    RightAxis = None
    TopAxis = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.ProfileViewDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the profile view component plan display color, layer, linetype, etc.
            type: Autodesk.Civil.DatabaseServices.Styles.ProfileViewDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class ProfileViewStyleCollection(StyleCollectionBase):
    """
    The ProfileViewStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class ProjectionBlockDisplayType():
    """
    An enumeration that defines projection block display type.
    """
    pass

class ProjectionDisplayStyleProfileType():
    """
    An enumeration that defines projection display style profile type.
    """
    pass

class ProjectionDisplayStyleSectionType():
    """
    An enumeration that defines projection display style section type.
    """
    pass

class ProjectionEntityDisplayType():
    """
    An enumeration that defines projection point display type.
    This enum is only used for AutoCAD point and AutoCAD solid display options.
    """
    pass

class ProjectionProfileOptions(object):
    """
    Contains display options and styles for objects projected from a plan view onto a profile view.
    """
    AutoCAD3dPolylineBeginVertexMarkerStyleId = None
    AutoCAD3dPolylineBeginVertexMarkerStyleName = None
    AutoCAD3dPolylineEndVertexMarkerStyleId = None
    AutoCAD3dPolylineEndVertexMarkerStyleName = None
    AutoCAD3dPolylineInternalVertexMarkerStyleId = None
    AutoCAD3dPolylineInternalVertexMarkerStyleName = None
    AutoCADBlockDisplayOptions = None
    AutoCADBlockMarkerStyleId = None
    AutoCADBlockMarkerStyleName = None
    AutoCADBlockSymbolBlockId = None
    AutoCADBlockSymbolBlockName = None
    AutoCADPointDisplayOptions = None
    AutoCADPointMarkerStyleId = None
    AutoCADPointMarkerStyleName = None
    AutoCADSolidDisplayOptions = None
    AutoCADSolidMarkerStyleId = None
    AutoCADSolidMarkerStyleName = None
    MultiViewBlockDirection = None
    MultiViewBlockDisplayOptions = None
    MultiViewBlockDisplayRepresentationId = None
    MultiViewBlockDisplayRepresentationName = None
    MultiViewBlockMarkerStyleId = None
    MultiViewBlockMarkerStyleName = None
    MultiViewBlockSymbolBlockId = None
    MultiViewBlockSymbolBlockName = None
    VerticallyExaggerateBlocks = None
    VerticallyExaggerateMultiViewBlocks = None
    VerticallyExaggerateSolids = None
    pass

class ProjectionSectionOptions(object):
    """
    Contains display options and styles for objects projected from a plan view onto a section view.  
    Used by ProjectionStyle.
    """
    AutoCAD3dPolylineCrossingMarkerStyleId = None
    AutoCAD3dPolylineCrossingMarkerStyleName = None
    AutoCADBlockDisplayOptions = None
    AutoCADBlockMarkerStyleId = None
    AutoCADBlockMarkerStyleName = None
    AutoCADBlockSymbolBlockId = None
    AutoCADBlockSymbolBlockName = None
    AutoCADPointDisplayOptions = None
    AutoCADPointMarkerStyleId = None
    AutoCADPointMarkerStyleName = None
    AutoCADSolidDisplayAsTrueSection = None
    AutoCADSolidDisplayOptions = None
    AutoCADSolidMarkerStyleId = None
    AutoCADSolidMarkerStyleName = None
    MultiViewBlockDirection = None
    MultiViewBlockDisplayOptions = None
    MultiViewBlockDisplayRepresentationId = None
    MultiViewBlockDisplayRepresentationName = None
    MultiViewBlockMarkerStyleId = None
    MultiViewBlockMarkerStyleName = None
    MultiViewBlockSymbolBlockId = None
    MultiViewBlockSymbolBlockName = None
    VerticallyExaggerateBlocks = None
    VerticallyExaggerateMultiViewBlocks = None
    VerticallyExaggerateSolids = None
    pass

class ProjectionStyle(DBObject):
    """
    Contains display options and styles for objects projected from a plan view onto a section or profile view.
    """
    ProfileOptions = None
    SectionOptions = None
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(type: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleProfileType) -> DisplayStyle
            Gets the DisplayStyle object that specifies profile display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleProfileType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection(type: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleSectionType) -> DisplayStyle
            Gets the DisplayStyle object that specifies section display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleSectionType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class ProjectionStyleCollection(StyleCollectionBase):
    """
    A collection of ProjectionStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class QuantityTakeoffCriteria(DBObject):
    """
    A collection of items that define the criteria used to calculate material lists, which are
    then used ot generate quantity takeoff tables and reports.
    """
    Count = None
    Item = None
    def AddMaterial(self):
        """
        AddMaterial(materialName: System.String)
            Adds a new empty material with the default value to the list.
            materialName: System.String - The name of the material item.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all the material items from the list.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a material item from the list.
            index: System.Int32 - Specified the material item by index.
        """
        pass
    
    pass

class QuantityTakeoffCriteriaCollection(StyleCollectionBase):
    """
    The QuantityTakeoffCriteriaCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class QuantityTakeoffCriteriaData(object):
    """
    Defines additional data for material in QuantityTakeoffCriteria.
    """
    Condition = None
    ItemType = None
    Name = None
    pass

class QuantityTakeoffCriteriaItem(object):
    """
    Defines a material used to create quantity takeoff criteria (QuantityTakeoffCriteria).
    """
    Count = None
    CutFactor = None
    FillFactor = None
    Item = None
    MaterialName = None
    QuantityType = None
    ReFillFactor = None
    ShapeStyleId = None
    ShapeStyleName = None
    def AddCorridorShape(self):
        """
        AddCorridorShape(shapeName: System.String)
            Adds a new corridor shape data with the default value to the material item.
            shapeName: System.String - The name of the corridor shape.
        """
        pass
    
    
    def AddSurface(self):
        """
        AddSurface(surfaceName: System.String)
            Remove a surface data from the material item.
            surfaceName: System.String - The name of the surface.
        """
        pass
    
    
    def RemoveCorridorShape(self):
        """
        RemoveCorridorShape(shapeName: System.String)
            Remove a corridor shape data from the material item.
            shapeName: System.String - The name of the corridor shape.
        """
        pass
    
    
    def RemoveSurface(self):
        """
        RemoveSurface(surfaceName: System.String)
            Adds a new surface data with the default value to the material item.
            surfaceName: System.String - The name of the surface.
        """
        pass
    
    pass

class ReferenceTextComponentSelectedType():
    """
    
    """
    pass

class SampleLineDisplayStyleType():
    """
    Defines SampleLineStyle display style type.
    """
    pass

class SampleLineStyle(DBObject):
    """
    Specifies display properties for the sample lines used to obtain elevational information from an existing terrain model or surface.
    """

    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.SampleLineDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties for the SampleLine component.
            type: Autodesk.Civil.DatabaseServices.Styles.SampleLineDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SampleLineDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the SampleLine component.
            type: Autodesk.Civil.DatabaseServices.Styles.SampleLineDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SampleLineStyleCollection(StyleCollectionBase):
    """
    The SampleLineStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class ScaleType():
    """
    Defines how to scale the point marker.
    """
    pass

class ScalingMethodType():
    """
    Specifies the scaling method, which, in combination with the Watershed Units value, determines the point symbol size.
    """
    pass

class SchematicLineOption():
    """
    Defines HorizontalGeometryBandStyle schematic line option.
    """
    pass

class SectionDataBandStyle(DBObject):
    """
    The section data band style wrapper class.
    """
    BandType = None
    CenterlineLabelStyleId = None
    CenterlineTickStyle = None
    GradeBreaksLabelStyleId = None
    GradeBreaksTickStyle = None
    IncrementalDistanceLabelStyleId = None
    MajorIncrementLabelStyleId = None
    MajorIncrementTickStyle = None
    MinorIncrementLabelStyleId = None
    MinorIncrementTickStyle = None
    SampleLineVerticesLabelStyleId = None
    SampleLineVerticesTickStyle = None
    TitleTextLabelStyleId = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SectionDataDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the SectionData component.
            type: Autodesk.Civil.DatabaseServices.Styles.SectionDataDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SectionDataDisplayStyleType():
    """
    Defines SectionDataBandStyle display style type.
    """
    pass

class SectionDisplayStyleSectionType():
    """
    Defines SectionStyle display style type.
    """
    pass

class SectionLabelSetItem(BaseLabelSetItem):
    """
    A collection of properties used to ensure that labels associated with sections are consistent and to ensure that labels used elsewhere contain distinguishing content.
    """
    DimensionAnchorOption = None
    DimensionAnchorValue = None
    Increment = None
    StaggerLabel = None
    StaggerLineHeight1 = None
    StaggerLineHeight2 = None
    Weeding = None
    pass

class SectionLabelSetStyle(DBObject):
    """
    The section labelset  wrapper class.
    """
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionLabelSetItem
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class SectionLabelSetStyleCollection(StyleCollectionBase):
    """
    The SectionLabelStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SectionSegmentBandStyle(DBObject):
    """
    The section data band style wrapper class.
    """
    BandType = None
    SegmentLabelsTickStyle = None
    SegmentsLabelStyleId = None
    TitleTextLabelStyleId = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SectionSegmentDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the SectionalSegment component.
            type: Autodesk.Civil.DatabaseServices.Styles.SectionSegmentDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SectionSegmentDisplayStyleType():
    """
    Defines SectionSegmentBandStyle display style type.
    """
    pass

class SectionStyle(DBObject):
    """
    Specifies display characteristics and associated information for cross sections and their constituent components.
    """

    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection(type: Autodesk.Civil.DatabaseServices.Styles.SectionDisplayStyleSectionType) -> DisplayStyle
            Gets the DisplayStyle object that specifies section display properties for the Section component.
            type: Autodesk.Civil.DatabaseServices.Styles.SectionDisplayStyleSectionType
        """
        pass
    
    pass

class SectionStyleCollection(StyleCollectionBase):
    """
    The SectionStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SectionViewBandSetItem(BandSetItem):
    """
    Encapsulates a single section view data band.
    """
    BandStyleId = None
    LabelAtEndOffset = None
    LabelAtStartOffset = None
    MajorInterval = None
    MinorInterval = None
    pass

class SectionViewBandSetItemCollection(BandSetItemCollection):
    """
    The SectionViewBandSetItemCollectione wrapper class.
    """
    Item = None
    def Add(self):
        """
        Add(database: Database, bandType: Autodesk.Civil.BandType, sectionBandStyleName: System.String) -> BandType
            Creates a new section view band set item with the given band type and name, adds it to the collection, and returns a pointer to the new instance.
            database: Database - The drawing database.
            bandType: Autodesk.Civil.BandType - The section band type, only ProfileData, HorizontalGeometry, VerticalGeometry, Superelevation, ProfileViewPipeNetwork and ProfileViewSectionalData are valid here.
            sectionBandStyleName: System.String - The section band name.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionViewBandSetItem
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class SectionViewBandSetStyle(DBObject):
    """
    The SectionViewBandSetStyle wrapper class.
    """

    def GetBottomBandSetItems(self):
        """
        GetBottomBandSetItems() -> SectionViewBandSetItemCollection
            Gets the bottom band items collection from the current bandset style.
        """
        pass
    
    
    def GetTopBandSetItems(self):
        """
        GetTopBandSetItems() -> SectionViewBandSetItemCollection
            Gets the top band items collection from the current bandset style.
        """
        pass
    
    
    def SetBottomBandSetItems(self):
        """
        SetBottomBandSetItems(bandSetItems: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItemCollection) -> SectionViewBandSetItemCollection
            Sets the bottom band items collection to the current bandset style.
            bandSetItems: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItemCollection
        """
        pass
    
    
    def SetTopBandSetItems(self):
        """
        SetTopBandSetItems(bandSetItems: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItemCollection) -> SectionViewBandSetItemCollection
            Sets the top band items collection to the current bandset style.
            bandSetItems: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItemCollection
        """
        pass
    
    pass

class SectionViewBandSetStyleCollection(StyleCollectionBase):
    """
    The SectionViewBandSetStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SectionViewDisplayStyleType():
    """
    Defines section view components type.
    """
    pass

class SectionViewPlotRuleType():
    """
    Specifies whether to plot the section views by rows or columns.
    """
    pass

class SectionViewStyle(DBObject):
    """
    The section view style wrapper class.
    """
    BottomAxis = None
    CenterAxis = None
    GraphStyle = None
    GridStyle = None
    LeftAxis = None
    RightAxis = None
    TopAxis = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SectionViewDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the section view component plan display color, layer, linetype, etc.
            type: Autodesk.Civil.DatabaseServices.Styles.SectionViewDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SectionViewStyleCollection(StyleCollectionBase):
    """
    The SectionViewStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SectionalDataBandStyle(DBObject):
    """
    The section data band style wrapper class.
    """
    BandType = None
    IncrementalSectionDataLabelStyleId = None
    IncrementalSectionDataTickStyle = None
    SampleLineStationLabelStyleId = None
    SampleLineStationTickStyle = None
    TitleTextLabelStyleId = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SectionalDataDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the SectionalData component.
            type: Autodesk.Civil.DatabaseServices.Styles.SectionalDataDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SectionalDataDisplayStyleType():
    """
    Defines SectionalDataBandStyle display style type.
    """
    pass

class SegmentColumnStyle(ColumnStyle):
    """
    Specifies the advance column style obtained from the Parcel Segment table style or Alignment Segment table style.
    """

    def GetContentString(self):
        """
        GetContentString(type: Autodesk.Civil.TableSegmentDataType) -> TableSegmentDataType
            Gets the specified display content of segment column style.
            type: Autodesk.Civil.TableSegmentDataType
        """
        pass
    
    
    def GetContentStringFormatted(self):
        """
        GetContentStringFormatted(type: Autodesk.Civil.TableSegmentDataType) -> TableSegmentDataType
            Gets the specified content of segment column style with MText string.
            type: Autodesk.Civil.TableSegmentDataType
        """
        pass
    
    
    def SetContentString(self):
        """
        SetContentString(type: Autodesk.Civil.TableSegmentDataType, newVal: System.String) -> TableSegmentDataType
            Sets the specified display content of segment column style.
            type: Autodesk.Civil.TableSegmentDataType
            newVal: System.String
        """
        pass
    
    
    def SetContentStringFormatted(self):
        """
        SetContentStringFormatted(type: Autodesk.Civil.TableSegmentDataType, newVal: System.String) -> TableSegmentDataType
            Sets the specified content of segment column style with MText string.
            type: Autodesk.Civil.TableSegmentDataType
            newVal: System.String
        """
        pass
    
    pass

class ShapeDisplayStyleType():
    """
    Defines ShapeStyle display style type.
    """
    pass

class ShapeStyle(DBObject):
    """
    Used to control the visual style of various roadway shape objects.  Also used to style ProfileView ProfileHatchArea objects.  ShapeStyle objects defined for a drawing are kept in the 
    CivilDocument::Styles::ShapeStyles collection.
    """
    AreaFillHatchDisplayStyleModel = None
    AreaFillHatchDisplayStylePlan = None
    StyleType = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies profile display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection(type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies section display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetHatchDisplayStyleModel(self):
        """
        GetHatchDisplayStyleModel() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that specifies model display properties.
        """
        pass
    
    
    def GetHatchDisplayStylePlan(self):
        """
        GetHatchDisplayStylePlan() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that specifies plan display properties.
        """
        pass
    
    
    def GetHatchDisplayStyleProfile(self):
        """
        GetHatchDisplayStyleProfile() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that specifies profile display properties.
        """
        pass
    
    
    def GetHatchDisplayStyleSection(self):
        """
        GetHatchDisplayStyleSection() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that specifies section display properties.
        """
        pass
    
    pass

class ShapeStyleCollection(StyleCollectionBase):
    """
    A collection of ShapeStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SheetDisplayStyleType():
    """
    Defines SheetStyle display style type.
    """
    pass

class SheetStyle(DBObject):
    """
    The sheet plot style applied when plot by page is selected.
    """
    PageLayoutId = None
    PageMarginBottom = None
    PageMarginLeft = None
    PageMarginRight = None
    PageMarginTop = None

    pass

class SheetStyleCollection(StyleCollectionBase):
    """
    The SheetStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SizeFilterField(PartDataField):
    """
    Part size parameters from a SizeFilterRecord.
    """
    DataSource = None
    IsMultipleSelect = None
    pass

class SizeFilterRecord(object):
    """
    Lets users specify what part sizes they want to add into a part family.
    """
    Item = None
    ParamCount = None
    PartFamilyGuid = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the SizeFilterRecord
        """
        pass
    
    
    def GetParamByContextAndIndex(self):
        """
        GetParamByContextAndIndex(context: Autodesk.Civil.DatabaseServices.PartContextType, index: System.Int32) -> SizeFilterField
            Gets the catalog parameter by context and index.
            context: Autodesk.Civil.DatabaseServices.PartContextType
            index: System.Int32
        """
        pass
    
    pass

class SlopeArrowType():
    """
    Defines the head style of ArrowType
    """
    pass

class SlopePatternComponent(object):
    """
    Encapsulates the properties of slope pattern components used to make up a SlopePatternStyle.
    """
    SlopeLine = None
    SlopeLineOffset = None
    SlopeLineSymbol = None
    pass

class SlopePatternLine(object):
    """
    Defines a line used in a SlopePatternComponent.
    """
    Color = None
    Grade1 = None
    Grade2 = None
    Length = None
    LengthType = None
    Linetype = None
    LineWeight = None
    MaximumLength = None
    PercentofLength = None
    PercentofLength1 = None
    PercentofLength2 = None
    StartType = None
    pass

class SlopePatternLineOffset(object):
    """
    Defines the offset of lines in a SlopePatternComponent.
    """
    Distance = None
    MaximumDistance = None
    MinimumDistance = None
    Numberoflines = None
    OffsetType = None
    PercentofLength = None
    RadialOffsetAngle = None
    pass

class SlopePatternLineSymbol(object):
    """
    Defines the symbol used with a SlopePatternComponent.
    """
    BlockName = None
    Color = None
    Length = None
    LengthType = None
    Linetype = None
    LineWeight = None
    Numberoflines = None
    PercentofLength = None
    SymbolType = None
    WidthRatio = None
    pass

class SlopePatternStyle(DBObject):
    """
    A style that defines the pattern that represents a slope in a grading style.
    """
    Count = None
    Item = None
    MinDisplayLength = None
    PreviewFeatureLength = None
    PreviewSlope = None
    PreviewSlopeLength = None
    def AddComponent(self):
        """
        AddComponent(position: System.Int32)
            Adds a new component using the default parameters in a specified position.
            position: System.Int32 - The position of the new component in relation to existing components.
        """
        pass
    
    
    def CopyComponent(self):
        """
        CopyComponent(index: System.Int32, insertPosition: System.Int32)
            Copy a component and insert into the slope pattern style.
            Remarks: You can use the parameter- insertPosition as a index to get the component in the slope pattern style.
            index: System.Int32 - The index in the collection.
            insertPosition: System.Int32 - The position of the new component in relation to existing components.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes the component from the collection by the specified index.
            index: System.Int32 - The index in the collection.
        """
        pass
    
    pass

class SlopePatternStyleCollection(StyleCollectionBase):
    """
    The SlopePatternStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class StaggerLabelType():
    """
    Defines the grade break label stagger type.
    """
    pass

class StructureColumnComponentData(object):
    """
    Specifies the tabel cell component data information.
    """
    ComponentType = None
    Content = None
    Name = None
    pass

class StructureColumnComponents(object):
    """
    
    """
    Count = None
    Item = None
    def AddComponent(self):
        """
        AddComponent(name: System.String, componentType: Autodesk.Civil.StructureColumnComponentType) -> StructureColumnComponentType
            Adds a table cell component data to the collection with the default Content("Structure Text") and Justification(Center).
            name: System.String - The name of the table cell component data.
            componentType: Autodesk.Civil.StructureColumnComponentType - The type of the table cell component data.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all the table cell component data from the collection.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a table cell component data by index in the collection.
            index: System.Int32 - The index of the table cell component data to remove.
        RemoveAt(name: System.String)
            Removes a table cell component data by name in the collection.
            name: System.String - The name of the table cell component data.
        """
        pass
    
    
    def SwitchComponentsOrder(self):
        """
        SwitchComponentsOrder(index1: System.Int32, index2: System.Int32)
            Switch the component data order by index.
            index1: System.Int32 - The first index of the table cell component data in the collection.
            index2: System.Int32 - The second index of the table cell component data in the collection.
        """
        pass
    
    pass

class StructureColumnStyle(ColumnStyle):
    """
    Specifies the advance column style obtained from the Structure table style.
    """

    def GetComponents(self):
        """
        GetComponents() -> StructureColumnComponents
            Gets the table cell components from the structure column style.
        """
        pass
    
    
    def SetComponents(self):
        """
        SetComponents(componentDatas: Autodesk.Civil.DatabaseServices.Styles.StructureColumnComponents) -> StructureColumnComponents
            Sets the table cell components to the structure column style.
            componentDatas: Autodesk.Civil.DatabaseServices.Styles.StructureColumnComponents - The table cell components.
        """
        pass
    
    pass

class StructureDisplayStylePlanType():
    """
    Specifies the display style type when the Structure is displayed in plan view.
    """
    pass

class StructureDisplayStyleProfileType():
    """
    Specifies the display style type when the Structure is displayed in profile view.
    """
    pass

class StructureDisplayStyleSectionType():
    """
    Specifies the display style type when the Structure is displayed in section view.
    """
    pass

class StructureInsertionLocation():
    """
    Specifies the block insertion laction.
    """
    pass

class StructureModelViewOptionType():
    """
    Specifies the dimensions of the structure in model view.
    """
    pass

class StructurePlanViewType():
    """
    specifies whether the 2D plan view of the structure style is displayed as an outline of the 3D object, or as an AutoCAD block reference.
    """
    pass

class StructureRuleSetStyle(DBObject):
    """
    A set of rules for structure objects.
    """


    pass

class StructureRuleSetStyleCollection(StyleCollectionBase):
    """
    A collection of StructureRuleSetStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class StructureSimpleSolidType():
    """
    Specifies the simple shape options.
    """
    pass

class StructureSizeOptionsType():
    """
    Specifies the size options type.
    """
    pass

class StructureStyle(DBObject):
    """
    Specifies display properties for all structure objects in the drawing.
    """
    ModelOption = None
    PlanOption = None
    ProfileOption = None
    SectionOption = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel() -> DisplayStyle
            Gets the DisplayStyle object that defines the Model style.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(component: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStylePlanType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Plan style for the component indicated by the specified StructureDisplayStylePlanType value.
            component: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStylePlanType - The Structure display component to get.  
        """
        pass
    
    
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(component: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleProfileType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Profile style for the component indicated by the specified StructureDisplayStyleProfileType value.
            component: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleProfileType - The Structure display component to get.  
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection(component: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleSectionType) -> DisplayStyle
            Gets the DisplayStyle object that defines the Section style for the component indicated by the specified StructureDisplayStyleSectionType value.
            component: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleSectionType - The Structure display component to get.  
        """
        pass
    
    
    def GetHatchStylePlan(self):
        """
        GetHatchStylePlan() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that defines the Plan style.
        """
        pass
    
    
    def GetHatchStyleProfile(self):
        """
        GetHatchStyleProfile() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that defines the Profile style for the component indicated by the specified StructureHatchStyleProfileType value.
        """
        pass
    
    
    def GetHatchStyleSection(self):
        """
        GetHatchStyleSection() -> HatchDisplayStyle
            Gets the HatchDisplayStyle object that defines the Section style.
        """
        pass
    
    pass

class StructureStyleCollection(StyleCollectionBase):
    """
    A collection of StructureStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class StructureStyleModelOption(object):
    """
    Specifies the method that is used to define and draw the dimensions of the structure in model view.
    """
    ModelViewOptions = None
    SimpleSolidType = None
    pass

class StructureStyleOptionBase(StructureStyleProfileOption):
    """
    Base class for StructureStyleProfileOption and StructureStyleSectionOption.
    """
    BlockInsertLocation = None
    MaskConnectedObjects = None
    SizeType = None
    SymbolBlockName = None
    SymbolBlockXScale = None
    SymbolBlockYScale = None
    SymbolBlockZScale = None
    ViewOptions = None
    XSize = None
    XSizePercent = None
    YSize = None
    YSizePercent = None
    pass

class StructureStylePlanOption(object):
    """
    Specifies the method that is used to define and draw the dimensions of the structure in 2D plan view.
    """
    MaskConnectedObjects = None
    PlanViewOptions = None
    Size = None
    SizePercent = None
    SizeType = None
    SymbolBlockName = None
    SymbolBlockXScale = None
    SymbolBlockYScale = None
    SymbolBlockZScale = None
    pass

class StructureStyleProfileOption(StructureStyleOptionBase):
    """
    Specifies the method that is used to define and draw the dimensions of the structure in profile view.
    """

    pass

class StructureStyleSectionOption(StructureStyleOptionBase):
    """
    Specifies the method that is used to define and draw the dimensions of the structure in section view.
    """

    pass

class StructureViewType():
    """
    Specifies the method that will be used to define and draw the dimensions of the structure in profile or section view.
    """
    pass

class StyleBase(DBObject):
    """
    The base class for all style objects.
    """
    CreateBy = None
    DateCreated = None
    DateModified = None
    IsUsed = None
    ModifiedBy = None
    Name = None
    def CopyAsSibling(self):
        """
        CopyAsSibling(styleName: System.String) -> ObjectId
            Copy the current style and add it to the parent node as a sibling.
            styleName: System.String - The name of the style.
        """
        pass
    
    
    def ExportTo(self):
        """
        ExportTo(destinationDatabase: Database, conflictResolution: Autodesk.Civil.StyleConflictResolverType) -> StyleConflictResolverType
            Exports the current style to another drawing.
            destinationDatabase: Database - The destination database.
            conflictResolution: Autodesk.Civil.StyleConflictResolverType - Specifies how to resolve conflicts if the current style has the same name as a style in the destination database.
        ExportTo(styleIds: ObjectIdCollection, destinationDatabase: Database, conflictResolution: Autodesk.Civil.StyleConflictResolverType) -> StyleConflictResolverType
            Exports a collection of style ids to another drawing.
            styleIds: ObjectIdCollection - The object id collection of styles need to export.
            destinationDatabase: Database - The destination database.
            conflictResolution: Autodesk.Civil.StyleConflictResolverType - Specifies how to resolve conflicts if any exported styles have the same name as a style in the destination database.
        """
        pass
    
    pass

class StyleCollectionBase(AlignmentDesignCheckSetCollection):
    """
    The base class for all style collections.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            Creates a new style object, adds it to the collection, and returns an ObjectId for the object.
            name: System.String - 
            The name of the new style. If this string is empty or null, a dynamically generated name is created.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(item: ObjectId) -> bool
            Determines whether an element specified by ObjectId is in the collection.
            item: ObjectId
        Contains(styleName: System.String) -> bool
            Determines whether an element is in the collection by its name.
            styleName: System.String
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<ObjectId>
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(index: System.Int32)
            Removes a style by index from the collection.
            index: System.Int32 - The index of the style to remove from the collection.
        Remove(styleName: System.String)
            Removes a style by name from the collection.
            styleName: System.String - The name of the style to remove from the collection.
        Remove(style: Autodesk.Civil.DatabaseServices.Styles.StyleBase) -> StyleBase
            Removes a style by Object from the collection.
            style: Autodesk.Civil.DatabaseServices.Styles.StyleBase - The style object to remove from the collection.
        """
        pass
    
    pass

class StylesRoot(object):
    """
    The root class for accessing collections of all Civil 3D styles.
    """
    AlignmentDesignCheckSets = None
    AlignmentStyles = None
    AssemblyStyles = None
    BandStyles = None
    BuildingSiteStyles = None
    CantViewStyles = None
    CatchmentStyles = None
    CodeSetStyles = None
    CorridorStyles = None
    FeatureLineStyles = None
    GradingCriteriaSets = None
    GradingStyles = None
    GroupPlotStyles = None
    InterferenceStyles = None
    IntersectionStyles = None
    LabelSetStyles = None
    LabelStyles = None
    LinkStyles = None
    MarkerStyles = None
    MassHaulLineStyles = None
    MassHaulViewStyles = None
    MatchLineStyles = None
    ParcelStyles = None
    PartsListSet = None
    PipeRuleSetStyles = None
    PipeStyles = None
    PointCloudStyles = None
    PointStyles = None
    ProfileDesignCheckSets = None
    ProfileStyles = None
    ProfileViewBandSetStyles = None
    ProfileViewStyles = None
    ProjectionStyles = None
    QuantityTakeoffCriterias = None
    SampleLineStyles = None
    SectionStyles = None
    SectionViewBandSetStyles = None
    SectionViewStyles = None
    ShapeStyles = None
    SheetStyles = None
    SlopePatternStyles = None
    StructureRuleSetStyles = None
    StructureStyles = None
    SuperelevationViewStyles = None
    SurfaceStyles = None
    SurveyFigureStyles = None
    SurveyNetworkStyles = None
    TableStyles = None
    ViewFrameStyles = None
    pass

class SubassemblySubentityStyle(DBObject):
    """
    Base class for LinkStyle and ShapeStyle.
    """
    StyleType = None

    pass

class SubassemblySubentityStyleType():
    """
    
    """
    pass

class SuperelevationDataBandStyle(DBObject):
    """
    The super elevation data band style wrapper class.
    """
    BandType = None
    FullSuperLabelStyleId = None
    FullSuperTickStyle = None
    LevelCrownLabelStyleId = None
    LevelCrownTickStyle = None
    NormalCrownLabelStyleId = None
    NormalCrownTickStyle = None
    ReverseCrownLabelStyleId = None
    ReverseCrownTickStyle = None
    ShoulderCriticalPointsLabelStyleId = None
    ShoulderCriticalPointsTickStyle = None
    SlopeTransitionRegionLabelStyleId = None
    SlopeTransitionRegionTickStyle = None
    TitleTextLabelStyleId = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SuperelevationDataDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the SuperelevationData component.
            type: Autodesk.Civil.DatabaseServices.Styles.SuperelevationDataDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SuperelevationDataDisplayStyleType():
    """
    Defines SuperelevationDataBandStyle display style type.
    """
    pass

class SuperelevationViewStyle(DBObject):
    """
    The class to describe superelevation object style.
    """
    AxisBottomMajorTickInterval = None
    AxisTopMajorTickInterval = None
    UseFullHeightTick = None
    UseSmallTicksAtBottom = None
    UseSmallTicksAtMiddle = None
    UseSmallTicksAtTop = None
    VerticalUnitHeight = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.SuperElevationViewDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the superelevation component.
            type: Autodesk.Civil.SuperElevationViewDisplayStyleType
        """
        pass
    
    pass

class SuperelevationViewStyleCollection(StyleCollectionBase):
    """
    The SuperelevationViewStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SurfaceBaseStyle(SurfaceBoundaryStyle):
    """
    The surface base style class
    """
    DisplayMode = None
    ExaggerateElevationBy = None
    FlattenToElevationBy = None
    pass

class SurfaceBoundaryStyle(SurfaceBaseStyle):
    """
    The surface boundary style class
    """
    DatumElevation = None
    DisplayExteriorBoundaries = None
    DisplayInteriorBoundaries = None
    ProjectGridToDatum = None
    UseDatum = None
    pass

class SurfaceContourStyle(SurfaceBaseStyle):
    """
    The surface boundary style class
    """
    BaseElevationInterval = None
    DepressionTickMarkInterval = None
    DepressionTickMarkLength = None
    DisplayDepressions = None
    GroupRangeValuesBy = None
    LegendStyleId = None
    LegendStyleName = None
    MajorContourColorScheme = None
    MajorContourInterval = None
    MinorContourColorScheme = None
    MinorContourInterval = None
    NumberOfRanges = None
    RangePrecision = None
    SmoothContours = None
    SmoothingFactor = None
    SmoothingType = None
    UseColorScheme = None
    def GetContourValues(self):
        """
        GetContourValues() -> ContourValues
            Gets an array of ContourValues that represent how to render major and minor contours.
            Remarks: Since this value is initialized in UI code, this method returns an empty array the first time it is called.
        """
        pass
    
    
    def SetContourValues(self):
        """
        SetContourValues(contourValuesArray: Autodesk.Civil.DatabaseServices.Styles.ContourValues) -> ContourValues
            Set an array of ContourValues that represent how to render major and minor contours.
            Remarks: The size of array should be the same as NumberOfRanges, or else ArgumentException will be thrown.
            contourValuesArray: Autodesk.Civil.DatabaseServices.Styles.ContourValues
        """
        pass
    
    pass

class SurfaceDirectionStyle(SurfaceBaseStyle):
    """
    The surface boundary style class
    """
    ColorScheme = None
    DisplayEntityMode = None
    GroupValuesBy = None
    LegendStyleId = None
    LegendStyleName = None
    NumberOfRanges = None
    RangePrecision = None
    pass

class SurfaceDisplay3dType():
    """
    Defines how to display surface style, whether it is exaggerated, flattened, or displayed at actual elevation levels.
    """
    pass

class SurfaceDisplayStyleType():
    """
    Defines surface display style type.
    """
    pass

class SurfaceDisplayType():
    """
    Defines how surface objects are to be displayed/rendered.
    """
    pass

class SurfaceElevationStyle(SurfaceBaseStyle):
    """
    The surface boundary style class
    """
    ColorScheme = None
    CutScheme = None
    DataBandingMode = None
    DisplayEntityMode = None
    FillScheme = None
    GroupValuesBy = None
    IntervalLength = None
    LegendStyleId = None
    LegendStyleName = None
    NumberOfRanges = None
    RangePrecision = None
    pass

class SurfaceGridStyle(SurfaceBaseStyle):
    """
    The SurfaceGridStyle class.
    """
    PrimaryGridInterval = None
    PrimaryGridOrientation = None
    SecondaryGridInterval = None
    SecondaryGridOrientation = None
    UsePrimaryGrid = None
    UseSecondaryGrid = None
    pass

class SurfaceGroupValuesByType():
    """
    Defines how values are grouped.
    """
    pass

class SurfaceHatchInfo(object):
    """
    The SurfaceHatchInfo class.
    """
    PatternAngle = None
    PatternDouble = None
    PatternName = None
    PatternScale = None
    PatternScaleType = None
    PatternSpace = None
    PatternType = None
    def SetHatchPattern(self):
        """
        SetHatchPattern(patternType: HatchPatternType, patternName: System.String)
            Sets both pattern type and pattern name for surface hatch entity.
            patternType: HatchPatternType
            patternName: System.String
        """
        pass
    
    pass

class SurfacePointStyle(SurfaceBaseStyle):
    """
    The SurfacePointStyle class.
    """
    DataPointsColor = None
    DataPointsSymbol = None
    DerivedPointsColor = None
    DerivedPointsSymbol = None
    NondestructivePointsColor = None
    NondestructivePointsSymbol = None
    ScalingMethodType = None
    Units = None
    pass

class SurfaceSlopeArrowStyle(SurfaceBaseStyle):
    """
    The SurfaceSlopeArrowStyle class.
    """
    ArrowScale = None
    ArrowType = None
    ColorScheme = None
    GroupValuesBy = None
    LegendStyleId = None
    LegendStyleName = None
    NumberOfRanges = None
    RangePrecision = None
    pass

class SurfaceSlopeStyle(SurfaceBaseStyle):
    """
    The SurfaceSlopeStyle class.
    """
    ColorScheme = None
    DisplayEntityMode = None
    GroupValuesBy = None
    LegendStyleId = None
    LegendStyleName = None
    NumberOfRanges = None
    RangePrecision = None
    pass

class SurfaceStyle(DBObject):
    """
    The surface style class.
    """
    BoundaryStyle = None
    ContourStyle = None
    DirectionStyle = None
    ElevationStyle = None
    GridStyle = None
    PointStyle = None
    SlopeArrowStyle = None
    SlopeStyle = None
    TriangleStyle = None
    WatershedStyle = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the surface component Model display color, layer, linetype, etc.
            type: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the surface component Plan display color, layer, linetype, etc.
            type: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection() -> DisplayStyle
            Gets the DisplayStyle object that specifies the surface component Section display color, layer, linetype, etc.
        """
        pass
    
    pass

class SurfaceStyleCollection(StyleCollectionBase):
    """
    The SurfaceStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SurfaceTriangleStyle(SurfaceBaseStyle):
    """
    The SurfaceTriangleStyle class.
    """

    pass

class SurfaceWatershedStyle(SurfaceBaseStyle):
    """
    The SurfaceWatershedStyle class.
    """
    BoundaryPointStyle = None
    BoundarySegmentStyle = None
    DepressionStyle = None
    FlatAreaStyle = None
    LabelStyleId = None
    LabelStyleName = None
    LegendStyleId = None
    LegendStyleName = None
    MultipleDrainNotchStyle = None
    MultipleDrainStyle = None
    PointScalingMethod = None
    PointUnits = None
    pass

class SurveyElevationDisplayType():
    """
    Specifies the display mode for figure elevations in the drawing.
    """
    pass

class SurveyFigureDisplayType():
    """
    
    """
    pass

class SurveyFigureMarkerPlacementType():
    """
    Specifies the placement of additional markers.
    """
    pass

class SurveyFigureProfileDisplayType():
    """
    
    """
    pass

class SurveyFigureSectionDisplayType():
    """
    
    """
    pass

class SurveyFigureStyle(DBObject):
    """
    The survey figure style class.
    """
    AdditionalMarkerDivideFigureBy = None
    AdditionalMarkerInterval = None
    AdditionalMarkerPlacementMethod = None
    AdditionalMarkerStyleId = None
    AlignAdditionalMarkersWithFigure = None
    AlignEndpointMarkersWithFigure = None
    AlignMidpointMarkersWithFigure = None
    AlignVertexMarkersWithFigure = None
    BeginningVertexMarkerStyleId = None
    CrossingMarkerStyleId = None
    EndingVertexMarkerStyleId = None
    EndPointMarkerStyleId = None
    ExaggerateElevationBy = None
    FlattenToElevationBy = None
    InternalVertexMarkerStyleId = None
    MidpointMarkerStyleId = None
    NetworkDisplayMode = None
    PlaceAdditionalMarkerAtFigureEndPoint = None
    PlaceAdditionalMarkerAtFigureStartPoint = None
    StartPointMarkerStyleId = None
    VertexMarkerStyleId = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureDisplayType) -> DisplayStyle
            Gets the DisplayStyle object for survey figure style model view.
            displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureDisplayType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureDisplayType) -> DisplayStyle
            Gets the DisplayStyle object for survey figure style plan view.
            displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureDisplayType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleProfile(self):
        """
        GetDisplayStyleProfile(displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureProfileDisplayType) -> DisplayStyle
            Gets the DisplayStyle object for survey figure style profile view.
            displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureProfileDisplayType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStyleSection(self):
        """
        GetDisplayStyleSection(displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureSectionDisplayType) -> DisplayStyle
            Gets the DisplayStyle object for survey figure style section view.
            displayType: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureSectionDisplayType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SurveyFigureStyleCollection(StyleCollectionBase):
    """
    The SurveyStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class SurveyNetworkDisplayStyleType():
    """
    Specifies the component for survey network display type.
    """
    pass

class SurveyNetworkStyle(DBObject):
    """
    The alignment style wrapper class.
    """
    ErrorEllipseScaleFactor = None
    ExaggerateElevationBy = None
    FlattenToElevationBy = None
    KnownControlPointsMarkerStyleId = None
    NetworkDisplayMode = None
    NonControlPointsMarkerStyleId = None
    SideshotPointsMarkerStyleId = None
    ToleranceErrorPointsMarkerStyleId = None
    UnknownControlPointsMarkerStyleId = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the SurveyFigure model display components.
            type: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies the SurveyFigure plan display components.
            type: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class SurveyNetworkStyleCollection(StyleCollectionBase):
    """
    The SurveyNetworkStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class TableDisplayStyleType():
    """
    An enumeration that defines tab display style type.
    """
    pass

class TableSortingOrderType():
    """
    Specifies the table sorting order type.
    """
    pass

class TableStyle(DBObject):
    """
    Controls the display of tables.
    """
    BorderDisplayStyleModel = None
    BorderDisplayStylePlan = None
    ColumnStyles = None
    DataAreaFillDisplayStyleModel = None
    DataAreaFillDisplayStylePlan = None
    DataDividerDisplayStyleModel = None
    DataDividerDisplayStylePlan = None
    DataSeparatorDisplayStyleModel = None
    DataSeparatorDisplayStylePlan = None
    DataTextDisplayStyleModel = None
    DataTextDisplayStylePlan = None
    DataTextHeight = None
    DataTextStyle = None
    EnableWordWrapping = None
    HeaderAreaFillDisplayStyleModel = None
    HeaderAreaFillDisplayStylePlan = None
    HeaderSeparatorDisplayStyleModel = None
    HeaderSeparatorDisplayStylePlan = None
    HeaderTextDisplayStyleModel = None
    HeaderTextDisplayStylePlan = None
    HeaderTextHeight = None
    HeaderTextStyle = None
    MaintainViewOrientation = None
    RepeatHeaderInSplitTables = None
    RepeatTitleInSplitTables = None
    SortData = None
    SortingColumn = None
    SortingOrder = None
    TableType = None
    Title = None
    TitleAreaFillDisplayStyleModel = None
    TitleAreaFillDisplayStylePlan = None
    TitleJustification = None
    TitleSeparatorDisplayStyleModel = None
    TitleSeparatorDisplayStylePlan = None
    TitleTextDisplayStyleModel = None
    TitleTextDisplayStylePlan = None
    TitleTextHeight = None
    TitleTextStyle = None
    TitleUnformatted = None
    TransposeSectionViewTable = None
    def GetDisplayStyleModel(self):
        """
        GetDisplayStyleModel(type: Autodesk.Civil.DatabaseServices.Styles.TableDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies model display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.TableDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.TableDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties.
            type: Autodesk.Civil.DatabaseServices.Styles.TableDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class TableStyleCollection(StyleCollectionBase):
    """
    A collection of TableStyle objects.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class TableStyleType():
    """
    Specifies the table style type.
    """
    pass

class TableStylesRoot(object):
    """
    The root object of all Civil 3D table-related styles.
    """
    AlignmentCurveTableStyles = None
    AlignmentLineTableStyles = None
    AlignmentSegmentTableStyles = None
    AlignmentSpiralTableStyles = None
    ParcelAreaTableStyles = None
    ParcelCurveTableStyles = None
    ParcelLineTableStyles = None
    ParcelSegmentTableStyles = None
    PipeTableStyles = None
    PointTableStyles = None
    QuantityTakeoffMaterialTableStyles = None
    QuantityTakeoffTotalVolumeTableStyles = None
    SectionViewMaterialTableStyles = None
    SectionViewTotalVolumeTableStyles = None
    StructureTableStyles = None
    SurfaceContourTableStyles = None
    SurfaceDirectionTableStyles = None
    SurfaceElevationTableStyles = None
    SurfaceSlopeArrowContourTableStyles = None
    SurfaceSlopeTableStyles = None
    SurfaceUserDefinedContourTableStyles = None
    SurfaceWatershedTableStyles = None
    pass

class TextForEachComponentSelectedType():
    """
    
    """
    pass

class VerticalGeometryBandStyle(DBObject):
    """
    The vertical geometry band style wrapper class.
    """
    BandType = None
    CrestCurveLabelStyleId = None
    CrestCurveTickStyle = None
    DownhillTangentLabelStyleId = None
    DownhillTangentTickStyle = None
    LabelOnlyTangents = None
    SagCurveLabelStyleId = None
    SagCurveTickStyle = None
    TitleTextLabelStyleId = None
    UphillTangentLabelStyleId = None
    UphillTangentTickStyle = None
    def GetDisplayStylePlan(self):
        """
        GetDisplayStylePlan(type: Autodesk.Civil.DatabaseServices.Styles.VerticalGeometryDisplayStyleType) -> DisplayStyle
            Gets the DisplayStyle object that specifies plan display properties for the VerticalGeometry component.
            type: Autodesk.Civil.DatabaseServices.Styles.VerticalGeometryDisplayStyleType - The type of DisplayStyle to get.
        """
        pass
    
    pass

class VerticalGeometryDisplayStyleType():
    """
    Defines VerticalGeometryBandStyle display style type.
    """
    pass

class ViewFrameStyle(DBObject):
    """
    The view frame style wrapper class.
    """
    ViewFrameBoundaryDisplayStylePlan = None
    def GetViewFrameBoundaryDisplayStylePlan(self):
        """
        GetViewFrameBoundaryDisplayStylePlan() -> DisplayStyle
            Gets the DisplayStyle that specifies plan display properties for the extents of a view frame.
        """
        pass
    
    pass

class ViewFrameStyleCollection(StyleCollectionBase):
    """
    The ViewFrameStyleCollection class.
    """

    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            name: System.String
        """
        pass
    
    pass

class WatershedBaseStyle(WatershedDrainPointSegmentStyle):
    """
    The WatershedBaseStyle class.
    """
    Color = None
    Hatch = None
    HatchPattern = None
    LinetypeId = None
    LinetypeName = None
    UseHatching = None
    pass

class WatershedBoundaryPointStyle(WatershedBaseStyle):
    """
    The WatershedBoundaryPointStyle class.
    """

    pass

class WatershedBoundarySegmentStyle(WatershedBaseStyle):
    """
    The WatershedBoundaryPointStyle class.
    """

    pass

class WatershedDepressionStyle(WatershedBaseStyle):
    """
    The WatershedBoundaryPointStyle class.
    """

    pass

class WatershedDrainPointSegmentStyle(WatershedBaseStyle):
    """
    This class is to specify the display drain target point and segments for the watershed.
    """
    DrawDrainPoint = None
    DrawDrainSegment = None
    PointColor = None
    PointDisplayType = None
    SegmentColor = None
    SegmentLinetypeId = None
    SegmentLinetypeName = None
    pass

class WatershedDrainPointStyle(WatershedBaseStyle):
    """
    This class is to specify the display drain target points for the watershed.
    """
    DrawDrainPoint = None
    PointColor = None
    PointDisplayType = None
    pass

class WatershedDrainSegmentStyle(WatershedBaseStyle):
    """
    This class is to specify the display drain target segments for the watershed.
    """
    DrawDrainSegment = None
    SegmentColor = None
    SegmentLinetypeId = None
    SegmentLinetypeName = None
    pass

class WatershedFlatAreaStyle(WatershedBaseStyle):
    """
    The WatershedBoundaryPointStyle class.
    """

    pass

class WatershedMultipleDrainNotchStyle(WatershedBaseStyle):
    """
    The WatershedBoundaryPointStyle class.
    """

    pass

class WatershedMultipleDrainStyle(WatershedBaseStyle):
    """
    The WatershedBoundaryPointStyle class.
    """

    pass