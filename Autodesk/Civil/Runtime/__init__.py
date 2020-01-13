class CorridorError():
    """
    Corridor error types.
    """
    pass

class CorridorErrorLevel():
    """
    Error severity levels for Corridors.
    """
    pass

class CorridorLayoutModeDisplay():
    """
    Layout modes for subassemblies.
    """
    pass

class CorridorMode():
    """
    Roadway mode (design or layout).
    """
    pass

class CorridorState(RuntimeState):
    """
    Contains a wide array of information about a corridor and methods for determining locations relative 
    to the corridor. Used in the creation of custom subassemblies.
    """
    CurrentAlignmentId = None
    CurrentAlignmentIsOffsetAlignment = None
    CurrentAssemblyElevation = None
    CurrentAssemblyFixedElevation = None
    CurrentAssemblyFixedOffset = None
    CurrentAssemblyId = None
    CurrentAssemblyName = None
    CurrentAssemblyOffset = None
    CurrentAssemblyOffsetIsFixed = None
    CurrentBaselineId = None
    CurrentCorridorId = None
    CurrentCorridorName = None
    CurrentElevation = None
    CurrentOffset = None
    CurrentProfileId = None
    CurrentRegionEndStation = None
    CurrentRegionStartStation = None
    CurrentStation = None
    CurrentSubassemblyElevation = None
    CurrentSubassemblyId = None
    CurrentSubassemblyName = None
    CurrentSubassemblyOffset = None
    LayoutModeDisplayType = None
    Links = None
    Mode = None
    ParamsAlignment = None
    ParamsAlignmentGlobal = None
    ParamsBool = None
    ParamsBoolGlobal = None
    ParamsDouble = None
    ParamsDoubleGlobal = None
    ParamsElevationTarget = None
    ParamsElevationTargetGlobal = None
    ParamsLong = None
    ParamsLongGlobal = None
    ParamsOffsetTarget = None
    ParamsOffsetTargetGlobal = None
    ParamsPoint = None
    ParamsPointGlobal = None
    ParamsProfile = None
    ParamsProfileGlobal = None
    ParamsString = None
    ParamsStringGlobal = None
    ParamsSurface = None
    ParamsSurfaceGlobal = None
    Points = None
    ResourceString = None
    Shapes = None
    def IntersectAlignment(self):
        """
        IntersectAlignment(targetAlignmentId: ObjectId, alignmentId: ObjectId, origin: Autodesk.Civil.DatabaseServices.IPoint, lookRight: System.Boolean) -> IPoint
            Intersects a ray with an alignment, with no maximum distance specified.
            targetAlignmentId: ObjectId - Intersect with this alignment.
            alignmentId: ObjectId - Project the ray perpendicular to this alignment.
            origin: Autodesk.Civil.DatabaseServices.IPoint - Origin of the intersection ray.
            lookRight: System.Boolean - Project the ray to the right if true, to the left if false.
        IntersectAlignment(targetAlignmentId: ObjectId, alignmentId: ObjectId, origin: Autodesk.Civil.DatabaseServices.IPoint, lookRight: System.Boolean, maxDistance: System.Double) -> IPoint
            Intersects a ray with an alignment.
            targetAlignmentId: ObjectId - Intersect with this alignment.
            alignmentId: ObjectId - Project the ray perpendicular to this alignment.
            origin: Autodesk.Civil.DatabaseServices.IPoint - Origin of the intersection ray.
            lookRight: System.Boolean - Project the ray to the right if true, to the left if false.
            maxDistance: System.Double - Maximum distance to project the ray.
        """
        pass
    
    
    def IntersectLink(self):
        """
        IntersectLink(origin: Autodesk.Civil.DatabaseServices.IPoint, lookRight: System.Boolean, slope: System.Double, linkCode: System.String) -> IPoint
            Intersects a ray with an assembly's links.
            origin: Autodesk.Civil.DatabaseServices.IPoint - Origin of the intersection ray.
            lookRight: System.Boolean - Project the ray to the right if true, to the left if false.
            slope: System.Double - Slope of the ray.
            linkCode: System.String - Only intersect with links with this code. An empty string "" intersects with all links.
        """
        pass
    
    
    def IntersectSurface(self):
        """
        IntersectSurface(surfaceId: ObjectId, alignmentId: ObjectId, origin: Autodesk.Civil.DatabaseServices.IPoint, lookRight: System.Boolean, slope: System.Double) -> IPoint
            Intersects a ray with a surface, with no maximum ray distance.
            surfaceId: ObjectId - Intersect the ray with this surface.
            alignmentId: ObjectId - Project the ray perpendicular to this alignment.
            origin: Autodesk.Civil.DatabaseServices.IPoint - Origin of the intersection ray.
            lookRight: System.Boolean - Project the ray to the right if true, to the left if false.
            slope: System.Double - Slope of the ray.
        IntersectSurface(surfaceId: ObjectId, alignmentId: ObjectId, origin: Autodesk.Civil.DatabaseServices.IPoint, lookRight: System.Boolean, slope: System.Double, maxDistance: System.Double) -> IPoint
            Intersects a ray with a surface.
            surfaceId: ObjectId - Intersect the ray with this surface.
            alignmentId: ObjectId - Project the ray perpendicular to this alignment.
            origin: Autodesk.Civil.DatabaseServices.IPoint - Origin of the intersection ray.
            lookRight: System.Boolean - Project the ray to the right if true, to the left if false.
            slope: System.Double - Slope of the ray.
            maxDistance: System.Double - Maximum distance to project the ray.
        """
        pass
    
    
    def IsAboveSurface(self):
        """
        IsAboveSurface(surfaceId: ObjectId, alignmentId: ObjectId, point: Autodesk.Civil.DatabaseServices.IPoint) -> IPoint
            Determines if roadway point is above a surface, with no minimum distance specified.
            surfaceId: ObjectId - Target surface.
            alignmentId: ObjectId - Source alignment.
            point: Autodesk.Civil.DatabaseServices.IPoint - Source point.
        IsAboveSurface(surfaceId: ObjectId, alignmentId: ObjectId, point: Autodesk.Civil.DatabaseServices.IPoint, minimumAmountAbove: System.Double) -> IPoint
            Determines if roadway point is above a surface.
            surfaceId: ObjectId - Target surface.
            alignmentId: ObjectId - Source alignment.
            point: Autodesk.Civil.DatabaseServices.IPoint - Source point.
            minimumAmountAbove: System.Double - Minimum amount above surface.
        """
        pass
    
    
    def RecordError(self):
        """
        RecordError(error: Autodesk.Civil.Runtime.CorridorError, errorLevel: Autodesk.Civil.Runtime.CorridorErrorLevel, description: System.String, source: System.String, showInEventViewer: System.Boolean) -> CorridorError
            Record error.
            error: Autodesk.Civil.Runtime.CorridorError
            errorLevel: Autodesk.Civil.Runtime.CorridorErrorLevel
            description: System.String
            source: System.String
            showInEventViewer: System.Boolean
        """
        pass
    
    
    def SampleSection(self):
        """
        SampleSection(surfaceId: ObjectId, alignmentId: ObjectId, point1: Autodesk.Civil.DatabaseServices.IPoint, point2: Autodesk.Civil.DatabaseServices.IPoint) -> SampledSectionLinkCollection
            Samples elevation along an existing surface.
            surfaceId: ObjectId - Target surface.
            alignmentId: ObjectId - Source alignment.
            point1: Autodesk.Civil.DatabaseServices.IPoint - Start sampling at this point.
            point2: Autodesk.Civil.DatabaseServices.IPoint - End sampling at this point.
        """
        pass
    
    
    def SetAxisOfRotationCrownPoint(self):
        """
        SetAxisOfRotationCrownPoint(nCrownPointIndex: System.UInt32)
            If the crown point is set, the axis of rotation uses it in its
            calculation for a divided crown/centers pivot type/multiple group assembly case.
            If a crown point is not set, the default Baseline pivot behavior is be used
            nCrownPointIndex: System.UInt32 - Index of crown point to be used in AOR calc.
        """
        pass
    
    
    def SetAxisOfRotationInformation(self):
        """
        SetAxisOfRotationInformation(isPotentialPivot: System.Boolean, superElevationSlope: System.Double, superElevationSlopeType: Autodesk.Civil.SuperelevationCrossSegmentType, isReversedSlope: System.Boolean) -> SuperelevationCrossSegmentType
            Save the AOR (Axis of Rotation) information for a subassembly
            isPotentialPivot: System.Boolean - Specifies whether the current subassembly will have potential pivot points for AOR (Axis of Rotation).
            superElevationSlope: System.Double - The current superelevation slope from the alignment.
            superElevationSlopeType: Autodesk.Civil.SuperelevationCrossSegmentType - The current superelevation slope type.
            isReversedSlope: System.Boolean - Specifies whether the superelevation slope is reversed while being used in the current subassembly.
        """
        pass
    
    
    def SetAxisOfRotationSERange(self):
        """
        SetAxisOfRotationSERange(dApplySE_StartOffset: System.Double, dApplySE_EndOffset: System.Double)
            By default, the axis of rotation calculation assumes the superelevation cross-slope
            set in SetAxisOfRotationInfomation applies to the full width of the subassembly.
            If the subassembly wants to override that behavior it can specify a starting
            and ending offset that indicates where superelavtion was applied.
            dApplySE_StartOffset: System.Double - The start of the range where superelevation is applied.
            dApplySE_EndOffset: System.Double - The end of the range where superelevation is applied.
        """
        pass
    
    
    def SoeToXyz(self):
        """
        SoeToXyz(alignmentId: ObjectId, station: System.Double, offset: System.Double, elevation: System.Double, X: System.Double, Y: System.Double, Z: System.Double)
            Transforms from assembly local station, offset, elevation (SOE) coordinates to world x,y,z coordinates.
            alignmentId: ObjectId - Transform using this alignment.
            station: System.Double - Source station.
            offset: System.Double - Source offset.
            elevation: System.Double - Source elevation.
            X: System.Double - Destination X.
            Y: System.Double - Destination Y.
            Z: System.Double - Destination Z.
        """
        pass
    
    
    def XyzToSoe(self):
        """
        XyzToSoe(alignmentId: ObjectId, X: System.Double, Y: System.Double, Z: System.Double, station: System.Double, offset: System.Double, elevation: System.Double)
            Transforms from world x,y,z coordinates to assembly local station, offset, elevation (SOE) coordinates.
            alignmentId: ObjectId - Transform using this alignment.
            X: System.Double - Source X.
            Y: System.Double - Source Y.
            Z: System.Double - Source Z.
            station: System.Double - Destination station.
            offset: System.Double - Destination offset.
            elevation: System.Double - Destination elevation.
        """
        pass
    
    pass

class IParam():
    """
    Interface for parameters.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Value = None
    pass

class Param(object):
    """
    Use Autodesk.Civil.IParam instead.
    """
    pass

class ParamAccessType():
    """
    Defines access permissions for a parameter.
    """
    pass

class ParamAlignment(ParamBase):
    """
    Alignment parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Value = None
    pass

class ParamAlignmentCollection(ParamCollectionBase):
    """
    A collection of Alignment parameters.
    """
    Count = None
    Item = None
    def Value(self):
        """
        Value(index: System.Int32) -> ObjectId
            index: System.Int32
        Value(index: System.String) -> ObjectId
            index: System.String
        """
        pass
    
    pass

class ParamBase(ParamBool):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamElevationTarget):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamLong):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamDouble):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamString):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamPoint):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamAlignment):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamProfile):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamSurface):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBase(ParamOffsetTarget):
    """
    
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Key = None
    Value = None
    pass

class ParamBool(ParamBase):
    """
    A boolean parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    TypeInfo = None
    Value = None
    pass

class ParamBoolCollection(ParamCollectionBase):
    """
    A collection of boolean parameters.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, value: System.Boolean) -> ParamBool
            Adds a new item to parameters collection.
            Remarks: If the input name exists in collection, this function will not add new item, instead it will return existing item and change its value.
            name: System.String - Name of the new parameter.
            value: System.Boolean - Value of the new parameter.
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> bool
            index: System.Int32
        Value(index: System.String) -> bool
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamAlignmentCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamAlignment
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> ObjectId
            index: System.Int32
        Value(index: System.String) -> ObjectId
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamBoolCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamBool
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> bool
            index: System.Int32
        Value(index: System.String) -> bool
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamDoubleCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamDouble
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> double
            index: System.Int32
        Value(index: System.String) -> double
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamElevationTargetCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamElevationTarget
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> SlopeElevationTarget
            index: System.Int32
        Value(index: System.String) -> SlopeElevationTarget
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamLongCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamLong
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> int
            index: System.Int32
        Value(index: System.String) -> int
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamOffsetTargetCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamOffsetTarget
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> WidthOffsetTarget
            index: System.Int32
        Value(index: System.String) -> WidthOffsetTarget
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamPointCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamPoint
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> Point3d
            index: System.Int32
        Value(index: System.String) -> Point3d
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamProfileCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamProfile
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> ObjectId
            index: System.Int32
        Value(index: System.String) -> ObjectId
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamStringCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamString
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> string
            index: System.Int32
        Value(index: System.String) -> string
            index: System.String
        """
        pass
    
    pass

class ParamCollectionBase(ParamSurfaceCollection):
    """
    
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ParamSurface
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> ObjectId
            index: System.Int32
        Value(index: System.String) -> ObjectId
            index: System.String
        """
        pass
    
    pass

class ParamDouble(ParamBase):
    """
    A parameter with a double value.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    TypeInfo = None
    Value = None
    pass

class ParamDoubleCollection(ParamCollectionBase):
    """
    A collection of double parameters.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, value: System.Double) -> ParamDouble
            Adds a new item to parameters collection.
            Remarks: If the input name exists in collection, this function will not add new item, instead it will return existing item and change its value.
            name: System.String - Name of the new parameter.
            value: System.Double - Value of the new parameter.
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> double
            index: System.Int32
        Value(index: System.String) -> double
            index: System.String
        """
        pass
    
    pass

class ParamElevationTarget(ParamBase):
    """
    Elevation target parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Value = None
    pass

class ParamElevationTargetCollection(ParamCollectionBase):
    """
    A collection of elevation target parameters.
    """
    Count = None
    Item = None
    def Value(self):
        """
        Value(index: System.Int32) -> SlopeElevationTarget
            index: System.Int32
        Value(index: System.String) -> SlopeElevationTarget
            index: System.String
        """
        pass
    
    pass

class ParamLogicalNameType():
    """
    
    """
    pass

class ParamLong(ParamBase):
    """
    A long parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    TypeInfo = None
    Value = None
    def AddEnumData(self):
        """
        AddEnumData(name: System.String, displayName: System.String, value: System.Int32)
            Gets the name, display name, and value for the enum specified by name.
            name: System.String
            displayName: System.String
            value: System.Int32
        """
        pass
    
    
    def EnumCount(self):
        """
        EnumCount() -> uint
            Gets the number of values in the enums for this parameter.
        """
        pass
    
    
    def GetEnumData(self):
        """
        GetEnumData(index: System.UInt32, name: System.String, displayName: System.String, value: System.Int32)
            Gets the name, display name, and value for the enum specified by index.
            index: System.UInt32
            name: System.String
            displayName: System.String
            value: System.Int32
        """
        pass
    
    pass

class ParamLongCollection(ParamCollectionBase):
    """
    A collection of long parameters.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, value: System.Int32) -> ParamLong
            Adds a new item to parameters collection.
            Remarks: If the input name exists in collection, this function will not add new item, instead it will return existing item and change its value.
            name: System.String - Name of the new parameter.
            value: System.Int32 - Value of the new parameter.
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> int
            index: System.Int32
        Value(index: System.String) -> int
            index: System.String
        """
        pass
    
    pass

class ParamOffsetTarget(ParamBase):
    """
    An offset target parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Value = None
    pass

class ParamOffsetTargetCollection(ParamCollectionBase):
    """
    A collection of offset target parameters.
    """
    Count = None
    Item = None
    def Value(self):
        """
        Value(index: System.Int32) -> WidthOffsetTarget
            index: System.Int32
        Value(index: System.String) -> WidthOffsetTarget
            index: System.String
        """
        pass
    
    pass

class ParamPoint(ParamBase):
    """
    A point parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    Elevation = None
    IsReadOnly = None
    Offset = None
    Station = None
    Value = None
    def GetPoint(self):
        """
        GetPoint(station: System.Double, offset: System.Double, elevation: System.Double)
            Gets the station, offset, and elevation associated with the parameter.
            station: System.Double
            offset: System.Double
            elevation: System.Double
        """
        pass
    
    
    def SetPoint(self):
        """
        SetPoint(station: System.Double, offset: System.Double, elevation: System.Double)
            Sets the station, offset, and elevation associated with the parameter.
            station: System.Double
            offset: System.Double
            elevation: System.Double
        """
        pass
    
    pass

class ParamPointCollection(ParamCollectionBase):
    """
    A collection of point parameters.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String) -> ParamPoint
            Adds a new item to parameters collection.
            Remarks: If the input name exists in collection, this function will not add new item, instead it will return existing item and change its value.
            name: System.String - Name of the new parameter.
        Add(name: System.String, value: Point3d) -> ParamPoint
            Adds a new item to the parameters collection.
            Remarks: If the input name exists in collection, this function will not add new item, instead it will return existing item and change its value.
            name: System.String - Name of the new parameter.
            value: Point3d - Value of the new parameter.
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> Point3d
            index: System.Int32
        Value(index: System.String) -> Point3d
            index: System.String
        """
        pass
    
    pass

class ParamProfile(ParamBase):
    """
    A Profile parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Value = None
    pass

class ParamProfileCollection(ParamCollectionBase):
    """
    A collection of profile parameters.
    """
    Count = None
    Item = None
    def Value(self):
        """
        Value(index: System.Int32) -> ObjectId
            index: System.Int32
        Value(index: System.String) -> ObjectId
            index: System.String
        """
        pass
    
    pass

class ParamScope():
    """
    Defines the parameter scope.
    """
    pass

class ParamString(ParamBase):
    """
    A string parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Value = None
    pass

class ParamStringCollection(ParamCollectionBase):
    """
    A collection of string parameters.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String, value: System.String) -> ParamString
            Adds a new item to parameters collection.
            Remarks: If the input name exists in the collection, this function will not add a new item. Instead it will return the existing item and change its value.
            name: System.String - Name of the new parameter.
            value: System.String - Value of the new parameter.
        """
        pass
    
    
    def Value(self):
        """
        Value(index: System.Int32) -> string
            index: System.Int32
        Value(index: System.String) -> string
            index: System.String
        """
        pass
    
    pass

class ParamSurface(ParamBase):
    """
    A Surface parameter.
    """
    Access = None
    Comment = None
    Description = None
    DisplayName = None
    DisplayOrder = None
    IsReadOnly = None
    Value = None
    pass

class ParamSurfaceCollection(ParamCollectionBase):
    """
    A collection of surface parameters.
    """
    Count = None
    Item = None
    def Value(self):
        """
        Value(index: System.Int32) -> ObjectId
            index: System.Int32
        Value(index: System.String) -> ObjectId
            index: System.String
        """
        pass
    
    pass

class ParamType():
    """
    Defines the parameter type.
    """
    pass

class ParamsOwnerType():
    """
    Defines the owner type for a parameter.
    """
    pass

class PipeNetworkState(RuntimeState):
    """
    Contains the properties of the drawing's pipe network state.
    """
    CurrentPipeId = None
    CurrentStructureId = None
    IsBreakingPipe = None
    IsConnectingToStructure = None
    IsCurrentPartBeingAdd = None
    IsInLayoutMode = None
    IsLayoutUpStream = None
    LastPipeElevation = None
    ParamsBool = None
    ParamsDouble = None
    ParamsLong = None
    def RuleResourceString(self):
        """
        RuleResourceString(resId: System.String) -> string
            Resolves resource string ids defined inside the C3DPipeRules.DVB project.
            resId: System.String - Resource string.
        """
        pass
    
    
    def SetAlignmentOnPart(self):
        """
        SetAlignmentOnPart(paramName: System.String, alignmentId: ObjectId)
            Sets the specified parameter of alignment on the current part.
            paramName: System.String - The name of the parameter to set.
            alignmentId: ObjectId - The value to assign to the parameter.
        """
        pass
    
    
    def SetBoolOnPart(self):
        """
        SetBoolOnPart(paramName: System.String, value: System.Boolean)
            Sets the specified parameter of bool on the current part.
            paramName: System.String - The name of the parameter to set.
            value: System.Boolean - The value to assign to the parameter.
        """
        pass
    
    
    def SetDoubleOnCurrentPart(self):
        """
        SetDoubleOnCurrentPart(paramKey: System.String, value: System.Double)
            Sets an double value on the current part for the specified parameter.
            paramKey: System.String - Name of the part parameter.
            value: System.Double - Value to assign to the specified part parameter.
        """
        pass
    
    
    def SetErrorMsgOnCurrentPart(self):
        """
        SetErrorMsgOnCurrentPart(paramKey: System.String, errorMessage: System.String)
            Sets an error message on the current part for the specified parameter.
            paramKey: System.String - Name of the part parameter.
            errorMessage: System.String - The error message.
        """
        pass
    
    
    def SetLongOnPart(self):
        """
        SetLongOnPart(paramName: System.String, value: System.Int32)
            Sets the specified parameter of long on the current part.
            paramName: System.String - The name of the parameter to set.
            value: System.Int32 - The value to assign to the parameter.
        """
        pass
    
    
    def SetPointOnPart(self):
        """
        SetPointOnPart(paramName: System.String, value: Point3d)
            Sets the specified parameter of point on the current part.
            paramName: System.String - The name of the parameter to set.
            value: Point3d - The value to assign to the parameter.
        """
        pass
    
    
    def SetProfileOnPart(self):
        """
        SetProfileOnPart(paramName: System.String, profileId: ObjectId)
            Sets the specified parameter of profile on the current part.
            paramName: System.String - The name of the parameter to set.
            profileId: ObjectId - The value to assign to the parameter.
        """
        pass
    
    
    def SetStringOnPart(self):
        """
        SetStringOnPart(paramName: System.String, value: System.String)
            Sets the specified parameter of string on the current part.
            paramName: System.String - The name of the parameter to set.
            value: System.String - The value to assign to the parameter.
        """
        pass
    
    
    def SetSurfaceOnPart(self):
        """
        SetSurfaceOnPart(paramName: System.String, surfaceId: ObjectId)
            Sets the specified parameter of surface on the current part.
            paramName: System.String - The name of the parameter to set.
            surfaceId: ObjectId - The value to assign to the parameter.
        """
        pass
    
    pass

class RuntimeState(CorridorState):
    """
    Base class for objects containing user-defined parameters describing an object state.
    """
    CurrentMacroName = None
    CurrentMacroProject = None
    pass

class TypeInfoBool():
    """
    
    """
    pass

class TypeInfoDouble():
    """
    
    """
    pass

class TypeInfoLong():
    """
    
    """
    pass