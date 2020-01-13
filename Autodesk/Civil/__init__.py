class AccelerationUnitType():
    """
    An enumeration that describes accelleration units.
    """
    pass

class AlignmentDesignCheck(DesignCheck):
    """
    The Alignment design check class.
    """
    DesignCheckType = None
    pass

class AlignmentDesignCheckCollection(DesignCheckCollection):
    """
    The AlignmentDesignCheckCollection class.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, description: System.String, expression: System.String) -> AlignmentDesignCheck
            Adds a DesignCheck by specifying the name and expression.
            name: System.String - The name of DesignCheck.
            description: System.String - The description of DesignCheck.
            expression: System.String - The expression of DesignCheck.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all DesignChecks from the collection.
            Remarks: It will remove all corresponding DesignChecks existed in AlignmentDesignCheckSet or ProfileDesignCheckSet.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(name: System.String)
            Removes AlignmentDesignCheck from the collection by the specified name.
            Remarks: It will remove the corresponding AlignmentDesignCheck existed in AlignmentDesignCheckSet.
            name: System.String - Specifies the name of DesignCheck to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes DesignCheck from the collection by the specified index.
            Remarks: It will remove the corresponding AlignmentDesignCheck existed in AlignmentDesignCheckSet.
            index: System.Int32 - Specifies index in the collection to remove.
        """
        pass
    
    pass

class AlignmentDesignCheckRoot(object):
    """
    The AlignmentDesignCheckRoot class.
    """
    CurveDesignChecks = None
    LineDesignChecks = None
    SpiralDesignChecks = None
    SuperelevationDesignChecks = None
    TangentIntersectionDesignChecks = None
    pass

class AlignmentDesignCheckType():
    """
    Specifies the kind of alignment design check.
    """
    pass

class AlignmentDividedPivotType():
    """
    Specifies the type of divided pivot method.
    """
    pass

class AlignmentLockModeType():
    """
    An enumeration that specifies the lock mode of the Offset Alignment.
    """
    pass

class AlignmentMedianTreatmentType():
    """
    Specifies the type of median treatment.
    """
    pass

class AlignmentPointType():
    """
    Enumerates types of points on an Alignment.
    """
    pass

class AlignmentTransitionSegmentType():
    """
    Specify the segment type of linear transition used for the widening: Lines or Arcs.
    """
    pass

class AlignmentUndividedPivotType():
    """
    Specifies the type of undivided pivot method.
    """
    pass

class AlignmentUpdateModeType():
    """
    An enumeration that specifies the update mode in relationship to the parent Alignment.
    """
    pass

class AnchorLocationType():
    """
    Enumerates where to anchor various label annotations.
    """
    pass

class AnchorPointType():
    """
    Enumerates where to anchor various label annotations.
    """
    pass

class AngleFormatType():
    """
    Enumerates angle formats.
    """
    pass

class AngleUnitType():
    """
    Enumerates angle units.
    """
    pass

class AreaUnitType():
    """
    Enumerates area units.
    """
    pass

class ArrowHeadFitType():
    """
    An enumeration that defines the arrow head fit type.
    """
    pass

class ArrowHeadSizeType():
    """
    An enumeration that defines the arrow head size type.
    """
    pass

class ArrowHeadType():
    """
    An enumeration that defines the arrow head type.
    """
    pass

class AssemblyDisplayStyleType():
    """
    
    """
    pass

class AssemblyGroupNameType():
    """
    
    """
    pass

class BandLocationType():
    """
    An enumeration that specifies the position of the Band, either the top or bottom of the profile/section view.
    """
    pass

class BandType():
    """
    An enumeration that specifies the data band type.
    """
    pass

class BearingQuadrantType():
    """
    Enumerates bearing quadrant type.
    """
    pass

class BlockAttachmentType():
    """
    Enumerates how block label components are attached.
    """
    pass

class CantPivotMethodType():
    """
    Specifies the type of pivot method.
    """
    pass

class CantPointType():
    """
    Enumerates the cant critical points type that need to be labeled.
    """
    pass

class CantStationRoundingType():
    """
    Specifies the type of station rounding.
    """
    pass

class CantViewDisplayStyleType():
    """
    Specifies the cant view display style type.
    """
    pass

class CapitalizationType():
    """
    Enumerates how direction value text is capitalized.
    """
    pass

class CatchmentObjectType():
    """
    
    """
    pass

class CatchmentRainfallTravelTimeUnitType():
    """
    Specifies time units.
    """
    pass

class CatchmentShallowConcentratedFlowSurfaceType():
    """
    
    """
    pass

class CatchmentTimeOfConcentrationMethodType():
    """
    
    """
    pass

class CatchmentWatershedObjectType():
    """
    
    """
    pass

class CivilException(EntityNotFoundException):
    """
    Base class for all Civil exceptions.
    """
    def ErrorHandler(self):
        """
        ErrorHandler()
            Throws an ErrorStatus.UnknownError.
        ErrorHandler(message: System.String)
            Throws an ErrorStatus.UnknownError.
            message: System.String - 
            The error message.
        ErrorHandler(es: Autodesk.Civil.ErrorStatus) -> ErrorStatus
            Throws an ErrorStatus.UnknownError.
            es: Autodesk.Civil.ErrorStatus - 
            Error code.
        ErrorHandler(es: Autodesk.Civil.ErrorStatus, message: System.String) -> ErrorStatus
            Throws an ErrorStatus.UnknownError.
            es: Autodesk.Civil.ErrorStatus - 
            Error code.
            message: System.String - 
            Input the error message.
        """
        pass
    
    pass

class CivilVersion():
    """
    Versions of Civil 3D.
    """
    pass

class Constant(object):
    """
    Constants used by the Civil API.
    """
    pass

class CorridorAlongCurveOption():
    """
    Defines along alignment curve options.
    """
    pass

class CorridorAlongOffsetTargetCurveOption():
    """
    Defines along offset alignment target curve options.
    """
    pass

class CorridorRegionLockType():
    """
    Defines the region lock setting type.
    """
    pass

class CrossSectionShapeType():
    """
    Specifies cross section shapes.
    """
    pass

class CrossingBreaklinesElevationType():
    """
    An enumeration that specifies the elevation to use for the crossing breaklines.
    """
    pass

class CurbReturnType():
    """
    Enumerates the type of curb return used for the intersection: Chamfer, Circular Fillet, or 3-Centered Arcs.
    """
    pass

class DecimalCharacterType():
    """
    Enumerates decimal character type.
    """
    pass

class DeprecatedVersionAttribute(object):
    """
    Marks the program elements' version when they are deprecated.
    """
    Version = None
    pass

class DesignCheck(AlignmentDesignCheck):
    """
    The abstract design check class.
    """
    Description = None
    Expression = None
    Name = None
    pass

class DesignCheckCollection(AlignmentDesignCheckCollection):
    """
    
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, description: System.String, expression: System.String) -> AlignmentDesignCheck
            name: System.String
            description: System.String
            expression: System.String
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> AlignmentDesignCheck
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Remove(self):
        """
        Remove(name: System.String)
            name: System.String
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            index: System.Int32
        """
        pass
    
    pass

class DesignCheckCollection(ProfileDesignCheckCollection):
    """
    
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, description: System.String, expression: System.String) -> ProfileDesignCheck
            name: System.String
            description: System.String
            expression: System.String
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileDesignCheck
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Remove(self):
        """
        Remove(name: System.String)
            name: System.String
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            index: System.Int32
        """
        pass
    
    pass

class DesignSpeedLookupMethodType():
    """
    Specifies design speed lookup methods.
    """
    pass

class DimensionAnchorOptionType():
    """
    An enumeration that specifies the behavior of the anchor dimension.
    """
    pass

class DimensionAnchorType():
    """
    Enumerates the location of the anchor used to position dimension lines for certain profile view labels, such as vertical curve labels.
    """
    pass

class DirectionDisplayType():
    """
    Enumerates display direction.
    """
    pass

class DirectionNameDisplayType():
    """
    Specifies direction name display.
    """
    pass

class DistanceScaleFactorType():
    """
    
    """
    pass

class DrivingDirectionType():
    """
    
    """
    pass

class DropDecimalWholeType():
    """
    Specifies decimal rounding.
    """
    pass

class DropLeadingZeroType():
    """
    Specifies whether to drop leading zeros.
    """
    pass

class ElevationSourceType():
    """
    
    """
    pass

class ElevationToUseType():
    """
    An enumeration that defines the elevation to use for the crossing breaklines.
    """
    pass

class EntityNotFoundException(CivilException):
    """
    The exception that's thrown when an attempt is made to access a non-existent entity.  For example, 
    calling ProfileEntity.EntityBefore() on the first entity.
    """
    pass

class EntitySideType():
    """
    An enumeration that specifies the side of a civil entity.
    """
    pass

class ErrorStatus():
    """
    
    """
    pass

class ErrorStatusText(object):
    """
    
    """
    Text = None
    pass

class ExportDetermineElevationType():
    """
    An enumeration that specifies how the elevations of the DEM file are determined from the exported surface.
    """
    pass

class FeatureLineConnectDirectionType():
    """
    An enumeration that specifies connection direction of feature line.
    """
    pass

class FeatureLineLayerSettingType():
    """
    Defines the layer setting type.
    """
    pass

class FeatureLineLayerType():
    """
    
    """
    pass

class FeatureLinePointType():
    """
    
    """
    pass

class FlowUnitType():
    """
    Enumerates flow units.
    """
    pass

class FreeHaulDisplayType():
    """
    An enumeration that defines how to show the free haul in the graph.
    """
    pass

class GeometryPointLabelOption(object):
    """
    This class controls the selection state of a point type. The class is implemented as a generic that can be parameterized on the point type to manage.
    """
    PointType = None
    Selected = None
    pass

class GeometryPointSelector(object):
    """
    This class encapsulates the functionality to allow selecting and un-selecting point types.
    """
    Item = None
    def SelectAll(self):
        """
        SelectAll()
            Selects all supported geometry points.
        """
        pass
    
    
    def UnSelectAll(self):
        """
        UnSelectAll()
            Unselects all supported geometry points.
        """
        pass
    
    pass

class GradeFormatType():
    """
    Enumerates grade formats.
    """
    pass

class GradeSlopeFormatType():
    """
    Enumerates grade slope formats.
    """
    pass

class GradingDistanceProjectionType():
    """
    An enumeration that defines the type of projection for the Distance target.
    """
    pass

class GradingElevationProjectionType():
    """
    An enumeration that defines the type of projection for the Elevation target.
    """
    pass

class GradingInteriorCornerOverlapSolutionType():
    """
    An enumeration that defines how interior corner projections are cleaned up when the footprint corner has different elevations.
    """
    pass

class GradingRelativeElevationProjectionType():
    """
    An enumeration that defines the type of projection for the Relative Elevation target.
    """
    pass

class GradingSearchOrderType():
    """
    An enumeration that defines the secarch order for the grading.
    """
    pass

class GradingSlopeFormatType():
    """
    An enumeration that defines the target method for the grading
    """
    pass

class GradingSurfaceProjectionType():
    """
    An enumeration that defines the type of projection for the Surface target.
    """
    pass

class GradingTargetType():
    """
    An enumeration that defines the target method for the grading
    """
    pass

class HighSideShoulderMethodType():
    """
    Specifies shoulder methods in high side.
    """
    pass

class HighsideLocationType():
    """
    Specifies whether to drop leading zeros.
    """
    pass

class IProperty():
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    pass

class ImpliedPointOfIntersectionDisplayType():
    """
    Specifies implied point of intersection display methods.
    """
    pass

class InternalC3DPipesToStmMigration(object):
    """
    
    """
    def Migrate(self):
        """
        Migrate(pDwgDb: Database, stmFileName: System.String, pipeNetworkIds: ObjectIdCollection) -> bool
            pDwgDb: Database
            stmFileName: System.String
            pipeNetworkIds: ObjectIdCollection
        Migrate(pDwgDb: Database, stmFileName: System.String, selectedNames: System.Collections.Generic.List) -> bool
            pDwgDb: Database
            stmFileName: System.String
            selectedNames: System.Collections.Generic.List
        """
        pass
    
    pass

class KrigingSemivariogramType():
    """
    An enumeration that specifies mivariogram model for smoothing a surface using Kriging method.
    """
    pass

class LabelContentDisplayType():
    """
    Defines label content display type after it is dragged from its default position.
    """
    pass

class LabelInsertionType():
    """
    Enumerates label insertion.
    """
    pass

class LabelInsideCurveType():
    """
    Defines labels place type, inside or outside a curve.
    """
    pass

class LabelMaskType():
    """
    An enumeration that specifies the behavior of a label's background mask.
    """
    pass

class LabelRotationType():
    """
    An enumeration that specifies the label rotation type.
    """
    pass

class LabelStyleLengthType():
    """
    An enumeration that specifies how to define the length of the label line component.
    """
    pass

class LabelTextAttachmentType():
    """
    Enumerates label text attachment location.
    """
    pass

class LabelingPromptType():
    """
    Enumerates labeling prompts.
    """
    pass

class LandXMLImportAlignmentType():
    """
    Enumerates landXML import alignment type.
    """
    pass

class LatLongDirectionType():
    """
    Enumerates latitude / longitude direction.
    """
    pass

class LayoutModeType():
    """
    Enumerates layout mode.
    """
    pass

class LeaderAttachmentBehaviorType():
    """
    An enumeration that specifies the attachment behavior of the leader.
    """
    pass

class LeaderAttachmentType():
    """
    Enumerates leader attachment location.
    """
    pass

class LeaderShapeType():
    """
    Defines the leader shape type.
    """
    pass

class LeaderTailVisibilityType():
    """
    An enumeration that specifies the behavior of the leader tail visibility.
    """
    pass

class LeaderVisibilityType():
    """
    An enumeration that specifies the behavior of the leader visibility.
    """
    pass

class LinearUnitType():
    """
    Enumerates linear units.
    """
    pass

class LinkCreationType():
    """
    An enumeration that defines the link creation type.
    """
    pass

class LowSideShoulderMethodType():
    """
    Specifies shoulder methods in low side.
    """
    pass

class MassHaulLineDisplayStyleType():
    """
    An enumeration that defines MassHaulLineStye display style type.
    """
    pass

class MassHaulLineHatchDisplayStyleType():
    """
    An enumeration that defines MassHaulLineStye hatch display style type.
    """
    pass

class MassHaulViewDisplayStyleType():
    """
    An enumeration that defines masshaul view components type.
    """
    pass

class MatchLineLabelLocationType():
    """
    
    """
    pass

class NetworkDefaultLayoutCommandType():
    """
    
    """
    pass

class OrientationReferenceType():
    """
    Enumerates orientation reference.
    """
    pass

class ParcelAnalysisType():
    """
    
    """
    pass

class ParcelRemainderDistributionType():
    """
    Defines the parcel remainder distribution type.
    """
    pass

class ParcelSelectionType():
    """
    Defines the parcel selection type.
    """
    pass

class ParcelSolutionType():
    """
    Defines the parcel solution type.
    """
    pass

class PipeNetworkPartDisplayType():
    """
    
    """
    pass

class PipeSectionLabelPlacementType():
    """
    
    """
    pass

class PlacementOptionType():
    """
    An enumeration that specifies the placement option type.
    """
    pass

class PlanViewAlignType():
    """
    
    """
    pass

class PlottedUnitDisplayType():
    """
    Enumerates plotted units.
    """
    pass

class PointCloudDefaultFileExtensionType():
    """
    Defines the default file extension type of point cloud.
    """
    pass

class PointCloudDisplayStyleType():
    """
    Specifies the point cloud display style type.
    """
    pass

class PointCloudElevationRangeCreationType():
    """
    Defines the method to create the number of elevation ranges.
    """
    pass

class PointCloudRangeColorSchemeType():
    """
    Defines color scheme type.
    """
    pass

class PointCloudRegionType():
    """
    Defines the region which points are added to.
    """
    pass

class PointCloudSurfaceType():
    """
    Defines the type of surface which points are added to.
    """
    pass

class PointCouldColorSchemeType():
    """
    Defines the Color Type of points.
    """
    pass

class PointFileFormatType():
    """
    An enumeration that specifies the point file format type.
    """
    pass

class PointNamesExistType():
    """
    Specifies how to resolve existing point names on import.
    """
    pass

class PointNotOnEntityException(CivilException):
    """
    The exception that is thrown when there is an attempt to use point coordinates that do not exist.
    For example, calling Alignment.PointLocation() for a negative station number.
    """
    pass

class PointNumbersAssignedType():
    """
    Specifies how to assign point numbers.
    """
    pass

class PointNumbersExistType():
    """
    Specifies how to resolve conflicting point numbers.
    """
    pass

class PointNumbersSuppliedType():
    """
    Specifies how to number supplied point numbers.
    """
    pass

class PressureUnitType():
    """
    Enumerates pressure units.
    """
    pass

class ProfileApplyCurveType():
    """
    
    """
    pass

class ProfileCircularVerticalConstraintType():
    """
    
    """
    pass

class ProfileCurveType():
    """
    
    """
    pass

class ProfileDesignCheck(DesignCheck):
    """
    The Profile design check class.
    """
    DesignCheckType = None
    pass

class ProfileDesignCheckCollection(DesignCheckCollection):
    """
    The ProfileDesignCheckCollection class.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, description: System.String, expression: System.String) -> ProfileDesignCheck
            Adds a DesignCheck by specifying the name and expression.
            name: System.String - The name of DesignCheck.
            description: System.String - The description of DesignCheck.
            expression: System.String - The expression of DesignCheck.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all DesignChecks from the collection.
            Remarks: It will remove all corresponding DesignChecks existed in ProfileDesignCheckSet or ProfileDesignCheckSet.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(name: System.String)
            Removes ProfileDesignCheck from the collection by the specified name.
            Remarks: It will remove the corresponding ProfileDesignCheck existed in ProfileDesignCheckSet.
            name: System.String - Specifies the name of DesignCheck to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes DesignCheck from the collection by the specified index.
            Remarks: It will remove the corresponding ProfileDesignCheck existed in ProfileDesignCheckSet.
            index: System.Int32 - Specifies index in the collection to remove.
        """
        pass
    
    pass

class ProfileDesignCheckRoot(object):
    """
    The ProfileDesignCheckRoot class.
    """
    CurveDesignChecks = None
    LineDesignChecks = None
    pass

class ProfileDesignCheckType():
    """
    Specifies the kind of Profile design check.
    """
    pass

class ProfileParabolicVerticalConstraintType():
    """
    
    """
    pass

class ProfilePointType():
    """
    Enumerates types of points on a Profile.
    """
    pass

class ProfileViewDatumType():
    """
    
    """
    pass

class ProfileViewPlotType():
    """
    
    """
    pass

class ProfileViewSplitDatumType():
    """
    
    """
    pass

class ProfileViewSplitStationType():
    """
    
    """
    pass

class ProfileViewStartCornerType():
    """
    
    """
    pass

class ProjecitonPercentageType():
    """
    An enumeration that specifies the projection pertentage type.
    """
    pass

class ProjecitonRule():
    """
    An enumeration that specifies the projection rule type.
    """
    pass

class ProjectionUtil(object):
    """
    
    """
    def IsProfileProjectionObject(self):
        """
        IsProfileProjectionObject(projectionId: ObjectId, gsMarker: System.IntPtr) -> bool
            projectionId: ObjectId
            gsMarker: System.IntPtr
        """
        pass
    
    
    def IsSectionProjectionObject(self):
        """
        IsSectionProjectionObject(projectionId: ObjectId, gsMarker: System.IntPtr) -> bool
            projectionId: ObjectId
            gsMarker: System.IntPtr
        """
        pass
    
    pass

class Property(PropertyColor):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class Property(PropertyObjectId):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class Property(PropertyFeatureLineStylePriority):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class Property(PropertyString):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class Property(PropertyBoolean):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class Property(PropertyDouble):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class Property(PropertyAnchorPoint):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class Property(PropertyUInt):
    """
    
    """
    IsOverridable = None
    Locked = None
    Overridden = None
    Value = None
    def InternalGetValue(self):
        """
        InternalGetValue() -> Object
        """
        pass
    
    
    def InternalSetValue(self):
        """
        InternalSetValue(newValue: System.Object)
            newValue: System.Object
        """
        pass
    
    pass

class PropertyAnchorPoint(Property):
    """
    Property template for label anchor location.
    """
    Value = None

    pass

class PropertyAngle(Property):
    """
    Angle property template.
    """
    Value = None

    pass

class PropertyArrowhead(Property):
    """
    Property class for arrowheads.
    """
    Value = None

    pass

class PropertyBlock(Property):
    """
    Encapsulates a Block name.
    """
    Value = None

    pass

class PropertyBoolean(Property):
    """
    Encapsulates a boolean value.
    """


    pass

class PropertyColor(Property):
    """
    Color property.
    """


    pass

class PropertyDouble(Property):
    """
    Double property template.
    """


    pass

class PropertyEnum(Property):
    """
    Property template for enumerations.
    """
    Value = None

    pass

class PropertyExpression(Property):
    """
    Expression property template.
    """
    Value = None

    pass

class PropertyFeatureLineStylePriority(Property):
    """
    Feature Line Style Priority property.
    """
    Value = None

    pass

class PropertyInt(Property):
    """
    Integer property template.
    """


    pass

class PropertyLayer(Property):
    """
    Layer property template.
    """
    Value = None

    pass

class PropertyLinetype(Property):
    """
    Line type property template.
    """
    Value = None

    pass

class PropertyMText(Property):
    """
    MText property template, used to store those properties need to be formatted.
    """
    Value = None

    pass

class PropertyMaterial(Property):
    """
    Material property template.
    """
    Value = None

    pass

class PropertyNameTemplate(Property):
    """
    NameTemplate property template.
    """
    Value = None

    pass

class PropertyObjectId(Property):
    """
    ObjectId property template.
    """
    Value = None

    pass

class PropertyObjectName(Property):
    """
    Object name property template.
    """
    Value = None

    pass

class PropertyString(Property):
    """
    String property template.
    """
    Value = None

    pass

class PropertyTextStyle(Property):
    """
    Text style property template.
    """
    Value = None

    pass

class PropertyUInt(Property):
    """
    Unsigned Integer property template.
    """


    pass

class QuantityTakeoffLengthComputeType():
    """
    An enumeration that specifies the length computation type in the take off process.
    """
    pass

class QuantityTakeoffPipeLengthType():
    """
    An enumeration that specifies the pipe length type in the take off process.
    """
    pass

class QuantityTakeoffReportExtentType():
    """
    An enumeration that specifies the extents used when finding entities to participate in the take off process.
    """
    pass

class QuantityTakeoffReportType():
    """
    An enumeration that specifies the quantity takeoff report type.
    """
    pass

class ROWCleanupType():
    """
    Specifies ROW cleanup.
    """
    pass

class RadiusLookupMethodType():
    """
    
    """
    pass

class RailAlignmentPivotType():
    """
    Specifies which rail is the Pivot
    """
    pass

class RoadwaySideType():
    """
    An enumeration that defines the roadway side type.
    """
    pass

class RotationDirType():
    """
    Specifies rotation direction.
    """
    pass

class RoundingType():
    """
    Enumerates rounding.
    """
    pass

class SectionViewElevationRangeType():
    """
    Specifies section view elevation ranges.
    """
    pass

class SheetCreateType():
    """
    
    """
    pass

class SheetSetType():
    """
    
    """
    pass

class ShoulderMethodType():
    """
    Specifies shoulder methods.
    """
    pass

class SignType():
    """
    Enumerates signs.
    """
    pass

class SlopeFormatType():
    """
    Enumerates slope formats.
    """
    pass

class SlopePatternLengthType():
    """
    An enumeration that defines the slope pattern length type.
    """
    pass

class SlopePatternOffsetType():
    """
    An enumeration that defines the slope pattern offset type.
    """
    pass

class SlopePatternStartType():
    """
    An enumeration that defines the slope pattern start type.
    """
    pass

class SlopePatternSymbolType():
    """
    An enumeration that defines the slope pattern symbol type.
    """
    pass

class SpeedUnitType():
    """
    Enumerates speed units.
    """
    pass

class SpiralType():
    """
    An enumeration that defines the sprial types.
    """
    pass

class StationDelimiterCharacterType():
    """
    Enumerates station delimeter characters.
    """
    pass

class StationDelimiterPositionType():
    """
    Enumerates station position.
    """
    pass

class StationFormatType():
    """
    Enumerates station format.
    """
    pass

class StructureColumnComponentType():
    """
    An enumeration that specifies the structure table cell component type.
    """
    pass

class StructureProfileLabelPlacementType():
    """
    
    """
    pass

class StyleConflictResolverType():
    """
    Specifies how to resolve conflicts (the same name for an existing style and a new imported style) when exporting styles to another drawing using StyleBase::ExportTo().
    """
    pass

class SubassemblyNameType():
    """
    
    """
    pass

class SuperElevationViewDisplayStyleType():
    """
    Specifies the superelevation view display style type.
    """
    pass

class SuperelevationAttainmentRegionType():
    """
    An enumeration that specifies the attachment region type of a SuperElevationCriticalStation.
    """
    pass

class SuperelevationCorridorType():
    """
    Specifies superelevation corridor types.
    """
    pass

class SuperelevationCriticalStationType():
    """
    An enumeration that specifies the type of a Superelevation critical station.
    """
    pass

class SuperelevationCrossSegmentType():
    """
    An enumeration that specifies the type of a Superelevation cross segment.
    """
    pass

class SuperelevationPointType():
    """
    Enumerates the superelevation critical points type that need to be labeled.
    """
    pass

class SuperelevationStationRoundingType():
    """
    
    """
    pass

class SuperelevationTransitionRegionType():
    """
    An enumeration that specifies the transition type to which a SuperElevationCriticalStation is bound.
    """
    pass

class SurfaceBoundaryType():
    """
    Defines the boundary type.
    """
    pass

class SurfaceBreaklineType():
    """
    An enumeration that specifies the type of the breakline.
    """
    pass

class SurfaceDrawObjectType():
    """
    An enumeration that specifies the object type that the surface points data are created from in the SurfaceOperationAddDrawingObject operation.
    """
    pass

class SurfaceException(CivilException):
    """
    This class hanle the exception for any operation on the surface.
    """
    pass

class SurfaceExtractionSettingsType():
    """
    Specifies the style of extracted entities when extract surface objects like Border, Watershed and Contour.
    """
    pass

class SurfaceOpeartionStatusType():
    """
    An enumeration that specifies the current status of the surface operation with specified type.
    """
    pass

class SurfacePointOutputLocationsType():
    """
    An enumeration that specifies the type of output location for the points.
    """
    pass

class SurfacePointSelectionType():
    """
    An enumeration that specifies the type of selecting points to use for the surface smoothing extrapolation.
    """
    pass

class SurfaceRegionOptionsType():
    """
    
    """
    pass

class SurfaceSimplifyType():
    """
    
    """
    pass

class SurfaceSmoothType():
    """
    An enumeration that specifies the type of surface smoothing.
    """
    pass

class SurfaceStatus():
    """
    
    """
    pass

class SurfaceStatusText(object):
    """
    
    """
    Text = None
    pass

class SurfaceSurveyQueryType():
    """
    An enumeration that specifies the type of a survey query operation for a surface.
    """
    pass

class SurfaceType():
    """
    
    """
    pass

class SurveyException(CivilException):
    """
    This class hanle the exception for any operation on the survey.
    """
    pass

class SurveyProject(object):
    """
    Survey project class.
    """
    ProjectGUID = None
    ProjectName = None
    def Close(self):
        """
        Close()
            Close this survey project
        """
        pass
    
    
    def GetSurveyQueryCollection(self):
        """
        GetSurveyQueryCollection() -> SurveyQueryCollection
            Gets the query collection for this survey project.
        """
        pass
    
    
    def IsOpen(self):
        """
        IsOpen() -> bool
            returns true if this survey project is opened, else return false
        """
        pass
    
    
    def Open(self):
        """
        Open(openMode: System.Boolean)
            Open this survey project for write or read only
            openMode: System.Boolean - open for write or not
        """
        pass
    
    pass

class SurveyProjectCollection(object):
    """
    This class encapsulates the read-only collection for projects. 
    From this class, you can get the current survey project or find a specific survey project
    """
    Count = None
    Item = None
    WorkingFolder = None
    def GetCurrentProject(self):
        """
        GetCurrentProject() -> SurveyProject
            Gets the current survey project.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> SurveyProject
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumertor which can be used to enumerate this collection.
        """
        pass
    
    
    def GetItem(self):
        """
        GetItem(surveyProjectGuid: System.Guid) -> SurveyProject
            Find the survey project for the specified project GUID.
            surveyProjectGuid: System.Guid
        GetItem(surveyProjectPath: System.String) -> SurveyProject
            Finds the survey project for the specified project path.
            surveyProjectPath: System.String
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumertor which can be use to enumerate this collection.
        """
        pass
    
    pass

class SurveyQuery(object):
    """
    This class represents outer data about a query -- its name, 
    description, and GUID.
    """
    Description = None
    GUID = None
    Name = None
    pass

class SurveyQueryCollection(object):
    """
    This class is to encapsulate the read only collection for MetaQuery
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SurveyQuery
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetItem(self):
        """
        GetItem(queryGuid: System.Guid) -> SurveyQuery
            Find the meta query for the specified query guid.
            queryGuid: System.Guid
        GetItem(queryName: System.String) -> ArrayList
            Find the meta query list for the specified query name.
            queryName: System.String
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    pass

class SurveyStatus():
    """
    
    """
    pass

class SurveyStatusText(object):
    """
    
    """
    Text = None
    pass

class SweptCurveLocation():
    """
    An enumeration that specifies the loction where the swept curve created.
    """
    pass

class TableSegmentDataType():
    """
    Defines the type of content in a table column.
    """
    pass

class TableTitleDirectionType():
    """
    
    """
    pass

class TaperInputType():
    """
    An enumeration that specifies the taper input type of a Linear transition.
    """
    pass

class TextBorderType():
    """
    Enumerates text border types.
    """
    pass

class TextJustificationType():
    """
    Enumerates text justification.
    """
    pass

class TimeUnitType():
    """
    Enumerates time units.
    """
    pass

class TransitionInputType():
    """
    Enumerates the type of linear transition used for the widening: By Length or By Taper Ratio.
    """
    pass

class TransitionType():
    """
    Enumerates the type of transition used for the widening: Linear, Curve-Line-Curve, Curve-Curve -Reverse Curve, or Curve - Reverse Curve.
    """
    pass

class Utility(object):
    """
    
    """
    def PolarPoint(self):
        """
        PolarPoint(refPoint: Point3d, angle: System.Double, distance: System.Double) -> Point3d
            refPoint: Point3d
            angle: System.Double
            distance: System.Double
        PolarPoint(refPoint: System.Double, angle: System.Double, distance: System.Double) -> double[]
            Finds a point by means of polar coordinates.
            refPoint: System.Double - 
            Initial three-dimensional reference point.
            angle: System.Double - 
            Angle of the resulting point from the initial point.
            distance: System.Double - 
            Distance of the resulting point from the initial point.
        """
        pass
    
    pass

class VectorMeasurementType():
    """
    Enumerates vector measurment.
    """
    pass

class ViewFrameAngleType():
    """
    
    """
    pass

class ViewFrameLabelLocationType():
    """
    
    """
    pass

class VolumeSurfaceType():
    """
    
    """
    pass

class VolumeUnitType():
    """
    Enumerates volume units.
    """
    pass

class WaterdropObjectType():
    """
    
    """
    pass

class WatershedType():
    """
    An enumeration that specifies the watershed type.
    """
    pass

class Waypoint(object):
    """
    
    """
    def addAttribute(self):
        """
        addAttribute(name: System.String, value: System.String, fullName: System.Boolean)
            name: System.String
            value: System.String
            fullName: System.Boolean
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the Waypoint
        """
        pass
    
    
    def reached(self):
        """
        reached()
        """
        pass
    
    pass

class WideningByMethod():
    """
    
    """
    pass

class WideningSide():
    """
    An enumeration that specifies the side of aligment where the auto widening created.
    """
    pass