class AdditionalAppliedAssemblyInfo(object):
    """
    This class is used to represent the station and description of an additional applied assembly.
    """
    Description = None
    Station = None
    pass

class Alignment(Entity):
    """
    The Alignment class.  Alignment objects can represent centerlines, lanes, shoulders, right-of-ways, 
    or construction baselines.
    """
    AlignmentType = None
    CANTCriticalStaitons = None
    CANTCurves = None
    CreationMode = None
    CriteriaFileName = None
    DesignCheckSetId = None
    DesignCheckSetName = None
    DesignSpeeds = None
    EndingStation = None
    EndingStationWithEquations = None
    Entities = None
    HasRoundabout = None
    IsConnectedAlignment = None
    IsOffsetAlignment = None
    IsSiteless = None
    Length = None
    OffsetAlignmentInfo = None
    RailAlignmentInfo = None
    ReferencePoint = None
    ReferencePointStation = None
    SiteId = None
    SiteName = None
    StartingStation = None
    StationEquations = None
    StationIndexIncrement = None
    StyleId = None
    StyleName = None
    SuperelevationCriticalStations = None
    SuperelevationCurves = None
    SuperelevationType = None
    UpdateMode = None
    UseDesignCheckSet = None
    UseDesignCriteriaFile = None
    UseDesignSpeed = None
    def CopyToSite(self):
        """
        CopyToSite(siteId: ObjectId)
            Copies the Alignment to a specified Site. Specifying ObjectId.Null to copy it to siteless.
            Calling this method copies all children profiles, profile views and sample line group with this alignment as well.
            siteId: ObjectId -  The destination site ObjectId.
        CopyToSite(siteName: System.String)
            Copies the Alignment to a specified Site. Specifying "" to move it to siteless.
            Calling this method copies all children profiles, profile views and sample line group with this alignment as well.
            siteName: System.String -  The destination site name.
        """
        pass
    
    
    def Create(self):
        """
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, alignmentName: System.String, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> CivilDocument
            Creates an Alignment without geometry information.
            Remarks: This method creates an Alignment using ObjectId parameters. Use an ObjectId.NULL for a siteless Alignment.
            document: Autodesk.Civil.ApplicationServices.CivilDocument - Document object in which the Alignment is created. 
            alignmentName: System.String -  Name of the created Alignment. 
            siteId: ObjectId -  ObjectId of the site on which the Alignment is created. Pass null to create
            a siteless alignment.
            layerId: ObjectId -  ObjectId of the layer on which the Alignment is created. 
            styleId: ObjectId -  ObjectId of the style applied to the created Alignment. 
            labelSetId: ObjectId -  ObjectId of the labelSet applied to the created Alignment. 
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, alignmentName: System.String, siteName: System.String, layerName: System.String, styleName: System.String, labelSetName: System.String) -> CivilDocument
            Creates an Alignment without geometry information.
            Remarks: This method creates an Alignment using string parameters. Use an empty site name for a siteless Alignment.
            document: Autodesk.Civil.ApplicationServices.CivilDocument - Document object in which the Alignment is created.
            alignmentName: System.String - Name of the created Alignment.
            siteName: System.String - Name of the site on which Alignment is created. Pass null to create
            a siteless alignment.
            layerName: System.String - Name of the layer on which the Alignment is created. 
            styleName: System.String - Name of the style applied to the created Alignment. 
            labelSetName: System.String - Name of the labelSet applied to the created Alignment. 
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, plineOptions: Autodesk.Civil.DatabaseServices.PolylineOptions, alignmentName: System.String, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> CivilDocument
            Creates an Alignment from the specified Polyline, Polyline2d or Polyline3d.
            Remarks: This method creates an Alignment using ObjectId parameters. Use an ObjectId.NULL for a siteless Alignment.
            document: Autodesk.Civil.ApplicationServices.CivilDocument - Document object in which the Alignment is created. 
            plineOptions: Autodesk.Civil.DatabaseServices.PolylineOptions - Polyline options for creating the Alignment, including whether to add curves between
            tangents, and whether to erase the original polyline. 
            alignmentName: System.String -  Name of the created Alignment. 
            siteId: ObjectId -  ObjectId of the site on which the Alignment is created.  Pass null to create
            a siteless alignment.
            layerId: ObjectId -  ObjectId of the layer on which the Alignment is created. 
            styleId: ObjectId -  ObjectId of the style applied to the created Alignment. 
            labelSetId: ObjectId -  ObjectId of the labelSet applied to the created Alignment. 
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, plineOptions: Autodesk.Civil.DatabaseServices.PolylineOptions, alignmentName: System.String, siteName: System.String, layerName: System.String, styleName: System.String, labelSetName: System.String) -> CivilDocument
            Creates an Alignment from the specified Polyline, Polyline2d or Polyline3d.
            Remarks: This method creates an Alignment using string parameters. Use an null or empty site name for a siteless Alignment.
            document: Autodesk.Civil.ApplicationServices.CivilDocument - Document object in which the Alignment is created.
            plineOptions: Autodesk.Civil.DatabaseServices.PolylineOptions - Polyline options for creating the Alignment, including whether to add curves between
            tangents, and whether to erase the original polyline.
            alignmentName: System.String - Name of the created Alignment.
            siteName: System.String - Name of the site on which Alignment is created.  Pass null to create a
            siteless alignment.
            layerName: System.String - Name of the layer on which the Alignment is created. 
            styleName: System.String - Name of the style applied to the created Alignment. 
            labelSetName: System.String - Name of the labelSet applied to the created Alignment. 
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, alignmentName: System.String, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, type: Autodesk.Civil.DatabaseServices.AlignmentType) -> CivilDocument
            Creates an Alignment without geometry information, with Alignment Type.
            Remarks: This method creates an Alignment using ObjectId parameters. Use an ObjectId.NULL for a siteless Alignment.
            document: Autodesk.Civil.ApplicationServices.CivilDocument - Document object in which the Alignment is created. 
            alignmentName: System.String -  Name of the created Alignment. 
            siteId: ObjectId -  ObjectId of the site on which the Alignment is created. Pass null to create
            a siteless alignment.
            layerId: ObjectId -  ObjectId of the layer on which the Alignment is created. 
            styleId: ObjectId -  ObjectId of the style applied to the created Alignment. 
            labelSetId: ObjectId -  ObjectId of the labelSet applied to the created Alignment. 
            type: Autodesk.Civil.DatabaseServices.AlignmentType -  Alignment type of the created Alignment object. 
        Create(corridorFeatureLine: Autodesk.Civil.DatabaseServices.CorridorFeatureLine, alignmentName: System.String, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, alignmentType: Autodesk.Civil.DatabaseServices.AlignmentType) -> CorridorFeatureLine
            Creates an Alignment from the specified CorridorFeatureLine.
            corridorFeatureLine: Autodesk.Civil.DatabaseServices.CorridorFeatureLine - The CorridorFeatureLine used to create Alignment. 
            alignmentName: System.String - The name of the created Alignment. 
            siteId: ObjectId - The ObjectId of the site on which the Alignment is created.  Pass null to create
            a siteless Alignment.
            layerId: ObjectId - The ObjectId of the layer on which the Alignment is created. 
            styleId: ObjectId - The ObjectId of the style applied to the created Alignment. 
            labelSetId: ObjectId - The ObjectId of the labelSet applied to the created Alignment. 
            alignmentType: Autodesk.Civil.DatabaseServices.AlignmentType
        """
        pass
    
    
    def CreateOffsetAlignment(self):
        """
        CreateOffsetAlignment(offsetDistance: System.Double) -> Autodesk.Civil.DatabaseServices.Alignment.
            Creates an offset Alignment from the current alignment, returns the offset Alignment ObjectId.
            A positive value to create an offset alignment to the right side and negative to the left side.
            offsetDistance: System.Double - Specifies the distance to create offset Alignment.
        CreateOffsetAlignment(alignmentName: System.String, parentAlignmentId: ObjectId, offset: System.Double, styleId: ObjectId) -> ObjectId
            Creates an offset Alignment from the specified alignment object Id, returns the object Id of the offset alignment.
            Remarks: A negative value (offset < 0) indicates the Offset Alignment is at the left of the parent alignment.A positive value (offset > 0) indicates the Offset Alignment is at the right.
            alignmentName: System.String - The name of the offset alignment.
            parentAlignmentId: ObjectId - The object Id of  the parent alignment.
            offset: System.Double - The offset value for the offset alignment.
            styleId: ObjectId - The styleId for the offset alignment.
        CreateOffsetAlignment(database: Database, alignmentName: System.String, parentAlignmentName: System.String, offset: System.Double, styleName: System.String) -> ObjectId
            Creates an offset Alignment from the specified alignment name, returns the object Id of the offset alignment.
            Remarks: A negative value (offset < 0) indicates the Offset Alignment is at the left of the parent alignment.A positive value (offset > 0) indicates the Offset Alignment is at the right.
            database: Database - The database of the parent alignment.
            alignmentName: System.String - The name of the offset alignment.
            parentAlignmentName: System.String - The name of the parent alignment.
            offset: System.Double - The offset value for the offset alignment.
            styleName: System.String - The style name for the offset alignment .
        CreateOffsetAlignment(alignmentName: System.String, parentAlignmentId: ObjectId, offset: System.Double, styleId: ObjectId, startStation: System.Double, endStation: System.Double) -> ObjectId
            Creates an offset Alignment from the specified alignment object Id, returns the object Id of the offset alignment.
            Remarks: A negative value (offset < 0) indicates the Offset Alignment is at the left of the parent alignment.A positive value (offset > 0) indicates the Offset Alignment is at the right.
            alignmentName: System.String - The name of the offset alignment.
            parentAlignmentId: ObjectId - The object Id of  the parent alignment.
            offset: System.Double - The offset value for the offset alignment.
            styleId: ObjectId - The styleId for the offset alignment.
            startStation: System.Double - The start station for the offset alignment.
            endStation: System.Double - The end station for the offset alignment.
        CreateOffsetAlignment(database: Database, alignmentName: System.String, parentAlignmentName: System.String, offset: System.Double, styleName: System.String, startStation: System.Double, endStation: System.Double) -> ObjectId
            Creates an offset Alignment from the specified alignment name, returns the object Id of the offset alignment.
            Remarks: A negative value (offset < 0) indicates the Offset Alignment is at the left of the parent alignment.A positive value (offset > 0) indicates the Offset Alignment is at the right.
            database: Database - The database of the parent alignment.
            alignmentName: System.String - The name of the offset alignment.
            parentAlignmentName: System.String - The name of the parent alignment.
            offset: System.Double - The offset value for the offset alignment.
            styleName: System.String - The style name for the offset alignment .
            startStation: System.Double - The start station for the offset alignment.
            endStation: System.Double - The end station for the offset alignment.
        """
        pass
    
    
    def DistanceToAlignment(self):
        """
        DistanceToAlignment(stationOnThisAlignment: System.Double, otherAlignment: Autodesk.Civil.DatabaseServices.Alignment, distanceToOtherAlignment: System.Double, stationOnOtherAlignment: System.Double) -> Alignment
            Computes the distance to another Alignment.  If the target Alignment crosses the current Alignment, this
            method checks the distance to the target Alignment on both sides, and returns the shorter distance.
            stationOnThisAlignment: System.Double - Specifies the station name located on the current Alignment.
            otherAlignment: Autodesk.Civil.DatabaseServices.Alignment - Specifies the name of the target Alignment.
            distanceToOtherAlignment: System.Double - Returns the distance from the current Alignment to the other Alignment.
            stationOnOtherAlignment: System.Double - Returns the station located on the other Alignment.
        DistanceToAlignment(stationOnThisAlignment: System.Double, otherAlignment: Autodesk.Civil.DatabaseServices.Alignment, enumSide: Autodesk.Civil.DatabaseServices.AlignmentSide, distanceToOtherAlignment: System.Double, stationOnOtherAlignment: System.Double) -> Alignment
            Computes the distance to another Alignment, specifying the side of current Alignment to look for the target Alignment.
            stationOnThisAlignment: System.Double - Specifies the station name located on the current Alignment.
            otherAlignment: Autodesk.Civil.DatabaseServices.Alignment - Specifies the name of target Alignment.
            enumSide: Autodesk.Civil.DatabaseServices.AlignmentSide - Specifies which side of this Alignment to look for the target Alignment.  This is required in the
             the case where the alignments cross, and the target Alignment can be found on both sides.
            distanceToOtherAlignment: System.Double - Returns the distance from the current Alignment to the other Alignment.
            stationOnOtherAlignment: System.Double - Returns the station located on the other Alignment.
        """
        pass
    
    
    def GetAlignmentLabelGroupIds(self):
        """
        GetAlignmentLabelGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the Alignment's label group.
        """
        pass
    
    
    def GetAlignmentLabelIds(self):
        """
        GetAlignmentLabelIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the Alignment's labels.
        """
        pass
    
    
    def GetChildOffsetAlignmentIds(self):
        """
        GetChildOffsetAlignmentIds() -> ObjectIdCollection
            Gets the objectId collection of all child offset alignments, whose parent is this alignment instance.
        GetChildOffsetAlignmentIds(onlyDynamicUpdate: System.Boolean) -> ObjectIdCollection
            Gets the objectId collection of all child offset alignments, whose parent is this alignment instance.
            onlyDynamicUpdate: System.Boolean - Specifies whether only to include offset Alignment whose update mode is dynamic.
        """
        pass
    
    
    def GetCrossSlopeAtStation(self):
        """
        GetCrossSlopeAtStation(station: System.Double, crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType, applySmoothing: System.Boolean) -> SuperelevationCrossSegmentType
            Gets the cross slope value at the specified station for the indicated segment type.
            station: System.Double - The station value on the alignment object.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
            applySmoothing: System.Boolean - The bool value representing whether smoothing should be considered when calculating the cross slope.
        """
        pass
    
    
    def GetInstantaneousRadius(self):
        """
        GetInstantaneousRadius(rawStation: System.Double) -> double
            Returns the instantaneous radius at the specified station.
            rawStation: System.Double - Specifies the raw (no equations) station value.
        """
        pass
    
    
    def GetLabelGroupIds(self):
        """
        GetLabelGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the Alignment's label group.
        """
        pass
    
    
    def GetLabelIds(self):
        """
        GetLabelIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the Alignment's labels.
        """
        pass
    
    
    def GetNextUniqueName(self):
        """
        GetNextUniqueName(alignmentName: System.String) -> string
            Gets a string indicating a unique name for the Alignment. The input string could be a name template.
            Remarks: You can use this method to get a guaranteed unique name for the Alginment.  Every time you call this method, 
            the internal counter increments by one, even if no Alignment is created.
            For example: 
            CopyC#1String name1 = Alignment.GetNextUniqueName (..., "A");   //  name1 = "A"
            2String name2 = Alignment.GetNextUniqueName (..., "A");   //  name2 = "A(1)"
            3String name3 = Alignment.GetNextUniqueName (..., "Alignment - (<[Next Counter(CP)]>)");   //  name3 = "Alignment - (1)"
            4String name4 = Alignment.GetNextUniqueName (..., "Alignment - (<[Next Counter(CP)]>)");   //  name4 = "Alignment - (1)"
            alignmentName: System.String - A proposed Alignment name.
        """
        pass
    
    
    def GetPolyline(self):
        """
        GetPolyline() -> ObjectId
            Gets a polyline from the Alignment geometry.
        """
        pass
    
    
    def GetProfileIds(self):
        """
        GetProfileIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of all profiles belonging to this Alignment.
        """
        pass
    
    
    def GetProfileViewIds(self):
        """
        GetProfileViewIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of all profile views belonging to this Alignment.
        """
        pass
    
    
    def GetRegions(self):
        """
        GetRegions() -> AlignmentRegionCollection
            Gets the regions, which are included in offset alignment or curb return.
        """
        pass
    
    
    def GetSampleLineGroupIds(self):
        """
        GetSampleLineGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of all sample line groups belonging to this Alignment.
        """
        pass
    
    
    def GetStationSet(self):
        """
        GetStationSet(stationType: Autodesk.Civil.DatabaseServices.StationTypes) -> Station
            Gets the station set according to the StationType.
            stationType: Autodesk.Civil.DatabaseServices.StationTypes -  The type of the station which will be collected. 
            This method overload is intended to get station types other than All, Major, and Minor. 
        GetStationSet(stationType: Autodesk.Civil.DatabaseServices.StationTypes, interval: System.Double) -> Station
            Gets the station set according to the StationType and interval.
            stationType: Autodesk.Civil.DatabaseServices.StationTypes -  The type of the station which will be collected. 
            This method overload is intended to get Major or Minor station types.
            interval: System.Double -  The interval of station. You can only enter a Major and Minor station. 
        GetStationSet(stationType: Autodesk.Civil.DatabaseServices.StationTypes, majorInterval: System.Double, minorInterval: System.Double) -> Station
            Gets the station set according to the StationType and intervals.
            stationType: Autodesk.Civil.DatabaseServices.StationTypes -  The type of the station which will be collected. 
            This method overload is intended to get All or HorizontalMask station types.
            majorInterval: System.Double -  The major interval of station. 
            minorInterval: System.Double -  The minor interval of station. 
        """
        pass
    
    
    def GetStationStringWithEquations(self):
        """
        GetStationStringWithEquations(rawStation: System.Double) -> string
            Gets a string indicating the station of an Alignment using the Station equations.
            rawStation: System.Double - Specifies the raw (no equations) Station value.
        """
        pass
    
    
    def ImportLabelSet(self):
        """
        ImportLabelSet(labelSetStyleId: ObjectId)
            Takes the contents of the AlignmentLabelSetStyle template and copies its data into the database object.
            Remarks: Note that when the copying is performed, any existing AlignmentLabelSetStyle values are removed.
            labelSetStyleId: ObjectId - Label style set template ObjectId.
        ImportLabelSet(labelSetStyleName: System.String)
            Takes the contents of the AlignmentLabelSetStyle template and copies its data into the Database object.
            Remarks: Note that when the copying is performed, any existing AlignmentLabelSetStyle values are removed.
            labelSetStyleName: System.String - Label style set template name.
        """
        pass
    
    
    def PointLocation(self):
        """
        PointLocation(station: System.Double, offset: System.Double, easting: System.Double, northing: System.Double)
            Returns the easting and northing of a point on an Alignment given a station and an offset for the Alignment.
            station: System.Double - Specifies the station.
            offset: System.Double - Specifies the offset.
            easting: System.Double - Returns the Easting value.
            northing: System.Double - Returns the Northing value.
        PointLocation(station: System.Double, offset: System.Double, tolerance: System.Double, easting: System.Double, northing: System.Double, Bearing: System.Double)
            Given station and offset values, returns the easting, northing, and bearing values at that point on the Alignment.
            station: System.Double - Specifies the station name.
            offset: System.Double - Specifies the offset value.
            tolerance: System.Double - Specifies the tolerance value for the range of stations and offset values.  This value affects what alignment entity is examined for the point.  
            For example, if the length of the first entity in an alignment is 260, and this method looks for station 400, with tolerance 200, a point on the first entity is returned.  This is because 400-260 < 200.
            See the Developer's Guide for more information. 
            easting: System.Double - Returns the Easting value.
            northing: System.Double - Returns the Northing value.
            Bearing: System.Double - Returns the Bearing value.
        """
        pass
    
    
    def Reverse(self):
        """
        Reverse()
            Reverse the Alignment direction.
            Remarks: Reversing the stationing will remove all station equations and
            design speeds, and may adversely affect objects and data already
            created from the Alignment.
        """
        pass
    
    
    def StationOffset(self):
        """
        StationOffset(easting: System.Double, northing: System.Double, station: System.Double, offset: System.Double)
            Returns the station and offset on an Alignment at given easting and northing values.
            easting: System.Double - Specifies the Easting value.
            northing: System.Double - Specifies the Northing value.
            station: System.Double - Returns the station specified by the northing and easting.
            offset: System.Double - Returns the offset specified by the northing and easting.
        StationOffset(easting: System.Double, northing: System.Double, tolerance: System.Double, station: System.Double, offset: System.Double)
            Returns the nearest station and offset on an Alignment at given easting, northing and tolerance values.
            Remarks: This method returns an error code if the station and offset are out of range using the tolerance given.
            easting: System.Double - Specifies the Easting value.
            northing: System.Double - Specifies the Northing value.
            tolerance: System.Double - Specifies the tolerance value.  This value is in the same coordinate units as the Easting and Northing values,
            and specifies a range within which the method looks for a point on the Alignment.
            station: System.Double - Returns the station value.
            offset: System.Double - Returns the offset value.
        """
        pass
    
    
    def Update(self):
        """
        Update()
            Updates the OffsetAlignmentInfo for an offset alignment object.
            Remarks: If the geometry of a parent alignment is changed, the geometry and information for dependent offset alignments are not immediately updated in the same transaction.  
            When you need to work with a parent and offset alignments in the same operation, you should update the offset alignment before getting its OffsetAlignmentInfo. 
            You can get all the child offset alignments with GetChildOffsetAlignmentIds() and GetChildOffsetAlignmentIds(Boolean).
        """
        pass
    
    pass

class AlignmentArc(AlignmentEntity):
    """
    The AlignmentArc class.
    
    AlignmentArc derives from the abstract AlignmentCurve class,
    and represents an AlignmentEntity made up of a single
    AlignmentSubEntityArc object.
    """
    CenterPoint = None
    ChordDirection = None
    ChordLength = None
    Clockwise = None
    Constraint2 = None
    CurveGroupIndex = None
    CurveGroupSubEntityIndex = None
    DeflectedAngle = None
    Delta = None
    DirectionAtPoint1 = None
    DirectionAtPoint2 = None
    EndDirection = None
    ExternalSecant = None
    ExternalTangent = None
    GreaterThan180 = None
    Item = None
    Length = None
    MidOrdinate = None
    MinimumRadius = None
    PassThroughPoint1 = None
    PassThroughPoint2 = None
    PassThroughPoint3 = None
    PIStation = None
    Radius = None
    ReverseCurve = None
    StartDirection = None

    pass

class AlignmentArcConstraintType():
    """
    Defines the underlying alignment arc entity constraint type. For example, three points, or center radius
    """
    pass

class AlignmentCCRC(AlignmentEntity):
    """
    The Alignment CurveCurveReverseCurve class.
    This class represents an AlignmentEntity made up of Curve, Curve and reverse Curve subentities.
    """
    Arc1 = None
    Arc2 = None
    Arc3 = None
    Constraint2 = None

    pass

class AlignmentCCRCConstraintType():
    """
    Defines the underlying Curve-Curve-ReverseCurve entity constraint type.
    """
    pass

class AlignmentCRC(AlignmentEntity):
    """
    The Alignment MultipleArcs class.
    This class represents an AlignmentEntity made up of Curve and reverse curve subentities.
    """
    Arc1 = None
    Arc2 = None
    Constraint2 = None

    pass

class AlignmentCRCConstraintType():
    """
    Defines the underlying Curve-ReverseCurve entity constraint type.
    """
    pass

class AlignmentCTC(AlignmentEntity):
    """
    The Alignment MultipleArcs class.
    This class represents an AlignmentEntity made up of Curve, Line and Curve subentities.
    """
    Arc1 = None
    Arc2 = None
    Constraint2 = None
    Tangent = None

    pass

class AlignmentCTCConstraintType():
    """
    Defines the underlying Curve-Line-Curve entity constraint type.
    """
    pass

class AlignmentCantLabelGroup(Entity):
    """
    This class encapsulates the functionality of an alignment cant group label.
    """

    def Create(self):
        """
        Create(alignmentId: ObjectId) -> ObjectId
            Creates a new instance of an AlignmentCantLabelGroup on an alignment entity with the default label style.
            alignmentId: ObjectId - The alignment in which the label group is located.
        Create(alignmentId: ObjectId, styleId: ObjectId) -> ObjectId
            Creates a new instance of an AlignmentCantLabelGroup on an alignment entity with the specified label style.
            alignmentId: ObjectId - The alignment in which the label group is located.
            styleId: ObjectId - The style of the new AlignmentCantLabelGroup.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of AlignmentCantLabelGroup objects on the Alignment.
            alignmentId: ObjectId - The ObjectId of the Alignment where the labels are located.
        """
        pass
    
    
    def GetGeometryPointsOptions(self):
        """
        GetGeometryPointsOptions() -> GeometryPointSelector
            Gets a GeometryPointSelector object containing the state of all CantPointType objects for the current label.
        """
        pass
    
    
    def SetGeometryPointsOptions(self):
        """
        SetGeometryPointsOptions(transitionPointsOptions: Autodesk.Civil.GeometryPointSelector) -> GeometryPointSelector
            Sets the state of all CantPointType objects for the current label.
            transitionPointsOptions: Autodesk.Civil.GeometryPointSelector
        """
        pass
    
    pass

class AlignmentCreationType():
    """
    
    """
    pass

class AlignmentCurve(AlignmentEntity):
    """
    The AlignmentCurve class.  This is an abstract base class for other Alignment Entity classes, 
    such as AlignmentArc, AlignmentSCS, and AlignmentLine.
    """
    EndPoint = None
    EndStation = None
    HighestDesignSpeed = None
    Length = None
    StartPoint = None
    StartStation = None

    pass

class AlignmentCurveLabel(Entity):
    """
    This class represents an alignment curve label.
    """

    def Create(self):
        """
        Create(entity: Autodesk.Civil.DatabaseServices.AlignmentArc, labelStyleId: ObjectId) -> AlignmentArc
            Creates a new instance of an AlignmentCurveLabel on an alignment arc entity with the specified label style in the default layer.
            entity: Autodesk.Civil.DatabaseServices.AlignmentArc - The alignment arc entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        Create(subEntityArc: Autodesk.Civil.DatabaseServices.AlignmentSubEntityArc, labelStyleId: ObjectId) -> AlignmentSubEntityArc
            Creates a new instance of an AlignmentCurveLabel on an alignment arc sub-entity with the specified label style in the default layer.
            subEntityArc: Autodesk.Civil.DatabaseServices.AlignmentSubEntityArc - The alignment arc sub-entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        """
        pass
    
    pass

class AlignmentDesignSpeedLabelGroup(Entity):
    """
    This class represents an alignment design speed label group.
    """

    def Create(self):
        """
        Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId
            Creates a new instance of an AlignmentDesignSpeedLabelGroup on an alignment entity with the specified label style.
            styleId: ObjectId - The style of the new AlignmentDesignSpeedLabelGroup.
            alignmentId: ObjectId - The alignment in which the labelgroup is located.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of AlignmentDesignSpeedLabelGroup objects on the Alignment.
            alignmentId: ObjectId - ObjectId of the Alignment where the labels are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectId collection of AlignmentDesignSpeedLabelGroup objects on the alignment.
            alignmentId: ObjectId - ObjectId of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of label.
        """
        pass
    
    pass

class AlignmentEntity(AlignmentCurve):
    """
    The AlignmentEntity class.  
    This is an abstract class from which AlignmentCurve inherits.
    """
    Constraint1 = None
    EntityAfter = None
    EntityBefore = None
    EntityId = None
    EntityType = None
    Item = None
    SubEntityCount = None
    def DesignChecks(self):
        """
        DesignChecks() -> AlignmentDesignCheck
            Gets the collection of applicable design checks.
        """
        pass
    
    
    def Equals(self):
        """
        Equals(obj: System.Object) -> bool
            obj: System.Object
        """
        pass
    
    
    def ValidateDesignCheck(self):
        """
        ValidateDesignCheck(designCheck: Autodesk.Civil.AlignmentDesignCheck) -> AlignmentDesignCheck
            Validate a specific design check on this entity.
            Remarks: This method is only used to check alignment entity with type AlignmentEntityType::SpiralCurve,CurveSpiral,SpiralSpiral,SpiralCurveSpiral.
            designCheck: Autodesk.Civil.AlignmentDesignCheck - The design check to validate
        """
        pass
    
    pass

class AlignmentEntityCollection(object):
    """
    The AlignmentEntity collection class.  This class represents the collection of all AlignmentEntity objects that belong to
    an Alignment.
    """
    Count = None
    FirstEntity = None
    Item = None
    LastEntity = None
    def AddFixedCurve(self):
        """
        AddFixedCurve(previousEntityId: System.Int32, passThroughPoint: Point3d) -> AlignmentArc
            Creates an AlignmentArc entity defined by a previous entity and a pass-through point.
            previousEntityId: System.Int32 - Previous entity identifier.
            passThroughPoint: Point3d - Passthrough point of the AlignmentArc entity.
        AddFixedCurve(passThroughPoint1: Point3d, passThroughPoint2: Point3d, directionAtPassThroughPoint2: Vector3d) -> AlignmentArc
            Creates an AlignmentArc entity defined by an initial pass-through point, a second pass-through point, and a direction at the second pass-through point.
            passThroughPoint1: Point3d - First pass-through point of the AlignmentArc entity (point #1).
            passThroughPoint2: Point3d - Second pass-through point of the AlignmentArc entity (point #2).
            directionAtPassThroughPoint2: Vector3d - Direction at second pass-through point #2.
        AddFixedCurve(centerPoint: Point3d, passThroughPoint: Point3d, isClockwise: System.Boolean) -> AlignmentArc
            Creates an AlignmentArc entity defined by a center point, a pass-through point, and a boolean value that specifies whether the direction is clockwise at the pass-through point.
            centerPoint: Point3d - Center point of the AlignmentArc entity.
            passThroughPoint: Point3d - Passthrough point of the AlignmentArc entity.
            isClockwise: System.Boolean - Specifies whether the AlignmentArc entity is created clockwise (True) or counter-clockwise (False).
        AddFixedCurve(passThroughPoint1: Point3d, directionAtPassThroughPoint1: Vector3d, passThroughPoint2: Point3d) -> AlignmentArc
            Creates an AlignmentArc entity defined by an initial pass-through point, a direction at the initial pass-through point, and a second pass-through point.
            passThroughPoint1: Point3d - First pass-through point of the AlignmentArc entity (point #1).
            directionAtPassThroughPoint1: Vector3d - Direction at first pass-through point #1.
            passThroughPoint2: Point3d - Second pass-through point of the AlignmentArc entity (point #2).
        AddFixedCurve(centerPoint: Point3d, radius: System.Double, isClockwise: System.Boolean) -> AlignmentArc
            Creates an AlignmentArc entity defined by a center point, radius, and boolean value that specifies whether the direction is clockwise.
            centerPoint: Point3d - Center point of the AlignmentArc entity.
            radius: System.Double - Radius of the AlignmentArc entity.
            isClockwise: System.Boolean - Specifies whether the AlignmentArc entity is created clockwise (True) or counter-clockwise (False).
        AddFixedCurve(passThroughPoint1: Point3d, passThroughPoint2: Point3d, radius: System.Double, isClockwise: System.Boolean) -> AlignmentArc
            Creates an AlignmentArc entity defined by an initial pass-through point, a second pass-through point, the radius, and a boolean specifying whether the curve direction is clockwise.
            passThroughPoint1: Point3d - First pass-through point of the AlignmentArc entity (point #1).
            passThroughPoint2: Point3d - Second pass-through point of the AlignmentArc entity (point #2).
            radius: System.Double - Radius of the AlignmentArc entity.
            isClockwise: System.Boolean - Specifies whether the AlignmentArc entity is created clockwise (True) or counter-clockwise (False).
        AddFixedCurve(passThroughPoint1: Point3d, directionAtPassThroughPoint1: Vector3d, radius: System.Double, isClockwise: System.Boolean) -> AlignmentArc
            Creates an AlignmentArc entity defined by an initial pass-through point, a direction at the second pass-through point, the radius, and a boolean indicating whether the curve direction is clockwise.
            passThroughPoint1: Point3d - Passthrough point of the AlignmentArc entity.
            directionAtPassThroughPoint1: Vector3d - Direction at pass-through point.
            radius: System.Double - Radius of the AlignmentArc entity.
            isClockwise: System.Boolean - Specifies whether the AlignmentArc entity is created clockwise (True) or counter-clockwise (False).
        AddFixedCurve(previousEntityId: System.Int32, startPoint: Point3d, middlePoint: Point3d, endPoint: Point3d) -> AlignmentArc
            Creates an AlignmentArc entity defined by a start point, middle point, and end point.
            Remarks: If possible, connect to the previous entity.
            previousEntityId: System.Int32 - Previous entity identifier.
            startPoint: Point3d - Start point of the AlignmentArc entity.
            middlePoint: Point3d - Middle point of the AlignmentArc entity.
            endPoint: Point3d - End point of the AlignmentArc entity.
        AddFixedCurve(previousEntityId: System.Int32, passThroughPoint1: Point3d, passThroughPoint2: Point3d, radius: System.Double, isClockwise: System.Boolean, isGreaterThan180: System.Boolean) -> AlignmentArc
            Creates an AlignmentArc entity defined by an initial pass-through point, a second pass-through point, the radius, a boolean specifying whether the curve direction is clockwise and a boolean specifying whether the AlignmentArc entity is greater than 180 degrees.
            previousEntityId: System.Int32 - Previous entity identifier.
            passThroughPoint1: Point3d - First pass-through point of the AlignmentArc entity (point #1).
            passThroughPoint2: Point3d - Second pass-through point of the AlignmentArc entity (point #2).
            radius: System.Double - Radius of the AlignmentArc entity.
            isClockwise: System.Boolean - Specifies whether the AlignmentArc entity is created clockwise (True) or counter-clockwise (False).
            isGreaterThan180: System.Boolean - Specifies whether the AlignmentArc entity is greater than 180 degrees.
        """
        pass
    
    
    def AddFixedLine(self):
        """
        AddFixedLine(startPoint: Point3d, endPoint: Point3d) -> AlignmentLine
            Creates an AlignmentLine entity defined by a start point and an end point.
            startPoint: Point3d - Start point of the line entity.
            endPoint: Point3d - End point of the line entity.
        AddFixedLine(previousEntityId: System.Int32, distance: System.Double) -> AlignmentLine
            Creates an AlignmentLine entity defined by a previous entity ID and a distance value for the new line.
            Remarks: Use absolute values for distance, so it is valid when distance is negative.
            previousEntityId: System.Int32 - Previous entity identifier.
            distance: System.Double - Distance of the line entity.
        AddFixedLine(previousEntityId: System.Int32, startPoint: Point3d, endPoint: Point3d) -> AlignmentLine
            Creates an AlignmentLine entity defined by a start point and an end point.
            previousEntityId: System.Int32 - Previous entity identifier.
            startPoint: Point3d - Start point of the line entity.
            endPoint: Point3d - End point of the line entity.
        """
        pass
    
    
    def AddFixedSpiral(self):
        """
        AddFixedSpiral(previousEntityId: System.Int32, startPoint: Point3d, spiralPI: Point3d, endPoint: Point3d, definitionType: Autodesk.Civil.SpiralType) -> AlignmentSpiral
            Creates an AlignmentSpiral entity defined by a previous entity, a start point, a point of intersection, an end point and a spiral curvature type.
            previousEntityId: System.Int32 - Previous entity identifier.
            startPoint: Point3d - Start point of the spriral entity.
            spiralPI: Point3d - Point of intersection for the spiral entity.
            endPoint: Point3d - End point of the spriral entity.
            definitionType: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFixedSpiral(previousEntityId: System.Int32, radius: System.Double, length: System.Double, spiralCurveType: Autodesk.Civil.DatabaseServices.SpiralCurveType, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSpiral
            Creates an AlignmentSpiral entity defined by a previous entity, a start point, a point of intersection, a radius, a length, a spiral curvature type and a clockwise indicator.
            Remarks: If possible, connect to the previous entity.
            previousEntityId: System.Int32 - Previous entity identifier.
            radius: System.Double - Radius of the arc entity.
            length: System.Double - Length of the spriral entity.
            spiralCurveType: Autodesk.Civil.DatabaseServices.SpiralCurveType - Specifies the spiral curve type, InCurve or OutCurve.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFixedSpiral(previousEntityId: System.Int32, startRadius: System.Double, endRadius: System.Double, length: System.Double, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSpiral
            Creates an AlignmentSpiral entity defined by a previous entity, a start point, a point of intersection, a start radius, an end radius, a length, a spiral definition, and a clockwise indicator.
            Remarks: If possible, connect to the previous entity.
            previousEntityId: System.Int32 - Previous entity identifier.
            startRadius: System.Double - Start value of the radius of the arc.
            endRadius: System.Double - End value of the radius of the arc.
            length: System.Double - Length of the spiral entity.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFixedSpiral(previousEntityId: System.Int32, startPoint: Point3d, spiralPI: Point3d, radius: System.Double, length: System.Double, spiralCurveType: Autodesk.Civil.DatabaseServices.SpiralCurveType, isClockwise: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSpiral
            Creates an AlignmentSpiral entity defined by a previous entity, a start point, a point of intersection, a radius, a length, a spiral curvature type and a clockwise indicator.
            Remarks: If possible, connect to the previous entity.
            previousEntityId: System.Int32 - Previous entity identifier.
            startPoint: Point3d - Start point of spriral entity.
            spiralPI: Point3d - Point of intersection for spiral entity.
            radius: System.Double - Radius of the arc entity.
            length: System.Double - Length of spriral entity.
            spiralCurveType: Autodesk.Civil.DatabaseServices.SpiralCurveType - Specifies the spiral curve type, InCurve or OutCurve.
            isClockwise: System.Boolean - Specifies whether spiral entity is created clockwise (True) or counter-clockwise (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFixedSpiral(previousEntityId: System.Int32, startPoint: Point3d, spiralPI: Point3d, startRadius: System.Double, endRadius: System.Double, length: System.Double, isClockwise: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSpiral
            Creates a spiral entity defined by a previous entity, a start point, a point of intersection, a start radius, an end radius, a length, a spiral definition, and a clockwise indicator.
            Remarks: If possible, connect to the previous entity.
            previousEntityId: System.Int32 - Previous entity identifier.
            startPoint: Point3d - Start point of the spiral entity.
            spiralPI: Point3d - Point of intersection of the spiral entity.
            startRadius: System.Double - Start value of the radius of the arc.
            endRadius: System.Double - End value of the radius of the arc.
            length: System.Double - Length of the spiral entity.
            isClockwise: System.Boolean - Specifies whether the spiral entity is created clockwise (True) or counter-clockwise (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFloatingArcWithSpiral(self):
        """
        AddFloatingArcWithSpiral(attachEntityId: System.Int32, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType, spParam: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, radius: System.Double, passThroughPoint: Point3d, isGreaterThan180: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSCS
            Adds an AlignmentSCS (SC or CS, Float Arc with Spiral) constrained by a spiral parameter,
            the radius for the circular arc, and a pass-through point for the circular arc.
            attachEntityId: System.Int32 - Previous or next entity identifer.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies the type to attach to the entity.
            spParam: System.Double - Spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the spParam's parameter's type.
            radius: System.Double - Radius of the arc entity.
            passThroughPoint: Point3d - Pass-through point of arc entity.
            isGreaterThan180: System.Boolean - Specifies whether the curve encompasses more than 180 degrees (True) or less than 180 degrees (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFloatingArcWithSpiral(attachEntityId: System.Int32, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType, spParam: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, radius: System.Double, arcLength: System.Double, isClockwise: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSCS
            Add an AlignmentSCS (SC or CS, Float Arc with Spiral) constrained by spiral parameter,
            the radius for the circular arc, and length of the circular arc.
            attachEntityId: System.Int32 - Previous or Next entity identifier.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies the type to attach the entity.
            spParam: System.Double - Spiral parameter(length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the previous parameter-spParam's type.
            radius: System.Double - Radius of the arc entity.
            arcLength: System.Double - Length of the arc.
            isClockwise: System.Boolean - Specifies whether arc entity is created clockwise (True) or counter-clockwise (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFloatingCSS(self):
        """
        AddFloatingCSS(nextEntityId: System.Int32, passThroughPoint1: Point3d, passThroughPoint2: Point3d, sp3Param: System.Double, sp4Param: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSSCSS
            Adds an AlignmentSSCSS (Spiral-Spiral-Curve-Spiral-Spiral group) entity constrained by a next entity, spiral3 and spiral4 parameters,
            two pass through points of the circular arc, and a spiral definition type.
            nextEntityId: System.Int32 - Next entity identifier.
            passThroughPoint1: Point3d - First pass-through point of the arc entity (point #1).
            passThroughPoint2: Point3d - Second pass-through point of the arc entity (point #2).
            sp3Param: System.Double - Third parameter (length or A-value).
            sp4Param: System.Double - Forth parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the spParam parameters' type.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFloatingCSS(nextEntityId: System.Int32, radius: System.Double, passThroughPoint: Point3d, sp3Param: System.Double, sp4Param: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSSCSS
            Adds an AlignmentSSCSS (Spiral-Spiral-Curve-Spiral-Spiral group) entity constrained by a next entity, spiral3 and spiral4 parameters,
            radius for circular arc,  pass through point of the circular arc, and a spiral definition type.
            nextEntityId: System.Int32 - Next entity identifier.
            radius: System.Double - .
            passThroughPoint: Point3d - Pass-through point of the arc entity.
            sp3Param: System.Double - Third parameter (length or A-value).
            sp4Param: System.Double - Forth parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the third and fourth spParam parameters' type.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFloatingCurve(self):
        """
        AddFloatingCurve(passThroughPoint: Point3d, nextEntityId: System.Int32) -> AlignmentArc
            Creates an AlignmentArc entity defined by a next entity, and a pass-through point.
            passThroughPoint: Point3d - Pass-through point of the arc entity.
            nextEntityId: System.Int32 - Next entity identifier.
        AddFloatingCurve(previousEntityId: System.Int32, passThroughPoint: Point3d) -> AlignmentArc
            Creates an AlignmentArc entity defined by a previous entity, and a pass-through point.
            previousEntityId: System.Int32 - Previous entity identifier.
            passThroughPoint: Point3d - Pass-through point of the arc entity.
        AddFloatingCurve(passThroughPoint: Point3d, directionAtPassThroughPoint: Vector3d, nextEntityId: System.Int32) -> AlignmentArc
            Creates an AlignmentArc entity defined by a next entity, a pass-through point, and the direction at the pass-through point.
            passThroughPoint: Point3d - pass-through point of arc entity.
            directionAtPassThroughPoint: Vector3d - Direction at pass-through point.
            nextEntityId: System.Int32 - Next entity identifier.
        AddFloatingCurve(previousEntityId: System.Int32, passThroughPoint: Point3d, directionAtPassThroughPoint: Vector3d) -> AlignmentArc
            Creates an AlignmentArc entity defined by a previous entity, a pass-through point, and the direction at the pass-through point.
            previousEntityId: System.Int32 - Previous entity identifier.
            passThroughPoint: Point3d - Pass-through point of arc entity.
            directionAtPassThroughPoint: Vector3d - Direction at the pass-through point.
        AddFloatingCurve(passThroughPoint: Point3d, radius: System.Double, isGreaterThan180: System.Boolean, curveType: Autodesk.Civil.DatabaseServices.CurveType, nextEntityId: System.Int32) -> AlignmentArc
            Creates an AlignmentArc entity defined by a next entity, a pass-through point, a radius, a boolean value indicating whether or not the curve encompasses more than 180 degrees of a circle, and the curve type.
            passThroughPoint: Point3d - Pass-through point of arc entity.
            radius: System.Double - Radius of the arc entity.
            isGreaterThan180: System.Boolean - Specifies whether the curve encompasses more than 180 degrees (True) or less than 180 degrees (False).
            curveType: Autodesk.Civil.DatabaseServices.CurveType - Specifies the curve type.
            nextEntityId: System.Int32 - Next entity identifier.
        AddFloatingCurve(previousEntityId: System.Int32, passThroughPoint: Point3d, radius: System.Double, isGreaterThan180: System.Boolean, curveType: Autodesk.Civil.DatabaseServices.CurveType) -> AlignmentArc
            Creates an AlignmentArc entity defined by a previous entity, a pass-through point, a radius, a boolean value indicating whether or not the curve encompasses more than 180 degrees of a circle, and the curve type.
            previousEntityId: System.Int32 - Previous entity identifier.
            passThroughPoint: Point3d - pass-through point of arc entity.
            radius: System.Double - Radius of the arc entity.
            isGreaterThan180: System.Boolean - Specifies whether the curve encompasses more than 180 degrees (True) or less than 180 degrees (False).
            curveType: Autodesk.Civil.DatabaseServices.CurveType - Specifies the curve type.
        AddFloatingCurve(previousEntityId: System.Int32, radius: System.Double, paramValue: System.Double, paramType: Autodesk.Civil.DatabaseServices.CurveParamType, isClockwise: System.Boolean) -> AlignmentArc
            Creates an AlignmentArc entity defined by a previous entity, radius, a constraint type and value.
            previousEntityId: System.Int32 - Previous entity identifier.
            radius: System.Double - Radius of the arc entity.
            paramValue: System.Double - Specifies the curve's constraint value.
            paramType: Autodesk.Civil.DatabaseServices.CurveParamType - Specifies the curve's constraint type.
            isClockwise: System.Boolean - Specifies whether arc entity is created clockwise (True) or counter-clockwise (False).
        AddFloatingCurve(radius: System.Double, paramValue: System.Double, paramType: Autodesk.Civil.DatabaseServices.CurveParamType, isClockwise: System.Boolean, nextEntityId: System.Int32) -> AlignmentArc
            Creates an AlignmentArc entity defined by a next entity, radius, a constraint type and value.
            radius: System.Double - Radius of the arc entity.
            paramValue: System.Double - Specifies the curve's constraint value.
            paramType: Autodesk.Civil.DatabaseServices.CurveParamType - Specifies the curve's constraint type.
            isClockwise: System.Boolean - Specifies whether arc entity is created clockwise (True) or counter-clockwise (False).
            nextEntityId: System.Int32 - identifier of the next entity (after the floating arc).
        """
        pass
    
    
    def AddFloatingLine(self):
        """
        AddFloatingLine(passThroughPoint: Point3d, nextEntityId: System.Int32) -> AlignmentLine
            Creates an AlignmentLine entity defined by a next entity and a pass-through point.
            passThroughPoint: Point3d - Passthrough point of the line entity.
            nextEntityId: System.Int32 - Next entity identifier.
        AddFloatingLine(previousEntityId: System.Int32, passThroughPoint: Point3d) -> AlignmentLine
            Creates an AlignmentLine entity defined by a previous entity and a pass-through point.
            previousEntityId: System.Int32 - Previous entity identifier.
            passThroughPoint: Point3d - Passthrough point of the line entity.
        AddFloatingLine(previousEntityId: System.Int32, length: System.Double) -> AlignmentLine
            Creates an AlignmentLine entity defined by a previous entity (to which it is tangent) and a length.
            previousEntityId: System.Int32 - Previous entity identifier.
            length: System.Double - Length of the line entity.
        AddFloatingLine(length: System.Double, nextEntityId: System.Int32) -> AlignmentLine
            Creates an AlignmentLine entity defined by a next entity (to which it is tangent) and a length.
            length: System.Double - Length of the line entity.
            nextEntityId: System.Int32 - Next entity identifier.
        """
        pass
    
    
    def AddFloatingLineWithSpiral(self):
        """
        AddFloatingLineWithSpiral(attachEntityId: System.Int32, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType, spParam: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, passThroughPoint: Point3d, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSTS
            Adds an AlignmentSTS (ST or TS, Float Line with Spiral) entity constrained by a spiral parameter and pass-through point for the line.
            attachEntityId: System.Int32 - Previous or next entity identifer.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whehther attachEntityId is the previous or next entity.
            spParam: System.Double - Spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the spParam parameter's type.
            passThroughPoint: Point3d - Pass-through point of the arc entity.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFloatingLineWithSpiral(attachEntityId: System.Int32, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType, spParam: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, tanLength: System.Double, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSTS
            Adds an AlignmentSTS (ST or TS, Float Line with Spiral) entity constrained by a spiral parameter and line length.
            attachEntityId: System.Int32 - Previous or next entity identifer.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whehther attachEntityId is the previous or next entity.
            spParam: System.Double - Spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the previous parameter-spParam's type.
            tanLength: System.Double - Length of line entity.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFloatingSSC(self):
        """
        AddFloatingSSC(previousEntityId: System.Int32, sp1Param: System.Double, sp2Param: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, passThroughPoint1: Point3d, passThroughPoint2: Point3d, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSSCSS
            Adds an AlignmentSSCSS (Spiral-Spiral-Curve-Spiral-Spiral group) entity constrained by a previous entity, spiral1 and spiral2 parameters,
            two pass through points of the circular arc, and a spiral definition type.
            previousEntityId: System.Int32 - Previous entity identifier.
            sp1Param: System.Double - First spiral parameter (length or A-value).
            sp2Param: System.Double - Second spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the spParam parameters' type.
            passThroughPoint1: Point3d - First pass-through point of the arc entity (point #1).
            passThroughPoint2: Point3d - Second pass-through point of the arc entity (point #2).
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFloatingSSC(previousEntityId: System.Int32, sp1Param: System.Double, sp2Param: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, radius: System.Double, passThroughPoint: Point3d, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSSCSS
            Adds an AlignmentSSCSS (Spiral-Spiral-Curve-Spiral-Spiral group) entity constrained by a previous entity, spiral1 and spiral2 parameters,
            radius for circular arc, pass through point of the circular arc, and a spiral definition type.
            previousEntityId: System.Int32 - Previous entity identifier.
            sp1Param: System.Double - First spiral parameter (length or A-value).
            sp2Param: System.Double - Second spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the spParam parameters' type.
            radius: System.Double - Radius of the arc entity.
            passThroughPoint: Point3d - Pass-through point of the arc entity.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFloatSpiral(self):
        """
        AddFloatSpiral(previousEntityId: System.Int32, radius: System.Double, length: System.Double, isClockwise: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSpiral
            Creates an AlignmentSpiral entity defined by a previous entity, a radius, a length, a clockwise indicator and a spiral definition.
            previousEntityId: System.Int32 - Previous entity identifier.
            radius: System.Double - End radius of the spiral entity.
            length: System.Double - Length of spriral entity.
            isClockwise: System.Boolean - Specifies whether spiral entity is created clockwise (True) or counter-clockwise (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFloatSpiral(radius: System.Double, length: System.Double, nextEntityId: System.Int32, isClockwise: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSpiral
            Creates an AlignmentSpiral entity defined by a radius, a length, a next entity, a clockwise indicator and a spiral definition.
            radius: System.Double - Start radius of the Spiral entity.
            length: System.Double - Length of spriral entity.
            nextEntityId: System.Int32 - Next entity identifier.
            isClockwise: System.Boolean - Specifies whether spiral entity is created clockwise (True) or counter-clockwise (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFreeCurve(self):
        """
        AddFreeCurve(previousEntityId: System.Int32, nextEntityId: System.Int32, passThroughPoint: Point3d) -> AlignmentArc
            Creates a free (dependent on two other subentities) AlignmentArc entity defined by a
            previous entity, a next entity, and a pass-through point.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            passThroughPoint: Point3d - Passthrough point of the AlignmentArc entity.
        AddFreeCurve(previousEntityId: System.Int32, nextEntityId: System.Int32, paramValue: System.Double, paramType: Autodesk.Civil.DatabaseServices.CurveParamType, isGreaterThan180: System.Boolean, curveType: Autodesk.Civil.DatabaseServices.CurveType) -> AlignmentArc
            Creates a free (dependent on two other subentities) arc AlignmentArc defined by a
            previous entity, a next entity, a constraint type and value, a boolean value
            specifying whether the curve encompasses more than 180 degrees, and the curve type.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            paramValue: System.Double - Specifies the curve's constraint value.
            paramType: Autodesk.Civil.DatabaseServices.CurveParamType - Specifies the curve's constraint type.
            isGreaterThan180: System.Boolean - Specifies whether the curve encompasses more than 180 degrees (True) or less than 180 degrees (False).
            curveType: Autodesk.Civil.DatabaseServices.CurveType - Specifies the curve type.
        """
        pass
    
    
    def AddFreeLine(self):
        """
        AddFreeLine(previousEntityId: System.Int32, nextEntityId: System.Int32) -> AlignmentLine
            Creates an AlignmentLine entity defined by two successive elements identified by ID.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
        """
        pass
    
    
    def AddFreeSCS(self):
        """
        AddFreeSCS(previousEntityId: System.Int32, nextEntityId: System.Int32, spiral1Param: System.Double, spiral2Param: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, radius: System.Double, isGreaterThan180: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSCS
            Creates a AlignmentSCS (Spiral-Curve-Spiral group) entity defined by a previous entity, a next entity, the 'A' values of two spirals, and the arc radius.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            spiral1Param: System.Double - First spiral parameter (length or A-value).
            spiral2Param: System.Double - Second spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the first and second spParam parameters' type.
            radius: System.Double - Radius of the arc entity.
            isGreaterThan180: System.Boolean - Specifies whether the curve encompasses more than 180 degrees (True) or less than 180 degrees (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Definition of the spiral.
        """
        pass
    
    
    def AddFreeSCSCS(self):
        """
        AddFreeSCSCS(previousEntityId: System.Int32, nextEntityId: System.Int32, constraintValue: Autodesk.Civil.DatabaseServices.SCSCSConstraints, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSCSCS
            Creates an AlignmentSCSCS (Spiral-Curve-Spiral-Curve-Spiral group) subentity defined by a previous element, a next element, an AeccGeSCSCSConstraints and a spiral definition type .
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            constraintValue: Autodesk.Civil.DatabaseServices.SCSCSConstraints - Specifies the entity constraint value.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFreeSCSSCS(self):
        """
        AddFreeSCSSCS(previousEntityId: System.Int32, nextEntityId: System.Int32, constraintValue: Autodesk.Civil.DatabaseServices.SCSSCSConstraints, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSCSSCS
            Creates an AlignmentSCSSCS (Spiral-Curve-Spiral-Spiral-Curve-Spiral group) subentity defined by a previous element, a next element, an AeccGeSCSCSConstraints and a spiral definition type.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            constraintValue: Autodesk.Civil.DatabaseServices.SCSSCSConstraints - Specifies the entity constraint value.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFreeSpiral(self):
        """
        AddFreeSpiral(previousEntityId: System.Int32, nextEntityId: System.Int32, spParam: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, spiralCurveType: Autodesk.Civil.DatabaseServices.SpiralCurveType, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSCS
            Creates a AlignmentSCS (Spiral-Curve-Spiral group  with a curve and a spiral length is 0) entity defined by a previous entity, a next entity, the lengths or A-Value of spiral, and the spiral type and the definition type.
            Remarks: You can use the AlignmentSCS.SpiralIn or AlignmentSCS.SpiralOut to get the real spiral sub-entity we added.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            spParam: System.Double - Spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the spParam parameter's type.
            spiralCurveType: Autodesk.Civil.DatabaseServices.SpiralCurveType - Specifies the spiral curve type, InCurve or OutCurve.
            spiralDefinition: Autodesk.Civil.SpiralType - Definition of the spiral.
        """
        pass
    
    
    def AddFreeSSBetweenCurves(self):
        """
        AddFreeSSBetweenCurves(previousEntityId: System.Int32, nextEntityId: System.Int32, spRatio: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSTS
            Adds an AlignmentSTS (Spiral-Line-Spiral group with the line length is 0) entity constrained by the two spiral parameters.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            spRatio: System.Double - Specifies spiral1 and spiral2 ratio (length or A-value) .
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the spRatio parameter's type.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def AddFreeSSBetweenTangents(self):
        """
        AddFreeSSBetweenTangents(previousEntityId: System.Int32, nextEntityId: System.Int32, spiral1Param: System.Double, spiral2Param: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, isGreaterThan180: System.Boolean, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSCS
            Creates a AlignmentSCS (Spiral-Curve-Spiral groupwith the curve length is 0) entity defined by a previous entity, a next entity, the 'A' value or Length of two spirals.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            spiral1Param: System.Double - First spiral parameter (length or A-value).
            spiral2Param: System.Double - Second spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the first and second spParam parameters' type.
            isGreaterThan180: System.Boolean - Specifies whether the curve encompasses more than 180 degrees (True) or less than 180 degrees (False).
            spiralDefinition: Autodesk.Civil.SpiralType - Definition of the spiral.
        """
        pass
    
    
    def AddFreeSTS(self):
        """
        AddFreeSTS(previousEntityId: System.Int32, nextEntityId: System.Int32, tanLength: System.Double, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSTS
            Adds an AlignmentSTS (Spiral-Line-Spiral) entity constrained by the line length.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            tanLength: System.Double - Length of the line entity.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        AddFreeSTS(previousEntityId: System.Int32, nextEntityId: System.Int32, sp1Param: System.Double, sp2Param: System.Double, spType: Autodesk.Civil.DatabaseServices.SpiralParamType, spiralDefinition: Autodesk.Civil.SpiralType) -> AlignmentSTS
            Adds an AlignmentSTS (Spiral-Line-Spiral group) entity constrained by the two spiral parameters.
            previousEntityId: System.Int32 - Previous entity identifier.
            nextEntityId: System.Int32 - Next entity identifier.
            sp1Param: System.Double - First spiral parameter (length or A-value).
            sp2Param: System.Double - Second spiral parameter (length or A-value).
            spType: Autodesk.Civil.DatabaseServices.SpiralParamType - Specifies the first and second spParam parameters' type.
            spiralDefinition: Autodesk.Civil.SpiralType - Specifies the spiral definition type.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all alignment entities from the collection.
        """
        pass
    
    
    def EntityAtId(self):
        """
        EntityAtId(id: System.Int32) -> AlignmentEntity
            Returns the AlignmentEntity specified by ID.
            id: System.Int32 - 
            The ID for the AlignmentEntity you want to get.
        """
        pass
    
    
    def EntityAtStation(self):
        """
        EntityAtStation(rawStation: System.Double) -> AlignmentEntity
            Gets the AlignmentEntity at a specified Station in the Alignment.
            rawStation: System.Double - Raw station
        """
        pass
    
    
    def GetEntityByOrder(self):
        """
        GetEntityByOrder(index: System.Int32) -> AlignmentEntity
            Gets an AlignmentEntity at a specified order index along the alignment path. 
            This function behaves like the GUI in that disconnected alignment entities are not considered.
            Remarks: This function can only get AlignmentEntity objects that are connected to the alignment.  
            Connected AlignmentEntity objects have stations, super elevations, etc.
            For example, if you create an alignment which has 3 entities, entity1 and entity2 are connected, but entity3 is disconnected, the function result would be:
            CopyC#1ent = entityCollection.GetEntityByOrder(0);  // ent = entity1
            2ent = entityCollection.GetEntityByOrder(1);  // ent = entity2
            3ent = entityCollection.GetEntityByOrder(2);  // ArgumentException, entity not found
            index: System.Int32 - The index at the alignment path, starting from 0
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> AlignmentEntity
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
        Remove(entity: Autodesk.Civil.DatabaseServices.AlignmentEntity) -> AlignmentEntity
            Removes alignment entity from the collection by the specified entity object.
            entity: Autodesk.Civil.DatabaseServices.AlignmentEntity - Specifies the entity of the AlignmentEntity to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes alignment entity from the collection by the specified index.
            index: System.Int32 - Specifies index in the collection to remove.
        """
        pass
    
    pass

class AlignmentEntityConstraintType():
    """
    Specifies the underlying alignment entity constraint type.
    """
    pass

class AlignmentEntityType():
    """
    Specifies the underlying entity type, for example, tangent, arc, spiral, etc.
    """
    pass

class AlignmentGeometryPointLabelGroup(Entity):
    """
    This class encapsulates the functionality to label a geometry point group in an alignment.
    """

    def Create(self):
        """
        Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId
            Creates a new instance of an AlignmentGeometryPointLabelGroup on an alignment entity with the specified label style.
            styleId: ObjectId - The style of the new AlignmentGeometryPointLabelGroup.
            alignmentId: ObjectId - The alignment in which the labelgroup is located.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of AlignmentGeometryPointLabelGroup objects on the Alignment.
            alignmentId: ObjectId - ObjectId of the Alignment where the labels are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectId collection of AlignmentGeometryPointLabelGroup objects on the alignment.
            alignmentId: ObjectId - ObjectId of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of the label.
        """
        pass
    
    
    def GetGeometryPointsOptions(self):
        """
        GetGeometryPointsOptions() -> GeometryPointSelector
            Gets a GeometryPointSelector containing the state of all AlignmentPointTypes for the current label.
        """
        pass
    
    
    def SetGeometryPointsOptions(self):
        """
        SetGeometryPointsOptions(alignmentGeometryPoints: Autodesk.Civil.GeometryPointSelector) -> GeometryPointSelector
            Sets the state of all AlignmentPointTypes for the current label.
            alignmentGeometryPoints: Autodesk.Civil.GeometryPointSelector
        """
        pass
    
    pass

class AlignmentGeometryPointStationType():
    """
    Defines types of Stations at geometry
    points on an alignment.
    """
    pass

class AlignmentIndexedPILabel(Entity):
    """
    This class represents an alignment point of intersection label.
    """

    def Create(self):
        """
        Create(arc: Autodesk.Civil.DatabaseServices.AlignmentArc, labelStyleId: ObjectId) -> AlignmentArc
            Creates a new instance of an AlignmentIndexedPILabel on an alignment arc entity with the specified label style in the default layer.
            arc: Autodesk.Civil.DatabaseServices.AlignmentArc
            labelStyleId: ObjectId
        Create(tangentIn: Autodesk.Civil.DatabaseServices.AlignmentLine, labelStyleId: ObjectId) -> AlignmentLine
            Creates a new instance of an AlignmentIndexedPILabel on an alignment tangent in entity with the specified label style in the default layer.
            tangentIn: Autodesk.Civil.DatabaseServices.AlignmentLine
            labelStyleId: ObjectId
        Create(scs: Autodesk.Civil.DatabaseServices.AlignmentSCS, labelStyleId: ObjectId) -> AlignmentSCS
            Creates a new instance of an AlignmentIndexedPILabel on an alignment SCS group entity with the specified label style in the default layer.
            scs: Autodesk.Civil.DatabaseServices.AlignmentSCS
            labelStyleId: ObjectId
        """
        pass
    
    pass

class AlignmentLabelGroup(Entity):
    """
    This class represents an alignment label group.
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(rxClass: RXClass, alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of labels on the alignment of a specified type.
            rxClass: RXClass - Type of the labels.
            alignmentId: ObjectId - ObjectId of the Alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of the specified type.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(rxClass: RXClass, alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectId collection of labels on the alignment of a specified type.
            rxClass: RXClass - Type of the labels.
            alignmentId: ObjectId - ObjectId of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of the specified type.
        """
        pass
    
    pass

class AlignmentLine(AlignmentEntity):
    """
    The AlignmentLine class.  
    This class represents an AlignmentEntity made up of a single line subentity.
    """
    Constraint2 = None
    CurveGroupIndex = None
    CurveGroupSubEntityIndex = None
    Direction = None
    Item = None
    Length = None
    MidPoint = None
    PassThroughPoint1 = None
    PassThroughPoint2 = None

    pass

class AlignmentLineConstraintType():
    """
    Defines the underlying line entity constraint type. For example, two points, or through point.
    """
    pass

class AlignmentMinorStationLabelGroup(Entity):
    """
    This class represents an alignment minor station label group.
    """
    MajorStationLabelGroup = None
    RangeEnd = None
    RangeEndFromFeature = None
    RangeStart = None
    RangeStartFromFeature = None
    def Create(self):
        """
        Create(styleId: ObjectId, majorStationId: ObjectId, increment: System.Double) -> ObjectId
            Creates a new instance of an AlignmentMinorStationLabelGroup on an alignment entity with the specified label style.
            styleId: ObjectId - The style ID of the new AlignmentMinorStationLabelGroup.
            majorStationId: ObjectId - ObjectId of major station label group.
            increment: System.Double
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all AlignmentMinorStationLabelGroup objects on the Alignment.
            alignmentId: ObjectId - The ObjectId of the Alignment where the labels are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectId collection of AlignmentMinorStationLabelGroup objects on the alignment.
            alignmentId: ObjectId - The ObjectId of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of the label.
        """
        pass
    
    
    def SetRange(self):
        """
        SetRange(rangeStart: System.Double, rangeEnd: System.Double)
            Sets both range parameters (start and end) at once.
            rangeStart: System.Double
            rangeEnd: System.Double
        """
        pass
    
    pass

class AlignmentMultipleSegments(AlignmentEntity):
    """
    The Alignment MultipleArcs class.
    This class represents an AlignmentEntity made up of several arc or line subentities.
    """
    Constraint2 = None
    Item = None
    SubEntityCount = None

    pass

class AlignmentMultipleSegmentsConstraintType():
    """
    Defines the underlying mutiple arcs entity constraint type.
    """
    pass

class AlignmentPILabel(Entity):
    """
    This class represents an alignment tangent intersection label.
    """

    def Create(self):
        """
        Create(arc: Autodesk.Civil.DatabaseServices.AlignmentArc, labelStyleId: ObjectId) -> AlignmentArc
            Creates a new instance of an AlignmentPILabel on an alignment arc entity with the specified label style in the default layer.
            arc: Autodesk.Civil.DatabaseServices.AlignmentArc - The alignment arc entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        Create(tangentIn: Autodesk.Civil.DatabaseServices.AlignmentLine, labelStyleId: ObjectId) -> AlignmentLine
            Creates a new instance of an AlignmentPILabel on an alignment tangent in entity with the specified label style in the default layer.
            tangentIn: Autodesk.Civil.DatabaseServices.AlignmentLine - The alignment tangent in entity of the PI.
            labelStyleId: ObjectId - The object id of label style for the label.
        Create(scs: Autodesk.Civil.DatabaseServices.AlignmentSCS, labelStyleId: ObjectId) -> AlignmentSCS
            Creates a new instance of an AlignmentPILabel on an alignment SCS group entity with the specified label style in the default layer.
            scs: Autodesk.Civil.DatabaseServices.AlignmentSCS - The alignment scs group entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        """
        pass
    
    pass

class AlignmentRegion(object):
    """
    This class represents a region in an Alignment.
    """
    EndStation = None
    EntryTransition = None
    ExitTransition = None
    IncreasedWidth = None
    Length = None
    Offset = None
    OffsetDist = None
    RegionType = None
    StartStation = None
    WideningCriteria = None
    def Split(self):
        """
        Split()
            Split an AlignmentRegion in half creating a widening region with the second AlignmentRegion.
            Remarks: Split a widening into two widenings sharing one 0-length transition and the right widening is of region type *specific*.
        """
        pass
    
    pass

class AlignmentRegionCollection(object):
    """
    This class represents a collection of AlignmentRegion objects, and it is returned by the Regions property of the OffsetAlignmentInfo object.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> AlignmentRegion
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def MergeToNeighborRegion(self):
        """
        MergeToNeighborRegion(index: System.Int32, preRegion: System.Boolean) -> bool
            Merges the specified region to neighbor region.
            Remarks: When preRegion is false and the input region is the last one, the method won't execute but still return true.When preRegion is true and the input region is the first one, the method won't execute but still return true.You should get a new Count of this collection after executing this method.
            index: System.Int32 - AlignmentRegion index. And the corresponding region's offset will be changed.
            preRegion: System.Boolean - Specify whether merge to previous region or next region.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(index: System.Int32)
            Removes an AlignmentRegion from the collection, which in turn removes the region from the Offset Alignment.
            Remarks: Removing an AlignmentRegion merges it with the previous region and eliminates any transition between them.Removing an AlignmentRegion may invalidate references to AlignmentTransition objects. Therefore, any references to an AlignmentTransition should not be used.Removing an AlignmentRegion may invalidate references to other AlignmentRegion objects in the same collection; therefore, any references held to an AlignmentRegion should not be used.
            index: System.Int32 - AlignmentRegion index.
        """
        pass
    
    pass

class AlignmentRegionType():
    """
    Defines alignment regions.
    """
    pass

class AlignmentSCS(AlignmentEntity):
    """
    The Alignment SpiralCurveSpiral class.
    This class represents an AlignmentEntity made up of an in spiral subentity, 
    an arc subentity, and and out spiral subentity.
    """
    Arc = None
    Constraint2 = None
    SpiralIn = None
    SpiralOut = None

    pass

class AlignmentSCSCS(AlignmentEntity):
    """
    The Alignment SpiralCurveSpiralCurveSpiral class.
    This class represents an AlignmentEntity made up of the 
    following subentities: an in spiral, then an arc, spiral, arc, and out spiral.
    """
    Arc1 = None
    Arc2 = None
    Constraint2 = None
    Spiral1 = None
    Spiral2 = None
    Spiral3 = None

    pass

class AlignmentSCSCSConstraintType():
    """
    Defines the underlying Spiral-Curve-Spiral-Curve-Spiral entity constraint type.
    """
    pass

class AlignmentSCSConstraintType():
    """
    Defines the underlying Spiral-Curve-Spiral entity constraint type.
    """
    pass

class AlignmentSCSSCS(AlignmentEntity):
    """
    The Alignment SpiralCurveSpiralSpiralCurveSpiral class.
    This class represents an AlignmentEntity made up of the following subentities: 
    an in spiral, then an arc, spiral, spiral, arc, and an out spiral.
    """
    Arc1 = None
    Arc2 = None
    Constraint2 = None
    Spiral1 = None
    Spiral2 = None
    Spiral3 = None
    Spiral4 = None

    pass

class AlignmentSCSSCSConstraintType():
    """
    Defines the underlying Spiral-Curve-Spiral-Spiral-Curve-Spiral entity constraint type.
    """
    pass

class AlignmentSSCSS(AlignmentEntity):
    """
    The Alignment SpiralSpiralCurveSpiralSpiral class.
    This class represents an AlignmentEntity made up of the following subentities:
    spiral, spiral, arc, spiral, spiral.
    """
    Arc = None
    Constraint2 = None
    Spiral1 = None
    Spiral2 = None
    Spiral3 = None
    Spiral4 = None

    pass

class AlignmentSSCSSConstraintType():
    """
    Defines the underlying Spiral-Spiral-Curve-SpiralSpiral entity constraint type.
    """
    pass

class AlignmentSTS(AlignmentEntity):
    """
    The Alignment SpiralTangentSpiral class.
    This class represents an AlignmentEntity made up of a spiral, then tangent, then spiral subentities.
    """
    Constraint2 = None
    SpiralIn = None
    SpiralOut = None
    Tangent = None

    pass

class AlignmentSTSConstraintType():
    """
    Defines the underlying Spiral-Line-Spiral entity constraint type.
    """
    pass

class AlignmentSide():
    """
    Alignment side enumeration.  This enum is used by DistanceToAlignment() to specify on which side of the 
    Alignment to look for the target Alignment.  This is required in the situation where the Alignments cross.
    Left and right are relative to a position at the Alignment start
    point facing the end point.
    """
    pass

class AlignmentSpiral(AlignmentEntity):
    """
    The AlignmentSpiral Class.
    AlignmentSpiral derives from the abstract AlignmentCurve class, and 
    represents an AlignmentEntity made up of a single spiral subentity.
    """
    A = None
    Compound = None
    Constraint2 = None
    CurveGroupIndex = None
    CurveGroupSubEntityIndex = None
    CurveType = None
    Delta = None
    Direction = None
    EndDirection = None
    Item = None
    K = None
    Length = None
    LongTangent = None
    MinimumTransitionLength = None
    P = None
    RadialPoint = None
    RadiusIn = None
    RadiusOut = None
    ShortTangent = None
    SPIAngle = None
    SPIPoint = None
    SpiralDefinition = None
    SPIStation = None
    StartDirection = None
    TotalX = None
    TotalY = None

    pass

class AlignmentSpiralConstraintType():
    """
    Defines the underlying spiral entity constraint type. For example, spiral in radius spiral out, spiral length radius pass point.
    """
    pass

class AlignmentSpiralLabel(Entity):
    """
    This class represents an alignment spiral label.
    """

    def Create(self):
        """
        Create(entitySpiral: Autodesk.Civil.DatabaseServices.AlignmentSpiral, labelStyleId: ObjectId) -> AlignmentSpiral
            Creates a new instance of an AlignmentSpiralLabel an alignment spiral entity with the specified label style in the default layer.
            entitySpiral: Autodesk.Civil.DatabaseServices.AlignmentSpiral - The alignment entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        Create(subEntitySpiral: Autodesk.Civil.DatabaseServices.AlignmentSubEntitySpiral, labelStyleId: ObjectId) -> AlignmentSubEntitySpiral
            Creates a new instance of an AlignmentSpiralLabel an alignment spiral sub-entity with the specified label style in the default layer.
            subEntitySpiral: Autodesk.Civil.DatabaseServices.AlignmentSubEntitySpiral - The alignment sub-entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        """
        pass
    
    pass

class AlignmentStationEquationLabelGroup(Entity):
    """
    This class represents an alignment station equation label group.
    """

    def Create(self):
        """
        Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId
            Creates a new instance of an AlignmentStationEquationLabelGroup on an alignment entity with the specified label style.
            styleId: ObjectId - The style of the new AlignmentStationEquationLabelGroup.
            alignmentId: ObjectId - The alignment in which the labelgroup is located.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of AlignmentStationEquationLabelGroup objects on the alignment.
            alignmentId: ObjectId - The ObjectId of the Alignment where the labels are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectId collection of AlignmentStationEquationLabelGroup obects on the alignment.
            alignmentId: ObjectId - The ObjectId of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include the derived lable types.
        """
        pass
    
    pass

class AlignmentStationLabelGroup(Entity):
    """
    This class represents an alignment station label group.
    """
    Increment = None
    RangeEnd = None
    RangeStart = None
    def Create(self):
        """
        Create(styleId: ObjectId, alignmentId: ObjectId, increment: System.Double) -> Autodesk.Civil.DatabaseServices.AlignmentStationLabelGroup.
            Creates a new instance of an AlignmentStationLabelGroup on an alignment entity with the specified label style.
            styleId: ObjectId - The style of the new AlignmentStationLabelGroup.
            alignmentId: ObjectId - The alignment in which the label group is located.
            increment: System.Double - Increment at which to insert major and minor station labels.
        """
        pass
    
    
    def CreateMajor(self):
        """
        CreateMajor(styleId: ObjectId, alignmentId: ObjectId, increment: System.Double) -> ObjectId
            Creates a new instance of an AlignmentStationLabelGroup on an alignment entity with the specified label style.
            styleId: ObjectId - The style of the new AlignmentStationLabelGroup.
            alignmentId: ObjectId - The alignment in which the label group is located.
            increment: System.Double - Increment at which to insert major and minor station labels.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of the specified label type on the alignment.
            alignmentId: ObjectId - The ObjectId of the Alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include derived label types.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of the specified label type on the alignment.
            alignmentId: ObjectId - The ObjectId of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include the derived label types.
        """
        pass
    
    pass

class AlignmentSubEntity(AlignmentSubEntityArc):
    """
    The alignment subentity class.  This class represents the basic drawing components that
    make up an alignment entity.
    """
    CurveGroupIndex = None
    CurveGroupSubEntityIndex = None
    EndPoint = None
    EndStation = None
    Length = None
    StartPoint = None
    StartStation = None
    SubEntityType = None
    def DesignChecks(self):
        """
        DesignChecks() -> AlignmentDesignCheck
            Gets the collection of applicable design checks.
        """
        pass
    
    
    def Equals(self):
        """
        Equals(obj: System.Object) -> bool
            obj: System.Object
        """
        pass
    
    
    def ValidateDesignCheck(self):
        """
        ValidateDesignCheck(designCheck: Autodesk.Civil.AlignmentDesignCheck) -> AlignmentDesignCheck
            Validate a specific design check on this entity.
            designCheck: Autodesk.Civil.AlignmentDesignCheck - The design check to validate
        """
        pass
    
    pass

class AlignmentSubEntityArc(AlignmentSubEntity):
    """
    The Alignment arc subentity class.
    """
    CenterPoint = None
    ChordDirection = None
    ChordLength = None
    Clockwise = None
    DeflectedAngle = None
    Delta = None
    DirectionAtPoint1 = None
    DirectionAtPoint2 = None
    EndDirection = None
    ExternalSecant = None
    ExternalTangent = None
    GreaterThan180 = None
    MidOrdinate = None
    MinimumRadius = None
    PassThroughPoint1 = None
    PassThroughPoint2 = None
    PassThroughPoint3 = None
    PIPoint = None
    PIStation = None
    Radius = None
    ReverseCurve = None
    StartDirection = None
    SubEntityType = None

    pass

class AlignmentSubEntityLine(AlignmentSubEntity):
    """
    The AlignmentSubEntityLine class.  
    This class represents the line object in AlignmentEntity objects.
    """
    Direction = None
    MidPoint = None
    PassThroughPoint1 = None
    PassThroughPoint2 = None
    SubEntityType = None

    pass

class AlignmentSubEntitySpiral(AlignmentSubEntity):
    """
    The Alignment spiral subentity class.
    This class represents spiral object in AlignmentEntity objects.
    """
    A = None
    Compound = None
    CurveType = None
    Delta = None
    Direction = None
    EndDirection = None
    K = None
    LongTangent = None
    MinimumTransitionLength = None
    P = None
    RadialPoint = None
    RadiusIn = None
    RadiusOut = None
    ShortTangent = None
    SPIAngle = None
    SPIPoint = None
    SpiralDefinition = None
    SPIStation = None
    StartDirection = None
    SubEntityType = None
    TotalX = None
    TotalY = None

    pass

class AlignmentSubEntityType():
    """
    Specifies the sub-entity type, for example, line, arc, spiral, etc.
    """
    pass

class AlignmentSuperelevationLabelGroup(Entity):
    """
    This class encapsulates the functionality of an alignment super-elevation group label.
    """

    def Create(self):
        """
        Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId
            Creates a new instance of an AlignmentSuperelevationLabelGroup on an alignment entity with the specified label style.
            styleId: ObjectId - The style of the new AlignmentSuperelevationLabelGroup.
            alignmentId: ObjectId - The alignment in which the label group is located.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of AlignmentSuperelevationLabelGroup objects on the Alignment.
            alignmentId: ObjectId - The ObjectId of the Alignment where the labels are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectId collection of AlignmentSuperelevationLabelGroup objects on the alignment.
            alignmentId: ObjectId - The ObjectId of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include derived label types.
        """
        pass
    
    
    def GetGeometryPointsOptions(self):
        """
        GetGeometryPointsOptions() -> GeometryPointSelector
            Gets a GeometryPointSelector object containing the state of all SuperelevationPointType objects for the current label.
        """
        pass
    
    
    def SetGeometryPointsOptions(self):
        """
        SetGeometryPointsOptions(transitionPoints: Autodesk.Civil.GeometryPointSelector) -> GeometryPointSelector
            Sets the state of all SuperelevationPointType objects for the current label.
            transitionPoints: Autodesk.Civil.GeometryPointSelector
        """
        pass
    
    pass

class AlignmentTable(Entity):
    """
    The AlignmentTable class.
    """


    pass

class AlignmentTangentLabel(Entity):
    """
    This class represents an alignment tangent label.
    """

    def Create(self):
        """
        Create(entityLine: Autodesk.Civil.DatabaseServices.AlignmentLine, labelStyleId: ObjectId) -> AlignmentLine
            Creates a new instance of an AlignmentTangentLabel on an alignment line entity with the specified label style in the default layer.
            entityLine: Autodesk.Civil.DatabaseServices.AlignmentLine - The alignment entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        Create(subEntityLine: Autodesk.Civil.DatabaseServices.AlignmentSubEntityLine, labelStyleId: ObjectId) -> AlignmentSubEntityLine
            Creates a new instance of an AlignmentTangentLabel on an alignment line sub-entity with the specified label style in the default layer.
            subEntityLine: Autodesk.Civil.DatabaseServices.AlignmentSubEntityLine - The alignment sub-entity in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        """
        pass
    
    pass

class AlignmentTransition(object):
    """
    This class represents a transition between two regions in an Alignment.
    """
    NextRegion = None
    PreviousRegion = None
    TransitionDescription = None
    TransitionType = None
    def Slim(self):
        """
        Slim()
            This method sets the TransitionType to TransitionType.Linear and sets the length of the transition to 0.
        """
        pass
    
    pass

class AlignmentTransitionCollection(object):
    """
    This class represents a collection of AlignmentTransition objects, and its returned by the Transitions property of the OffsetAlignmentInfo object.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> AlignmentTransition
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

class AlignmentType():
    """
    
    """
    pass

class AlignmentUpdateType():
    """
    
    """
    pass

class AlignmentVerticalGeometryPointLabelGroup(Entity):
    """
    This class represents an alignment vertical geometry point label group.
    """
    VerticalAlignment = None
    def Create(self):
        """
        Create(styleId: ObjectId, alignmentId: ObjectId, verticalAlignmentId: ObjectId) -> ObjectId
            Creates a new instance of an AlignmentVerticalGeometryPointLabelGroup on an alignment entity with the label style.
            styleId: ObjectId - The style Id of the new AlignmentVerticalGeometryPointLabelGroup.
            alignmentId: ObjectId - ObjectId of the alignment .
            verticalAlignmentId: ObjectId
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of AlignmentVerticalGeometryPointLabelGroup objects on the Alignment.
            alignmentId: ObjectId - The ObjectId of the Alignment where the labels are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an object Id collection of AlignmentVerticalGeometryPointLabelGroup objects on the alignment.
            alignmentId: ObjectId - The object Id of the alignment where the labels are located.
            includeDerived: System.Boolean - Indicates whether to include derived lable types.
        """
        pass
    
    
    def GetGeometryPointsOptions(self):
        """
        GetGeometryPointsOptions() -> GeometryPointSelector
            Gets a GeometryPointSelector object containing the state of all ProfilePointType objects for the current label.
        """
        pass
    
    
    def SetGeometryPointsOptions(self):
        """
        SetGeometryPointsOptions(alignmentVerticalGeometryPoints: Autodesk.Civil.GeometryPointSelector) -> GeometryPointSelector
            Sets the state of all ProfilePointType objects for the current label.
            alignmentVerticalGeometryPoints: Autodesk.Civil.GeometryPointSelector
        """
        pass
    
    pass

class AnchorInfo(object):
    """
    
    """
    pass

class AppliedAssembly(object):
    """
    Represents an AppliedAssembly object. An AppliedAssembly is a cross section of an existing corridor.
    """
    AdjustedElevation = None
    AssemblyId = None
    CorridorId = None
    Links = None
    LinksByCode = None
    Points = None
    PointsByCode = None
    Shapes = None
    ShapesByCode = None
    def GetAppliedSubassemblies(self):
        """
        GetAppliedSubassemblies() -> AppliedSubassemblyCollection
            Gets the collection of AppliedAssemblies in this AppliedAssembly.
        """
        pass
    
    
    def GetLinksByCode(self):
        """
        GetLinksByCode(code: System.String) -> CalculatedLinkCollection
            Gets the collection of CalculatedLinks in this AppliedAssembly that have a particular code.
            code: System.String - Specifies the name of code.
        """
        pass
    
    
    def GetPointsByCode(self):
        """
        GetPointsByCode(code: System.String) -> CalculatedPointCollection
            Gets the collection of CalculatedPoints in this AppliedAssembly that have a particular code.
            code: System.String - Specifies the name of code.
        """
        pass
    
    
    def GetShapesByCode(self):
        """
        GetShapesByCode(code: System.String) -> CalculatedShapeCollection
            Gets the collection of CalculatedShapes in this AppliedAssembly that have a particular code.
            code: System.String - Specifies the name of code.
        """
        pass
    
    pass

class AppliedAssemblyCollection(object):
    """
    The collection of assembly cross sections placed at intervals along corridor baselines.
    """
    CorridorId = None
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> AppliedAssembly
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetItemAt(self):
        """
        GetItemAt(station: System.Double) -> AppliedAssembly
            Gets the AppliedAssembly object nearest the specified station.
            Remarks: Tolerance of station is 1e-4.
            station: System.Double
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def Stations(self):
        """
        Stations() -> double[]
            Gets a list of stations in the collection.
        """
        pass
    
    pass

class AppliedAssemblySetting(object):
    """
    This class is used to get or set the frequency information for applying assembly.
    """
    AdditionalAppliedAssemblies = None
    AppliedAdjacentToOffsetTargetStartEnd = None
    AppliedAtHorizontalGeometryPoints = None
    AppliedAtOffsetTargetGeometryPoints = None
    AppliedAtProfileGeometryPoints = None
    AppliedAtProfileHighLowPoints = None
    AppliedAtSuperelevationCriticalPoints = None
    CorridorAlongCurvesOption = None
    FrequencyAlongCurves = None
    FrequencyAlongProfileCurves = None
    FrequencyAlongSpirals = None
    FrequencyAlongTangents = None
    FrequencyAlongTargetCurves = None
    MODAlongCurves = None
    MODAlongTargetCurves = None
    TargetCurveOption = None
    pass

class AppliedSubassembly(object):
    """
    An AppliedSubassemby object. An AppliedSubassembly is a series of points, links, and shapes that make up part of an AppliedAssembly (corridor cross section).
    """
    BaselineHookedTo = None
    CorridorId = None
    Links = None
    OriginStationOffsetElevationToBaseline = None
    Parameters = None
    Points = None
    Shapes = None
    SubassemblyId = None
    def Contains(self):
        """
        Contains(paramKeyName: System.String) -> bool
            Check if the parameter exists by specified key name.
            paramKeyName: System.String
        """
        pass
    
    
    def GetParameter(T)(self):
        """
        GetParameter(T)(paramKeyName: System.String) -> AppliedSubassemblyParam
            Gets the parameter by specified key name.
            paramKeyName: System.String
        """
        pass
    
    pass

class AppliedSubassemblyCollection(object):
    """
    Collection of AppliedSubassembly objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> AppliedSubassembly
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def ObjectIds(self):
        """
        ObjectIds() -> ObjectId[]
            Gets an array of AppliedSubassemblies' ObjectIds.
        """
        pass
    
    pass

class AppliedSubassemblyParam(object):
    """
    A class used to get or set applied subassembly parameter properties.
    """
    Comment = None
    DesignValue = None
    DesignValueAsObject = None
    DisplayName = None
    IsOverriden = None
    KeyName = None
    Value = None
    ValueAsObject = None
    ValueType = None
    def ClearOverride(self):
        """
        ClearOverride() -> bool
            Clear parameter override.
        """
        pass
    
    pass

class Assembly(Entity):
    """
    Pattern for the cross section of a corridor. Made up of multiple Subassembly objects.
    """
    CodeSetStyleId = None
    CodeSetStyleName = None
    Groups = None
    Location = None
    OffsetAssemblies = None
    StyleId = None
    StyleName = None
    Type = None
    def AddSubassembly(self):
        """
        AddSubassembly(subassemblyId: ObjectId) -> AssemblyGroup
            Adds a subassembly to the assembly.
            subassemblyId: ObjectId - The ObjectId of the source subassembly 
            to be added.
        AddSubassembly(subassemblyId: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Adds a subassembly to the assembly and hooks to the specified point 
            of a subassembly.
            subassemblyId: ObjectId - The ObjectId of the source subassembly 
            to be added.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def CopySubassembly(self):
        """
        CopySubassembly(subassemblyIdFrom: ObjectId) -> AssemblyGroup
            Copies a subassembly to the assembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source 
            subassembly to be copied.
        CopySubassembly(subassemblyIdFrom: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Copies a subassembly to the assembly and hooks to the specified point of a subassembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source subassembly to be copied.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def GetOffsetBaselineNames(self):
        """
        GetOffsetBaselineNames() -> string[]
            Returns all the names of the associated Baseline objects.
        """
        pass
    
    
    def InsertSubassemblyAfter(self):
        """
        InsertSubassemblyAfter(subassemblyId: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Inserts an unassigned subassembly after a subassembly in the 
            assembly and hooks to the specified point.
            Remarks: This method also can be used to insert a subassembly after the 
            subassembly to which no subassembly is hooked.
            subassemblyId: ObjectId - The ObjectId of the source subassembly to be added.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def InsertSubassemblyBefore(self):
        """
        InsertSubassemblyBefore(subassemblyId: ObjectId, targetSubassemblyId: ObjectId)
            Inserts an unassigned subassembly before a subassembly in the assembly.
            subassemblyId: ObjectId - The ObjectId of the subassembly to be 
            inserted before the target subassembly.
            targetSubassemblyId: ObjectId - The ObjectId of the subassembly 
            before which a new subassembly is inserted.
        """
        pass
    
    
    def MirrorSubassembly(self):
        """
        MirrorSubassembly(subassemblyIdFrom: ObjectId) -> AssemblyGroup
            Mirrors a subassembly to the assembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source subassembly to be mirrored.
        MirrorSubassembly(subassemblyIdFrom: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Mirrors a subassembly to the assembly and hooks to the specified point of a subassembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source subassembly to be mirrored.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def ReplaceSubassembly(self):
        """
        ReplaceSubassembly(subassemblyId: ObjectId, targetSubassemblyId: ObjectId)
            Replaces a subassembly in the assembly with another unassigned 
            subassembly.
            subassemblyId: ObjectId - The ObjectId of the subassembly to be 
            added to replace the target subassembly.
            targetSubassemblyId: ObjectId - The ObjectId of the subassembly 
            to be replaced in the assembly.
        """
        pass
    
    pass

class AssemblyCollection(object):
    """
    A collection of Assembly objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(assemblyName: System.String, type: Autodesk.Civil.DatabaseServices.AssemblyType, location: Point3d) -> AssemblyType
            Adds an Assembly object to the AssemblyCollection.
            assemblyName: System.String - Name of the Assembly to be created.
            type: Autodesk.Civil.DatabaseServices.AssemblyType - AssemblyType of the Assembly to be created.
            location: Point3d - Location of the created Assembly.
        Add(assemblyName: System.String, type: Autodesk.Civil.DatabaseServices.AssemblyType, location: Point3d, styleId: ObjectId, codeSetStyleId: ObjectId) -> AssemblyType
            Adds an Assembly object to the AssemblyCollection.
            assemblyName: System.String - Name of the Assembly to be created.
            type: Autodesk.Civil.DatabaseServices.AssemblyType - AssemblyType of the Assembly to be created.
            location: Point3d - Location of the created Assembly.
            styleId: ObjectId - ObjectId of the created Assembly's style.
            codeSetStyleId: ObjectId - ObjectId of the created Assembly's codeSetStyle.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<ObjectId>
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def ImportAssembly(self):
        """
        ImportAssembly(assemblyName: System.String, sourceDatabase: Database, sourceAssemblyName: System.String, location: Point3d) -> ObjectId
            Imports an Assembly object from a database with the name of source assembly.
            assemblyName: System.String - Name of the imported assembly object.
            sourceDatabase: Database - The source database.
            sourceAssemblyName: System.String - The source assembly name.
            location: Point3d - Location of the imported Assembly.
        ImportAssembly(assemblyName: System.String, atcFilePath: System.String, itemId: System.String, location: Point3d) -> ObjectId
            Imports an Assembly object from an atc file specified by its itemId.
            assemblyName: System.String - Name of the imported assembly object.
            atcFilePath: System.String - File path of the atc file.
            itemId: System.String - The itemId of the Assembly in atc file. It should not include the brackets.
            location: Point3d - Location of the imported Assembly.
        """
        pass
    
    pass

class AssemblyGroup(object):
    """
    Represents a group of subassembly objects part of an Assembly.
    """
    Name = None
    def GetSubassemblyIds(self):
        """
        GetSubassemblyIds() -> ObjectIdCollection
            Gets all subassembly ids in the group.
        """
        pass
    
    pass

class AssemblyGroupCollection(object):
    """
    A collection of assembly group.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> AssemblyGroup
            Allows enumerating all the assembly groups in the collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Allows enumerating all the assembly groups in the collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(groupName: System.String) -> bool
            Removes the assembly group with the given name.
            Remarks: After removing an assembly group using this method, all
            references to assembly groups in the collection are invalidated.
            groupName: System.String - Name of the created assembly group.
        Remove(group: Autodesk.Civil.DatabaseServices.AssemblyGroup) -> AssemblyGroup
            Removes the given assembly group.
            Remarks: After removing an assembly group using this method, all
            references to assembly groups in the collection are invalidated.
            group: Autodesk.Civil.DatabaseServices.AssemblyGroup - The created assembly group object.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes an assembly group at the specified index.
            Remarks: After removing an assembly group using this method, all
            references to assembly groups in the collection are invalidated.
            index: System.Int32 - Index of the created assembly group.
        """
        pass
    
    pass

class AssemblyType():
    """
    
    """
    pass

class AttributeTypeInfo(AttributeTypeInfoBool):
    """
    The base class for property type information.  Derived classes define different types of user-defined properties.
    """
    DefaultValue = None
    Description = None
    Name = None
    UseDefaultValue = None
    pass

class AttributeTypeInfoBool(AttributeTypeInfo):
    """
    This class represents property type information for Boolean properties.
    """
    DefaultValue = None
    pass

class AttributeTypeInfoDouble(AttributeTypeInfo):
    """
    This class represents property type information for properties that contain a double value or range.
    """
    DataType = None
    DefaultValue = None
    LowerBoundInclusive = None
    LowerBoundValue = None
    UpperBoundInclusive = None
    UpperBoundValue = None
    pass

class AttributeTypeInfoDoubleDataType():
    """
    An enumeration that specifies the data type of an AttribteTypeInfoDouble object.
    The the format of the data type is determined by the corresponding ambient settings for that type.
    """
    pass

class AttributeTypeInfoEnum(AttributeTypeInfo):
    """
    This class represents property type information for Enumeration user-defined properties.
    """
    DefaultValue = None
    def GetEnumValues(self):
        """
        GetEnumValues() -> string[]
            Gets a String array that contains all the valid enumeration values for the property.
        """
        pass
    
    pass

class AttributeTypeInfoInt(AttributeTypeInfo):
    """
    This class represents property type information for Integer type user-defined properties.
    """
    DefaultValue = None
    LowerBoundInclusive = None
    LowerBoundValue = None
    UpperBoundInclusive = None
    UpperBoundValue = None
    pass

class AttributeTypeInfoString(AttributeTypeInfo):
    """
    This class represents property type information for String-type user-defined properites.
    """
    DefaultValue = None
    pass

class AutoFeatureLabelGroup(Entity):
    """
    The base class for all label group objects that 
    automatically label a range on a feature.
    """
    RangeEnd = None
    RangeEndFromFeature = None
    RangeStart = None
    RangeStartFromFeature = None
    def SetRange(self):
        """
        SetRange(rangeStart: System.Double, rangeEnd: System.Double)
            Sets both range parameters (start and end) at once.
            rangeStart: System.Double
            rangeEnd: System.Double
        """
        pass
    
    pass

class AutoWideningCriteriaInfo(object):
    """
    This class encapsulates the properties that are necessary to add an autowidening from a criteria file.
    It is used by the OffsetAlignmentInfo::AddAutoWidenings() method.
    """
    AttainmentMethod = None
    CriteriaFileName = None
    LaneWidth = None
    LeftLanesCount = None
    MinimumRadiusTableName = None
    RightLanesCount = None
    SpiralPercentForSC = None
    TangentPercentForTC = None
    TransitionLengthTableName = None
    WheelbaseLength = None
    WideningMethod = None
    WideningSide = None
    pass

class AutoWideningInfo(object):
    """
    This class encapsulates the properties that are necessary to add an autowidening manually.
    It is used by the OffsetAlignmentInfo::AddAutoWidenings() method.
    """
    IncreasedWidth = None
    Side = None
    TransitionLength = None
    pass

class BaseBaseline(Baseline):
    """
    The base class for all baseline types.
    """
    AlignmentId = None
    baselineGUID = None
    BaselineType = None
    CorridorId = None
    DirectionAtStation = None
    EndStation = None
    ProfileId = None
    StartStation = None
    def GetDirectionAtStation(self):
        """
        GetDirectionAtStation(station: System.Double) -> Vector3d
            This method returns a Vector3d indicating the direction at the specified station.
            Remarks: This indexer returns a Vector3d that indicates the direction at the 
            specified station. The station value must be in the range 
            StartStation < = station < = EndStation. If the station value provided, fails
            to be in the required range, a zero-length vector is returned.
            station: System.Double - Station at which retrieve the direction.
        """
        pass
    
    
    def IsFeatureLineBased(self):
        """
        IsFeatureLineBased() -> bool
            Indicates whether the specific baseline of corridor is feature line based or not.
            Remarks: Derived classes override this pure virtual function to return whether is a feature line based baseline or not.
        """
        pass
    
    
    def SetAlignmentAndProfile(self):
        """
        SetAlignmentAndProfile(alignmentId: ObjectId, profileId: ObjectId)
            Sets the Alignment and Profile objects associated with this baseline.
            Remarks: This method requires to specify the Alignment and Profile objects for
            a baseline simultaneously. The  reason is because the associated Profile has to
            also be associated with the specified Alignment object. Changing the Alignment 
            will require a change in the Profile, and specifying them individually may leave
            the baseline object in an invalid state.
            But if it is a feature line based corridor, it will fail to set the alignment and profile, and throws an exception whose description is 
            "This operation on feature line based baseline is invalid".
            alignmentId: ObjectId - ObjectId of an Alignment object.
            profileId: ObjectId - ObjectId of a Profile object associated with the specified
            Alignment.
        """
        pass
    
    
    def SortedStations(self):
        """
        SortedStations() -> double[]
            Gets the sorted stations for the baseline.Note: This method doesn't work for
            DREF corridor, in this case, you should first get the applies asemblies and then call Stations() 
            to achieve the similar result.
        """
        pass
    
    
    def StationOffsetElevationToXYZ(self):
        """
        StationOffsetElevationToXYZ(soe: Point3d) -> Point3d
            Returns a world coordinate (in the format X/Y/Z) from a SOE baseline coordinate
            (Station/Offset/Elevation).
            Remarks: This method returns the world coordinate (X/Y/Z) from a specified SOE
            coordinate on a baseline (Station/Offset/Elevation).
            If the specified coordinate cannot be converted because of an invalid
            value in the Station, Offset, or Elevation parameters, the method returns a
            Point3d at the origin (Point3d(0, 0, 0)).
            soe: Point3d - Point3d object in the format Station/Offset/Elevation
        """
        pass
    
    pass

class BaseLineRange():
    """
    
    """
    BaseLineId = None
    EndStation = None
    StartStation = None
    def CheckStationRange(self):
        """
        CheckStationRange()
            Checks that the specified range is within the start and end station of the baseline.
            Remarks: This method verifies whether the specified range is within the start and end station of the baseline. The 
            method will throw an exception if the range is not valid.
        """
        pass
    
    pass

class Baseline(BaseBaseline):
    """
    A 3D path defined by an alignment and a profile.
    """
    AlignmentId = None
    AppliedAssembly = None
    baselineGUID = None
    BaselineRegions = None
    BaselineType = None
    IsProcessed = None
    MainBaselineFeatureLines = None
    Name = None
    NeedsProcessing = None
    OffsetBaselineFeatureLinesCol = None
    ProfileId = None
    def GetAppliedAssemblyAtIndex(self):
        """
        GetAppliedAssemblyAtIndex(index: System.Int32) -> AppliedAssembly
            Gets the AppliedAssembly by index.
            index: System.Int32 - Specified the index at which get the AppliedAssembly.
        """
        pass
    
    
    def GetAppliedAssemblyAtStation(self):
        """
        GetAppliedAssemblyAtStation(station: System.Double) -> AppliedAssembly
            Gets the AppliedAssembly by station.
            Remarks: Tolerance of station is 1e-4.
            station: System.Double - Specifies the station at which get the AppliedAssembly.
        """
        pass
    
    
    def GetTargets(self):
        """
        GetTargets() -> SubassemblyTargetInfoCollection
            Gets the targets information.
        """
        pass
    
    
    def IsFeatureLineBased(self):
        """
        IsFeatureLineBased() -> bool
            Indicates whether the specific baseline of corridor is feature line based or not.
            Remarks: If this baseline is feature line based, then it will return true.
        """
        pass
    
    
    def SetTargets(self):
        """
        SetTargets(updatedTargets: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfoCollection) -> SubassemblyTargetInfoCollection
            Sets the target information. The pass in updatedTargets should be got from method GetTargets().
            updatedTargets: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfoCollection
        """
        pass
    
    
    def SortedStations(self):
        """
        SortedStations() -> double[]
            Returns an array of doubles with the baseline stations sorted. Note: This method doesn't work for
            DREF corridor, in this case, you should first get the applies asemblies and then call Stations() 
            to achieve the similar result.
            Remarks: This method overrides the implementation for Baseline objects.
        """
        pass
    
    
    def UpdateStation(self):
        """
        UpdateStation(station: System.Double)
            Forces the corridor to rebuild at some station.
            Remarks: Rebuilding the Corridor object can be an expensive operation; therefore, caution should be taken when
            invoking this method. It is recommended you perform all modifications to the Corridor object and invoke this
            method as the last operation, as opposed to calling the method after each operation.  Check the IsOutOfDate property to determine
            whether a corridor requires rebuilding.
            station: System.Double
        """
        pass
    
    pass

class BaselineCollection(object):
    """
    A collection of Baseline objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(baselineName: System.String, alignmentId: ObjectId, profileId: ObjectId) -> Baseline
            Adds a baseline with the given baseline name, alignment and profile.
            Remarks: This method adds a new Baseline to the parent Corridor
            object specifying the name for the baseline and the referenced Alignment
            and Profile objects.
            The specified name must be unique for the parent Corridor
            object. Although the name is case-sensitive, it is not recommended to use names that differ only by capitalization.
            The Alignment must exist in the same drawing.
            The Profile must exist in the same drawing and be
            referenced by the specified Alignment object.
            baselineName: System.String -  object to be created.
            alignmentId: ObjectId - .
            profileId: ObjectId - .
        Add(baselineName: System.String, alignmentName: System.String, profileName: System.String) -> Baseline
            Adds a baseline with the given baseline name, alignment and profile.
            Remarks: This method adds a new Baseline to the parent Corridor
            object specifying the name for the baseline and the referenced Alignment
            and Profile objects.
            The specified name must be unique for the parent Corridor
            object. Although the name is case-sensitive, it is not recommended to use names that differ only by capitalization.
            An Alignment with the specified name must exist in the
            drawing.
            A Profile with the specified name must exist in the
            drawing and be referenced by the specified Alignment object.
            baselineName: System.String -  object to be created.
            alignmentName: System.String - .
            profileName: System.String - .
        """
        pass
    
    
    def AddGUIDBaseline(self):
        """
        AddGUIDBaseline(baselineName: System.String, alignmentId: ObjectId, profileId: ObjectId) -> Baseline
            Adds a baseline with the given baseline name, alignment, profile, and GUID.
            Remarks: This method adds a new Baseline to the parent Corridor
            object specifying the name and GUID for the baseline and the referenced Alignment
            and Profile objects.
            The specified name must be unique for the parent Corridor
            object. Although the name is case-sensitive, it is not recommended to use names that differ only by capitalization.
            The Alignment must exist in the same drawing.
            The Profile must exist in the same drawing and be
            referenced by the specified Alignment object.
            baselineName: System.String -  object to be created.
            alignmentId: ObjectId - .
            profileId: ObjectId - .
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> Baseline
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(baselineName: System.String) -> bool
            Removes the Baseline with the given name.
            baselineName: System.String -  to be removed.
        Remove(baseline: Autodesk.Civil.DatabaseServices.Baseline) -> Baseline
            Removes the given Baseline object.
            Remarks: After this method is invoked, the specified Baseline cannot be used any longer.
            baseline: Autodesk.Civil.DatabaseServices.Baseline -  instance to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes the Baseline at the specified index.
            Remarks: The specified index must be in the range 0 < = index < Count.
            index: System.Int32 -  instance to be removed.
        """
        pass
    
    pass

class BaselineFeatureLines(object):
    """
    A collection of multiple feature line collections (FeatureLinesCol) associated with a particular baseline or offset baseline.
    """
    CorridorId = None
    FeatureLineCollectionMap = None
    HardcodedOffsetBaselineName = None
    IsMainBaseline = None
    OffsetAlignmentId = None
    def CodeNames(self):
        """
        CodeNames() -> string[]
            Gets a list of code names in the collection.
        """
        pass
    
    pass

class BaselineFeatureLinesCollection(object):
    """
    A collection of multiple feature line collections (BaselineFeatureLines) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def CodeNames(self):
        """
        CodeNames() -> string[]
            Gets a list of code names in the collection.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> BaselineFeatureLines
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    pass

class BaselineRegion(object):
    """
    A segment of a baseline, specified by alignment stations for the start and end point. In a corridor, each baseline region uses a single assembly type.
    """
    AppliedAssemblies = None
    AppliedAssemblySetting = None
    AssemblyId = None
    CorridorId = None
    EndStation = None
    IsProcessed = None
    Name = None
    NeedsProcessing = None
    OffsetBaselines = None
    StartStation = None
    def AdditionalStations(self):
        """
        AdditionalStations() -> double[]
        """
        pass
    
    
    def AddStation(self):
        """
        AddStation(rawStation: System.Double, description: System.String)
            Adds a station to the BaselineRegion.
            rawStation: System.Double - The station number to add.
            description: System.String - A description of the station.
        """
        pass
    
    
    def ClearAdditionalStations(self):
        """
        ClearAdditionalStations()
        """
        pass
    
    
    def DeleteStation(self):
        """
        DeleteStation(rawStation: System.Double)
            Removes a station from the BaselineRegion.
            rawStation: System.Double - The station number to remove.
        """
        pass
    
    
    def GetOverriddenStations(self):
        """
        GetOverriddenStations() -> OverriddenStationInfo
            Gets the information of the overridden stations.
        """
        pass
    
    
    def GetTargets(self):
        """
        GetTargets() -> SubassemblyTargetInfoCollection
            Gets the targets information.
        """
        pass
    
    
    def Match(self):
        """
        Match(sourceRegion: Autodesk.Civil.DatabaseServices.BaselineRegion, matchOption: Autodesk.Civil.DatabaseServices.RegionMatchType) -> BaselineRegion
            Match the assembly, frequency parameters and target from sourceRegion.
            sourceRegion: Autodesk.Civil.DatabaseServices.BaselineRegion - The region to match.
            matchOption: Autodesk.Civil.DatabaseServices.RegionMatchType - The enum value to specify the way to match by sourceRegion.
        """
        pass
    
    
    def Merge(self):
        """
        Merge(firstRegion: Autodesk.Civil.DatabaseServices.BaselineRegion, lastRegion: Autodesk.Civil.DatabaseServices.BaselineRegion) -> BaselineRegion
            Merges the regions in the range specified by first and last region into current region.
            firstRegion: Autodesk.Civil.DatabaseServices.BaselineRegion - The first region used to specify region range.
            lastRegion: Autodesk.Civil.DatabaseServices.BaselineRegion - The last region used to specify region range.
        """
        pass
    
    
    def RemoveOverriddenStation(self):
        """
        RemoveOverriddenStation(station: System.Double) -> bool
            Removes a overridden station from region.
            station: System.Double - The overridden station to remove.
        """
        pass
    
    
    def SetTargets(self):
        """
        SetTargets(updatedTargets: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfoCollection) -> SubassemblyTargetInfoCollection
            Sets the target information. The pass in updatedTargets should be got from method GetTargets().
            updatedTargets: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfoCollection
        """
        pass
    
    
    def SortedStations(self):
        """
        SortedStations() -> double[]
        """
        pass
    
    
    def Split(self):
        """
        Split(splitStation: System.Double) -> BaselineRegion
            Splits the baseline region.
            Remarks: The splitStation must at least 0.01 greater than start station and 0.01 less than end station.
            The region is split into two regions, the first one (from start station) is the current region and the other is returned as a new region.
            splitStation: System.Double - The station in the region used to split.
        """
        pass
    
    pass

class BaselineRegionCollection(object):
    """
    A collection of baseline region (BaselineRegion) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(regionName: System.String, assemblyId: ObjectId) -> BaselineRegion
            Adds a region with the given region name and assembly after the last region.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Assembly
            regionName: System.String - Name of the created region.
            assemblyId: ObjectId - Object id of the assembly used to create the region.
        Add(regionName: System.String, assemblyName: System.String) -> BaselineRegion
            Adds a region with the given region name and assembly after the last region.
            regionName: System.String - Name of the created region.
            assemblyName: System.String - Name of the assembly used to create the region.
        Add(regionName: System.String, assemblyId: ObjectId, startStation: System.Double, endStation: System.Double) -> BaselineRegion
            Adds a region at the specified start and end station with the given name and assembly.
            regionName: System.String - Name of the created region.
            assemblyId: ObjectId - Object id of the assembly used to create region.
            startStation: System.Double
            endStation: System.Double - The end station used to create region.
        Add(regionName: System.String, assemblyName: System.String, startStation: System.Double, endStation: System.Double) -> BaselineRegion
            Adds a region at the specified start and end station with the given name and assembly.
            regionName: System.String - Name of the created region.
            assemblyName: System.String - Name of the assembly used to create region.
            startStation: System.Double
            endStation: System.Double - The end station used to create region.
        """
        pass
    
    
    def AddRegion(self):
        """
        AddRegion(regionName: System.String, assemblyId: ObjectId) -> BaselineRegion
            Creates a region with the given region name and the assembly object id.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Assembly
            regionName: System.String - Name of the created region.
            assemblyId: ObjectId - Object id of the assembly used to create the region.
        AddRegion(regionName: System.String, assemblyName: System.String) -> BaselineRegion
            Creates a region with the given name.
            regionName: System.String - Name of the created region.
            assemblyName: System.String - Name of the assembly used to create the region.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> BaselineRegion
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf(region: Autodesk.Civil.DatabaseServices.BaselineRegion) -> BaselineRegion
            Gets the specified region index in the collection.
            region: Autodesk.Civil.DatabaseServices.BaselineRegion - The object to locate in the collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(regionName: System.String) -> bool
            Removes a Region with the given region name.
            regionName: System.String - Name of the created region.
        Remove(region: Autodesk.Civil.DatabaseServices.BaselineRegion) -> BaselineRegion
            Removes the given region.
            region: Autodesk.Civil.DatabaseServices.BaselineRegion - The created region object.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a Region by index.
            index: System.Int32 - Index of the created region.
        """
        pass
    
    pass

class BoundingShapeType():
    """
    Specifies bounding shapes for Part objects.
    """
    pass

class CANTCriticalStation(object):
    """
    This class represents a CANT critical station on an Alignment object.
    """
    AppliedCANT = None
    CANTCurveName = None
    LeftRailElevationDifference = None
    ParentAlignmentId = None
    RightRailElevationDifference = None
    Station = None
    StationType = None
    TransitionDescription = None
    TransitionRegionType = None
    pass

class CANTCriticalStationCollection(object):
    """
    This class represents a collection of CANTCriticalStation objects.
    """
    Count = None
    Item = None
    ParentAlignmentId = None
    def Add(self):
        """
        Add(station: System.Double, criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType) -> SuperelevationCriticalStationType
            Adds a CANTCriticalStation of the specified transition type at the specified station.
            station: System.Double - The station value on the alignment object.
            criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType - The type of the critical station.
        Add(station: System.Double, criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType, attainmentRegionType: Autodesk.Civil.SuperelevationAttainmentRegionType) -> SuperelevationCriticalStationType
            Adds a CANTCriticalStation of the specified transition type at the specified station.
            station: System.Double - The station value on the alignment object.
            criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType - The type of the critical station.
            attainmentRegionType: Autodesk.Civil.SuperelevationAttainmentRegionType
        """
        pass
    
    
    def GetCriticalStationAt(self):
        """
        GetCriticalStationAt(station: System.Double, tolerance: System.Double) -> CANTCriticalStation
            Returns the CANTCriticalStation object at the specified station value.
            Remarks: If there is no CANTCriticalStation at the specified station value, the method returns Null.If there more than one CANTCriticalStation objects at the specified station, the method returns the first one in the collection, which is the previous curve bound station.
            station: System.Double - The station value on the alignment object.
            tolerance: System.Double - The tolerance value for the station value.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CANTCriticalStation
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def IsCriticalStation(self):
        """
        IsCriticalStation(station: System.Double, tolerance: System.Double) -> bool
            Returns whether there is a CANTCriticalStation at the specified station value.
            station: System.Double - The station value on the alignment object.
            tolerance: System.Double - The tolerance value for the station value.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes the CANTCriticalStation object from the collection at a specified index.
            index: System.Int32 - The index of critical station obejct in the current collection to be removed.
        """
        pass
    
    pass

class CANTCurve(SECurve):
    """
    
    """

    pass

class CANTCurveCollection(object):
    """
    This class represents a collection of CANTCurve objects.
    """
    Count = None
    Item = None
    ParentAlignmentId = None
    def AddUserDefinedCurve(self):
        """
        AddUserDefinedCurve(startSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity, endSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity) -> CANTCurve
            Adds user defined curve to this collection.
            startSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity - The start sub entity to create CANTCurve.
            endSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity - The end sub entity to create CANTCurve.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CANTCurve
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

class CalculatedLink(CalculatedSubentity):
    """
    The CalculatedLink class.
    """
    CalculatedPoints = None
    CorridorCodes = None
    DrawOverride = None
    pass

class CalculatedLinkCollection(object):
    """
    A calculated link is a collection of calculated points (CalculatedPoint) which are connected to form a line. Calculated shapes (CalculatedShape) are made up of calculated links.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(point1: Autodesk.Civil.DatabaseServices.CalculatedPoint, point2: Autodesk.Civil.DatabaseServices.CalculatedPoint, code: System.String) -> CalculatedLink
            Adds a link with two specified points.
            Remarks: This operation only immediately affects the objects those are from the same AppliedAssembly object or got from Baseline subsequently.
            point1: Autodesk.Civil.DatabaseServices.CalculatedPoint - The first point for the link to be added.
            point2: Autodesk.Civil.DatabaseServices.CalculatedPoint - The second point for the link to be added.
            code: System.String - The code of the newly added link.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CalculatedLink
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(link: Autodesk.Civil.DatabaseServices.CalculatedLink) -> CalculatedLink
            Removes a specified link from the collection.
            Remarks: This operation only immediately affects the objects those are from the same AppliedAssembly object or got from Baseline subsequently.
            link: Autodesk.Civil.DatabaseServices.CalculatedLink - The link needs to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a link specified by index from the collection.
            Remarks: This operation only immediately affects the objects those are from the same AppliedAssembly object or got from Baseline subsequently.
            index: System.Int32 - Index of the link to be removed.
        """
        pass
    
    pass

class CalculatedPoint(CalculatedSubentity):
    """
    A CalculatedPoint is the basic component that defines the stucture of an AppliedSubassembly.
    """
    CorridorCodes = None
    NormalToBaseline = None
    NormalToSubassembly = None
    StationOffsetElevationToBaseline = None
    StationOffsetElevationToSubassembly = None
    pass

class CalculatedPointCollection(object):
    """
    A collection of calculated point (CalculatedPoint) objects. Calculated points are used to define applied subassemblies.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(link: Autodesk.Civil.DatabaseServices.CalculatedLink, code: System.String) -> CalculatedPoint
            Adds a point at the midpoint of a specified link.
            Remarks: This operation only immediately affects the objects those are from the same AppliedAssembly object or got from Baseline subsequently.
            link: Autodesk.Civil.DatabaseServices.CalculatedLink - The link whose midpoint is used to locate the newly added point.
            code: System.String - The code of the newly added point.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CalculatedPoint
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(point: Autodesk.Civil.DatabaseServices.CalculatedPoint) -> CalculatedPoint
            Removes a specified point from the collection.
            Remarks: This operation only immediately affects the objects those are from the same AppliedAssembly object or got from Baseline subsequently.
            point: Autodesk.Civil.DatabaseServices.CalculatedPoint - The point needs to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a point specified by index from the collection.
            Remarks: This operation only immediately affects the objects those are from the same AppliedAssembly object or got from Baseline subsequently.
            index: System.Int32 - Index of the point to be removed.
        """
        pass
    
    pass

class CalculatedShape(CalculatedSubentity):
    """
    A CalculatedShape is defined from links and defines a closed region that represents 
    materials used in a corridor model.
    """
    Area = None
    CalculatedLinks = None
    CorridorCodes = None
    pass

class CalculatedShapeCollection(object):
    """
    Collection of calculated shape (CalculatedShape) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> CalculatedShape
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    pass

class CalculatedSubentity(CalculatedLink):
    """
    Parent class for the CalculatedShape, CalculatedLink and CalculatedPoint interfaces.
    """
    CorridorCodes = None
    CorridorId = None
    SubassemblyBelongedTo = None
    pass

class Catchment(Entity):
    """
    The Catchment class. This class wraps C3D's Catchment entity.
    This class is also used by the
    AeccContextualTabSelectorRules.xaml file to display the Catchment object's
    contextual tab.
    """

    def GetAvailableCatchmentLabelIds(self):
        """
        GetAvailableCatchmentLabelIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of all CatchmentLabels for the Catchment.
        """
        pass
    
    
    def GetAvailableFlowSegmentLabelIds(self):
        """
        GetAvailableFlowSegmentLabelIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of all FlowSegmentLabels for the Catchment.
        """
        pass
    
    
    def GetFlowPath(self):
        """
        GetFlowPath() -> FlowPath
            Get the FlowPath of the Catchment.
        """
        pass
    
    pass

class CatchmentLabel(Entity):
    """
    This class represents a Catchment label.
    """

    def Create(self):
        """
        Create(catchmentId: ObjectId) -> ObjectId
            Creates a new instance of a CatchmentLabel on the specified Catchment with the default label style.
            catchmentId: ObjectId - The ObjectId of the Catchment on which the label is located.
        Create(catchmentId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a CatchmentLabel on the specified Catchment with the specified label style.
            catchmentId: ObjectId - The ObjectId of the Catchment on which the label is located.
            labelStyleId: ObjectId - The ObjectId of a CatchmentLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(catchmentId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of CatchmentLabels on the specified Catchment.
            catchmentId: ObjectId - The ObjectId of the Catchment.
        """
        pass
    
    pass

class CodeCollection(object):
    """
    The Corridor code collection class. The wrapped object could be AeccDbRoadwayState or AeccDbSubassembly.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(code: System.String)
            Adds a new code to the collection.
            code: System.String
        Add(codes: System.String)
            Adds new codes to the collection.
            codes: System.String
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<string>
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(code: System.String) -> bool
            Remove the code from collection.
            code: System.String - 
            Name of the Corridor code.
        """
        pass
    
    
    def TryAdd(self):
        """
        TryAdd(code: System.String) -> bool
            Adds a new code to the collection.
            code: System.String
        TryAdd(codes: System.String)
            Adds new codes to the collection.
            codes: System.String
        """
        pass
    
    pass

class CogoPoint(object):
    """
    Encapsulates a COGO point object and associated information.
    """
    Convergence = None
    DescriptionFormat = None
    Easting = None
    Elevation = None
    ElevationOverride = None
    FullDescription = None
    FullDescriptionOverride = None
    GridEasting = None
    GridNorthing = None
    IsCheckedOut = None
    IsLabelDragged = None
    IsLabelPinned = None
    IsLabelVisible = None
    IsLocked = None
    IsMovable = None
    IsProjectPoint = None
    IsSurveyPoint = None
    LabelLocation = None
    LabelRotation = None
    LabelStyleId = None
    LabelStyleIdOverride = None
    Latitude = None
    LeaderAttachment = None
    LeaderTailVisibility = None
    LeaderVisibility = None
    Location = None
    Longitude = None
    MarkerRotation = None
    Northing = None
    PointName = None
    PointNumber = None
    PrimaryPointGroupId = None
    ProjectVersion = None
    RawDescription = None
    RawDescriptionOverride = None
    Scale = None
    ScaleXY = None
    ScaleZ = None
    ShowToolTip = None
    StyleId = None
    StyleIdOverride = None
    def ApplyDescriptionKeys(self):
        """
        ApplyDescriptionKeys()
            Applies the DescriptionKeys to the CogoPoint.
        """
        pass
    
    
    def ClearAllLabelTextComponentOverrides(self):
        """
        ClearAllLabelTextComponentOverrides()
            Clears all text component overrides in the CogoPoint label.
        """
        pass
    
    
    def ClearLabelTextComponentOverrides(self):
        """
        ClearLabelTextComponentOverrides(labelComponentId: ObjectId)
            Clears the text component overrides on the specified text component in the CogoPoint label.
            labelComponentId: ObjectId - The ObjectId of the text component to clear.
        """
        pass
    
    
    def GetLabelTextComponentIds(self):
        """
        GetLabelTextComponentIds() -> ObjectIdCollection
            Gets an ObjectIdCollection containing the text components in the CogoPoint label.
        """
        pass
    
    
    def GetLabelTextComponentJustificationOverride(self):
        """
        GetLabelTextComponentJustificationOverride(labelComponentId: ObjectId) -> TextJustificationType
            Gets the overriden justification on the specified text component in the CogoPoint label.
            labelComponentId: ObjectId
        """
        pass
    
    
    def GetLabelTextComponentOverride(self):
        """
        GetLabelTextComponentOverride(labelComponentId: ObjectId) -> string
            Gets the overriden text on the specified text component in the CogoPoint label.
            labelComponentId: ObjectId
        """
        pass
    
    
    def GetUDPValue(self):
        """
        GetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPBoolean) -> UDPBoolean
            Gets the value the for the user-defined property with a boolean data type.
            udp: Autodesk.Civil.DatabaseServices.UDPBoolean - The UDP to get the value for.
        GetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPDouble) -> UDPDouble
            Gets the value the for the user-defined property with a double data type.
            udp: Autodesk.Civil.DatabaseServices.UDPDouble - The UDP to get the value for.
        GetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPEnumeration) -> UDPEnumeration
            Gets the value the for the user-defined property with an enumeration data type.
            udp: Autodesk.Civil.DatabaseServices.UDPEnumeration - The UDP to get the value for.
        GetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPInteger) -> UDPInteger
            Gets the value the for the user-defined property with an integer data type.
            udp: Autodesk.Civil.DatabaseServices.UDPInteger - The UDP to get the value for.
        GetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPString) -> UDPString
            Gets the value the for the user-defined property with a string data type.
            udp: Autodesk.Civil.DatabaseServices.UDPString - The UDP to get the value for.
        """
        pass
    
    
    def IsLabelTextComponentOverriden(self):
        """
        IsLabelTextComponentOverriden(labelComponentId: ObjectId) -> bool
            Returns whether the specified text component is overridden in the CogoPoint label.
            labelComponentId: ObjectId - The ObjectId of the text component to query.
        """
        pass
    
    
    def Renumber(self):
        """
        Renumber(newPointNumber: System.UInt32) -> uint
            Renumbers the PointNumber to a new value.
            newPointNumber: System.UInt32
        Renumber(newPointNumber: System.UInt32, resolveType: Autodesk.Civil.DatabaseServices.PointNumberResolveType) -> PointNumberResolveType
            Renumbers the PointNumber to a new value.
            Remarks: If resolveType is PointNumberResolveType.UseNext in duplicate situation, the new PointNumber will be the next valid PointNumber.
            If resolveType is PointNumberResolveType.Overwrite in duplicate situation, the CogoPoint with newPointNumber will be overwrite by current CogoPoint.
            newPointNumber: System.UInt32 - Specified the new pointNumer.
            resolveType: Autodesk.Civil.DatabaseServices.PointNumberResolveType - Specified the way to resolve the point number duplication situation.
        """
        pass
    
    
    def ResetLabel(self):
        """
        ResetLabel()
            Resets the CogoPoint label object to its defaults.
        """
        pass
    
    
    def ResetLabelLocation(self):
        """
        ResetLabelLocation()
            Resets the location of the CogoPoint label object to its defaults.
        """
        pass
    
    
    def ResetLabelRotation(self):
        """
        ResetLabelRotation()
            Resets the rotation status of the CogoPoint label object to its defaults.
        """
        pass
    
    
    def SetLabelTextComponentJustificationOverride(self):
        """
        SetLabelTextComponentJustificationOverride(labelComponentId: ObjectId, textJustificationType: Autodesk.Civil.TextJustificationType) -> TextJustificationType
            Overrides the justification on the specified text component in the CogoPoint label.
            labelComponentId: ObjectId - The ObjectId of the text component.
            textJustificationType: Autodesk.Civil.TextJustificationType - The type of text justification to set.
        """
        pass
    
    
    def SetLabelTextComponentOverride(self):
        """
        SetLabelTextComponentOverride(labelComponentId: ObjectId, textOverride: System.String)
            Overrides the text on the specified text component in the CogoPoint label.
            labelComponentId: ObjectId - The ObjectId of the text component.
            textOverride: System.String - The overriden label text.
        """
        pass
    
    
    def SetUDPValue(self):
        """
        SetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPBoolean, value: System.Boolean) -> UDPBoolean
            Sets the value the for the user-defined property with a boolean data type.
            udp: Autodesk.Civil.DatabaseServices.UDPBoolean - The UDP to set the value for.
            value: System.Boolean - The boolean to set the UDP value to.
        SetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPDouble, value: System.Double) -> UDPDouble
            Sets the value the for the user-defined property with a double data type.
            udp: Autodesk.Civil.DatabaseServices.UDPDouble - The UDP to set the value for.
            value: System.Double - The double to set the UDP value to.
        SetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPEnumeration, value: System.String) -> UDPEnumeration
            Sets the value the for the user-defined property with an enumeration data type.
            udp: Autodesk.Civil.DatabaseServices.UDPEnumeration - The UDP to set the value for.
            value: System.String - The enumeration value to set the UDP value to.
        SetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPInteger, value: System.Int32) -> UDPInteger
            Sets the value the for the user-defined property with an integer data type.
            udp: Autodesk.Civil.DatabaseServices.UDPInteger - The UDP to set the value for.
            value: System.Int32 - The integer to set the UDP value to.
        SetUDPValue(udp: Autodesk.Civil.DatabaseServices.UDPString, value: System.String) -> UDPString
            Sets the value the for the user-defined property with a string data type.
            udp: Autodesk.Civil.DatabaseServices.UDPString - The UDP to set the value for.
            value: System.String - The string to set the UDP value to.
        """
        pass
    
    pass

class CogoPointCollection(object):
    """
    This class encapsulates a collection of CogoPoint objects.
    """
    Count = None
    def Add(self):
        """
        Add(location: Point3d, useNextPointNumSetting: System.Boolean) -> ObjectId
            Adds a new CogoPoint at the given location.
            Remarks: The created CogoPoint's Description is empty.
            location: Point3d - The location of the new CogoPoint.
            useNextPointNumSetting: System.Boolean
        Add(locations: Point3dCollection, useNextPointNumSetting: System.Boolean) -> ObjectIdCollection
            Adds new CogoPoints at the given locations.
            Remarks: The CogoPoints created with this method have empty Descriptions.
            locations: Point3dCollection - The locations of the new CogoPoints.
            useNextPointNumSetting: System.Boolean
        Add(location: Point3d, desc: System.String, useNextPointNumSetting: System.Boolean) -> ObjectId
            Adds a new CogoPoint at the given location with the specified description information.
            location: Point3d - The location of the new CogoPoint.
            desc: System.String - The description of the new CogoPoint.
            useNextPointNumSetting: System.Boolean
        Add(locations: Point3dCollection, desc: System.String, useNextPointNumSetting: System.Boolean) -> ObjectIdCollection
            Adds new CogoPoints at the given locations with the given description information.
            locations: Point3dCollection - A collection of 3d points specifying the locations of the new CogoPoints.
            desc: System.String - The description of the new CogoPoints.
            useNextPointNumSetting: System.Boolean
        Add(location: Point3d, desc: System.String, useDescriptionKey: System.Boolean, matchOnParams: System.Boolean, useNextPointNumSetting: System.Boolean) -> ObjectId
            Adds a new CogoPoint at the given location with the specified description information, optionally using a DescriptionKey.
            Remarks: If useDescriptionKey is set to false, the behavior of this method is equal to Add(location, desc).
            location: Point3d - The location of the new CogoPoint.
            desc: System.String - The description of the new CogoPoint.
            useDescriptionKey: System.Boolean - Specifies whether to use the DescriptionKey.
            matchOnParams: System.Boolean - Specifies whether parameters are used in description key matching to rotate and scale the point symbol.
            useNextPointNumSetting: System.Boolean
        Add(locations: Point3dCollection, desc: System.String, useDescriptionKey: System.Boolean, matchOnParams: System.Boolean, useNextPointNumSetting: System.Boolean) -> ObjectIdCollection
            Adds new CogoPoints at the given locations with the given description information, optionally using a DescriptionKey.
            Remarks: If useDescriptionKey is set to false, the behavior of this method is equal to Add(locations, desc).
            locations: Point3dCollection - A collection of 3d points specifying the locations of the new CogoPoints.
            desc: System.String - The description of the new CogoPoints.
            useDescriptionKey: System.Boolean - Specifies whether to use the DescriptionKey.
            matchOnParams: System.Boolean - Specifies whether parameters are used in description key matching to rotate and scale the point symbol.
            useNextPointNumSetting: System.Boolean
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all CogoPoints from the collection.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(pointNumber: System.UInt32) -> bool
            Determines whether the collection contains a CogoPoint with the given pointNumber.
            pointNumber: System.UInt32
        """
        pass
    
    
    def ExportPoints(self):
        """
        ExportPoints(pointFileFullName: System.String, fileFormat: GetPointFileFormats()) -> PointFileFormat
            Exports points to a point file.
            Remarks: useAdjustedElevation and shouldExpandCoordinateData are disregarded if they are not supported by the specified point file format.If the file specified by pointFileFullName already exists, it is overwritten.If the file specified by pointFileFullName does not exist, it is created automatically.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: GetPointFileFormats() - .
        ExportPoints(pointFileFullName: System.String, fileFormat: GetPointFileFormats(), pointGroupId: ObjectId) -> PointFileFormat
            Exports points in the specified PointGroup to a point file.
            Remarks: If the file specified by pointFileFullName already exists, it is overwritten.If the file specified by pointFileFullName does not exist, it is created automatically.Set the pointGroupId to ObjectId::Null to export all points.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: GetPointFileFormats() - .
            pointGroupId: ObjectId - The ObjectId of the PointGroup from which the CogoPoints are exported.
        ExportPoints(pointFileFullName: System.String, fileFormat: GetPointFileFormats(), useAdjustedElevation: System.Boolean, shouldTransformCoordinate: System.Boolean, shouldExpandCoordinateData: System.Boolean) -> PointFileFormat
            Exports points to a point file with advanced options.
            Remarks: useAdjustedElevation and shouldExpandCoordinateData are disregarded if they are not supported by the specified point file format.If the file specified by pointFileFullName already exists, it is overwritten.If the file specified by pointFileFullName does not exist, it is created automatically.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: GetPointFileFormats() - .
            useAdjustedElevation: System.Boolean - Specifies whether to adjust the point elevation values.
            shouldTransformCoordinate: System.Boolean - Specifies whether to transform the points in the file.
            shouldExpandCoordinateData: System.Boolean - Specifies whether to calculate the coordinate data properties of the points, such as degrees, minutes, seconds, and hemisphere for latitude and longitude.
        ExportPoints(pointFileFullName: System.String, fileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat, useAdjustedElevation: System.Boolean, shouldTransformCoordinate: System.Boolean, shouldExpandCoordinateData: System.Boolean, pointGroupId: ObjectId) -> PointFileFormat
            Exports points in specified PointGroup to a point file with advanced options.
            Remarks: useAdjustedElevation and shouldExpandCoordinateData are disregarded if they are not supported by the specified point file format.If the file specified by pointFileFullName already exists, it is overwritten.If the file specified by pointFileFullName does not exist, it is created automatically.Set the pointGroupId to ObjectId::Null to export all points.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat - The file format for the point file.  You can get a collection of supported point file formats by using PointFileFormatCollection.GetPointFileFormats().
            useAdjustedElevation: System.Boolean - Specifies whether to adjust the point elevation values.
            shouldTransformCoordinate: System.Boolean - Specifies whether to transform the points in the file.
            shouldExpandCoordinateData: System.Boolean - Specifies whether to calculate the coordinate data properties of the points, such as degrees, minutes, seconds, and hemisphere for latitude and longitude.
            pointGroupId: ObjectId - The ObjectId of the PointGroup from which the CogoPoints are exported.
        """
        pass
    
    
    def GetCogoPoints(self):
        """
        GetCogoPoints(pDatabase: Database) -> CogoPointCollection
            Gets the CogoPointCollection object containing all the CogoPoints in a drawing.
            pDatabase: Database
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<ObjectId>
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator that can be used to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator that can be used to enumerate this collection.
        """
        pass
    
    
    def GetPointByPointNumber(self):
        """
        GetPointByPointNumber(pointNumber: System.UInt32) -> ObjectId
            Gets the ObjectId of a CogoPoint by a given pointNumber.
            Remarks: Use the Contains(UInt32) method to determine whether the collection contains a point with the given point number.
            pointNumber: System.UInt32 - The point number to get.
        """
        pass
    
    
    def ImportPoints(self):
        """
        ImportPoints(pointFileFullName: System.String, fileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat) -> PointFileFormat
            Imports points from a point file.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat - The file format for the point file.  You can get a collection of supported point file formats by using PointFileFormatCollection.GetPointFileFormats().
        ImportPoints(pointFileFullName: System.String, fileFormat: GetPointFileFormats(), pointGroupId: ObjectId) -> PointFileFormat
            Imports points from a point file to an existing PointGroup.
            Remarks: Set the pointGroupId to ObjectId::Null to specify that the imported points are not added to a PointGroup.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: GetPointFileFormats() - .
            pointGroupId: ObjectId - The ObjectId of the PointGroup into which the CogoPoints are imported.
        ImportPoints(pointFileFullName: System.String, fileFormat: GetPointFileFormats(), useAdjustedElevation: System.Boolean, shouldTransformCoordinate: System.Boolean, shouldExpandCoordinateData: System.Boolean) -> PointFileFormat
            Imports points from a point file with advanced options.
            Remarks: useAdjustedElevation and shouldExpandCoordinateData are disregarded if they are not supported by the specified point file format.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: GetPointFileFormats() - .
            useAdjustedElevation: System.Boolean - Specifies whether to adjust the point elevation values.
            shouldTransformCoordinate: System.Boolean - Specifies whether to transform the points in the file.
            shouldExpandCoordinateData: System.Boolean - Specifies whether to calculate the coordinate data properties of the points, such as degrees, minutes, seconds, and hemisphere for latitude and longitude.
        ImportPoints(pointFileFullName: System.String, fileFormat: GetPointFileFormats(), useAdjustedElevation: System.Boolean, shouldTransformCoordinate: System.Boolean, shouldExpandCoordinateData: System.Boolean, pointGroupId: ObjectId) -> PointFileFormat
            Imports points from a point file to an existing PointGroup with advanced options.
            Remarks: useAdjustedElevation and shouldExpandCoordinateData are disregarded if they are not supported by the specified point file format.Set the pointGroupId to ObjectId::Null to specify that the imported points are not added to a PointGroup.
            pointFileFullName: System.String - The full path and name of the point file.
            fileFormat: GetPointFileFormats() - .
            useAdjustedElevation: System.Boolean - Specifies whether to adjust the point elevation values.
            shouldTransformCoordinate: System.Boolean - Specifies whether to transform the points in the file.
            shouldExpandCoordinateData: System.Boolean - Specifies whether to calculate the coordinate data properties of the points, such as degrees, minutes, seconds, and hemisphere for latitude and longitude.
            pointGroupId: ObjectId - The ObjectId of the PointGroup into which the CogoPoints are imported.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(pointId: ObjectId)
            Removes the specified CogoPoint from the collection.
            pointId: ObjectId
        Remove(pointNumber: System.UInt32)
            Removes the CogoPoint with the given pointNumber from the collection.
            Remarks: This method does not throw an exception if called with a pointNumber that does not exist in the collection.
            pointNumber: System.UInt32
        """
        pass
    
    
    def SetDescriptionFormat(self):
        """
        SetDescriptionFormat(pointId: ObjectId, descFormat: System.String) -> ObjectId
            Sets the DescriptionFormat property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the DescriptionFormat property for.
            descFormat: System.String - The new DescriptionFormat value.
        SetDescriptionFormat(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the DescriptionFormat property for multiple CogoPoints with different values.
            Remarks: If there are fewer strings than points, only the first n points in the list will have their DescriptionFormat property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the DescriptionFormat property for.
            values: System.Collections.Generic.IEnumerable - A sequence of strings to set the corresponding point's DescriptionFormat property to.
        SetDescriptionFormat(pointIds: System.Collections.Generic.IEnumerable, descFormat: System.String) -> ObjectIdCollection
            Sets the DescriptionFormat property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the DescriptionFormat property for.
            descFormat: System.String - The new DescriptionFormat value.
        """
        pass
    
    
    def SetEasting(self):
        """
        SetEasting(pointId: ObjectId, easting: System.Double) -> ObjectId
            Sets the Easting property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the Easting property for.
            easting: System.Double - The new Easting value.
        SetEasting(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the Easting property for multiple CogoPoints with different values.
            Remarks: If there are fewer doubles than points, only the first n points in the list will have their Easting property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the Easting property for.
            values: System.Collections.Generic.IEnumerable - A sequence of doubles to set the corresponding point's Easting property to.
        SetEasting(pointIds: System.Collections.Generic.IEnumerable, easting: System.Double) -> ObjectIdCollection
            Sets the Easting property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the Easting property for.
            easting: System.Double - The new Easting value.
        """
        pass
    
    
    def SetElevation(self):
        """
        SetElevation(pointId: ObjectId, elevation: System.Double) -> ObjectId
            Sets Elevation for a single CogoPoint.
            Remarks: If you want to set the elevation to the state of "Has not beet set" for the CogoPoint, set the elevation to Double.NaN.
            pointId: ObjectId - The ObjectId of the point you want to set the elevation for.
            elevation: System.Double - The new elevation value.  Specify Double.NaN to unset the elevation.
        SetElevation(pointIds: System.Collections.Generic.IEnumerable, elevations: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the elevation for multiple CogoPoints with different elevation values.
            Remarks: If you want to set to the state of "Has not beet set" for all the CogoPoints, 
            set the elevation to Double.NaN.If there are fewer elevations than points, only the first n points in the list will have their elevation
            set, where n is the number of elevations specified.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds for the points you want to set the elevation for.
            elevations: System.Collections.Generic.IEnumerable
        SetElevation(pointIds: System.Collections.Generic.IEnumerable, elevation: System.Double) -> ObjectIdCollection
            Sets Elevation for multiple CogoPoints with the same elevation.
            Remarks: If you want to set the elevation to the state of "Has not beet set" for the CogoPoints, set the elevation to Double.NaN.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds for the points you want to set the elevation for.
            elevation: System.Double - The new elevation value.  Specify Double.NaN to unset the elevation.
        """
        pass
    
    
    def SetElevationByOffset(self):
        """
        SetElevationByOffset(pointId: ObjectId, offset: System.Double) -> ObjectId
            Sets the elevation for a single CogoPoint using an offset value.
            pointId: ObjectId - The ObjectId of the point you want to set the elevation for.
            offset: System.Double - An offset value to apply to the point's current elevation.
        SetElevationByOffset(pointIds: System.Collections.Generic.IEnumerable, offsets: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets Elevation for multiple CogoPoints with different elevation values.
            Remarks: If there are fewer offsets than points, only the first n points in the list will have their elevation
            set, where n is the number of offsets specified.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the elevation for.
            offsets: System.Collections.Generic.IEnumerable - A sequence of offset values to apply to each corresponding point's current elevation.
        SetElevationByOffset(pointIds: System.Collections.Generic.IEnumerable, offset: System.Double) -> ObjectIdCollection
            Sets the elevation for multiple CogoPoints with the same elevation using an offset value.
            pointIds: System.Collections.Generic.IEnumerable
            offset: System.Double - An offset value to apply to each point's current elevation.
        """
        pass
    
    
    def SetElevationBySurface(self):
        """
        SetElevationBySurface(pointId: ObjectId, surfaceId: ObjectId) -> ObjectId
            Sets the elevation for a single CogoPoint with the elevation obtained from a specified surface.
            pointId: ObjectId - The ObjectId of the point you want to set the elevation for.
            surfaceId: ObjectId - The ObjectId of the Surface object you want to get the elevation from.
        SetElevationBySurface(pointIds: System.Collections.Generic.IEnumerable, surfaceId: ObjectId) -> ObjectIdCollection
            Sets the elevation for multiple CogoPoints with elevation values obtained from a specified surface.
            pointIds: System.Collections.Generic.IEnumerable - A list of ObjectIds of the points you want to set the elevation for.
            surfaceId: ObjectId - The ObjectId of the Surface object you want to get the elevation from.
        """
        pass
    
    
    def SetIsLocked(self):
        """
        SetIsLocked(pointId: ObjectId, isLocked: System.Boolean) -> ObjectId
            Sets the IsLocked property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the IsLocked property for.
            isLocked: System.Boolean - The new isLocked value.
        SetIsLocked(pointIds: System.Collections.Generic.IEnumerable, isLocked: System.Boolean) -> ObjectIdCollection
            Sets the IsLocked property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the IsLocked property for.
            isLocked: System.Boolean - The new isLocked value.
        SetIsLocked(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets IsLocked for multiple CogoPoints with different values.
            Remarks: If there are fewer booleans than points, only the first n points in the list will have their IsLocked property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the IsLocked property for.
            values: System.Collections.Generic.IEnumerable - A sequence of booleans to set the corresponding point's IsLocked property to.
        """
        pass
    
    
    def SetLabelRotation(self):
        """
        SetLabelRotation(pointId: ObjectId, rotation: System.Double) -> ObjectId
            Sets the LabelRotation property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the LabelRotation property for.
            rotation: System.Double - The new LabelRotation value.
        SetLabelRotation(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the LabelRotation property for multiple CogoPoints with different values.
            Remarks: If there are fewer doubles than points, only the first n points in the list will have their LabelRotation property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the LabelRotation property for.
            values: System.Collections.Generic.IEnumerable - A sequence of doubles to set the corresponding point's LabelRotation property to.
        SetLabelRotation(pointIds: System.Collections.Generic.IEnumerable, rotation: System.Double) -> ObjectIdCollection
            Sets the LabelRotation property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the LabelRotation property for.
            rotation: System.Double - The new LabelRotation value.
        """
        pass
    
    
    def SetLabelStyleId(self):
        """
        SetLabelStyleId(pointId: ObjectId, styleId: ObjectId) -> ObjectId
            Sets the LabelStyleId for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the LabelStyleId property for.
            styleId: ObjectId - The ObjectId of the style you want to set LabelStyleId to (object type LabelStyle).
        SetLabelStyleId(pointIds: System.Collections.Generic.IEnumerable, styleId: ObjectId) -> ObjectIdCollection
            Sets the LabelStyleId for multiple CogoPoints with the same style.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the LabelStyleId for.
            styleId: ObjectId - The ObjectId of the style you want to set the LabelStyleId to (object type LabelStyle).
        SetLabelStyleId(pointIds: System.Collections.Generic.IEnumerable, styleIds: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the LabelStyleId for multiple CogoPoints with different styles.
            Remarks: If there are fewer LabelStyleIds than points, only the first n points in the list will have their LabelStyleId property
            set, where n is the number of LabelStyleIds specified.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the LabelStyleId for.
            styleIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the LabelStyles you want to set the corresponding point's LabelStyleId to.
        """
        pass
    
    
    def SetMarkerRotation(self):
        """
        SetMarkerRotation(pointId: ObjectId, rotation: System.Double) -> ObjectId
            Sets the MarkerRotation property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the MarkerRotation property for.
            rotation: System.Double - The new MarkerRotation value.
        SetMarkerRotation(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the MarkerRotation property for multiple CogoPoints with different values.
            Remarks: If there are fewer doubles than points, only the first n points in the list will have their MarkerRotation property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the MarkerRotation property for.
            values: System.Collections.Generic.IEnumerable - A sequence of doubles to set the corresponding point's MarkerRotation property to.
        SetMarkerRotation(pointIds: System.Collections.Generic.IEnumerable, rotation: System.Double) -> ObjectIdCollection
            Sets the MarkerRotation property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the MarkerRotation property for.
            rotation: System.Double - The new MarkerRotation value.
        """
        pass
    
    
    def SetNorthing(self):
        """
        SetNorthing(pointId: ObjectId, northing: System.Double) -> ObjectId
            Sets the Northing property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the Northing property for.
            northing: System.Double
        SetNorthing(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the Northing property for multiple CogoPoints with different values.
            Remarks: If there are fewer doubles than points, only the first n points in the list will have their Northing property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the Northing property for.
            values: System.Collections.Generic.IEnumerable - A sequence of doubles to set the corresponding point's Northing property to.
        SetNorthing(pointIds: System.Collections.Generic.IEnumerable, northing: System.Double) -> ObjectIdCollection
            Sets the Northing property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the Northing property for.
            northing: System.Double - The new Northing value.
        """
        pass
    
    
    def SetPointName(self):
        """
        SetPointName(pointId: ObjectId, name: System.String) -> ObjectId
            Sets the PointName property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the PointName property for.
            name: System.String
        SetPointName(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the PointName property for multiple CogoPoints with different values.
            Remarks: If there are fewer strings than points, only the first n points in the list will have their PointName property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the PointName property for.
            values: System.Collections.Generic.IEnumerable - A sequence of strings to set the corresponding point's PointName property to.
        """
        pass
    
    
    def SetPointNumber(self):
        """
        SetPointNumber(pointId: ObjectId, pointNumber: System.UInt32) -> ObjectId
            Sets the PointNumber for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the PointNumber for.
            pointNumber: System.UInt32 - The new PointNumber value.
        SetPointNumber(pointIds: System.Collections.Generic.IEnumerable, additiveFactor: System.Int32) -> ObjectIdCollection
            Sets the PointNumber for multiple CogoPoints with different values.
            Remarks: The order of the input pointIds will be changed. The returned value's order will not be the same as the input pointIds.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points to set the PointNumber for.
            additiveFactor: System.Int32 - The offset value that will be added to the original PointNumber for each subsequent point.
        """
        pass
    
    
    def SetRawDescription(self):
        """
        SetRawDescription(pointId: ObjectId, rawDesc: System.String) -> ObjectId
            Sets the RawDescription property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the RawDescription property for.
            rawDesc: System.String - The new RawDescription value.
        SetRawDescription(pointIds: System.Collections.Generic.IEnumerable, rawDescs: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the RawDescription property for multiple CogoPoints with different RawDescription values.
            Remarks: If there are fewer raw description strings than points, only the first n points in the list will have their RawDescription property
            set, where n is the number of strings specified.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the RawDescription for.
            rawDescs: System.Collections.Generic.IEnumerable - A sequence of new RawDescription values.
        SetRawDescription(pointIds: System.Collections.Generic.IEnumerable, rawDesc: System.String) -> ObjectIdCollection
            Sets the RawDescription property for multiple CogoPoints with a single RawDescription value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the RawDescription for.
            rawDesc: System.String - The new RawDescription value.
        """
        pass
    
    
    def SetScaleXY(self):
        """
        SetScaleXY(pointId: ObjectId, scale: System.Double) -> ObjectId
            Sets the ScaleXY property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the ScaleXY property for.
            scale: System.Double - The new ScaleXY value.
        SetScaleXY(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets ScaleXY for multiple CogoPoints with different values.
            Remarks: If there are fewer doubles than points, only the first n points in the list will have their ScaleXY property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the ScaleXY property for.
            values: System.Collections.Generic.IEnumerable - A sequence of doubles to set the corresponding point's ScaleXY property to.
        SetScaleXY(pointIds: System.Collections.Generic.IEnumerable, scale: System.Double) -> ObjectIdCollection
            Sets the ScaleXY property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the ScaleXY property for.
            scale: System.Double - The new ScaleXY value.
        """
        pass
    
    
    def SetScaleZ(self):
        """
        SetScaleZ(pointId: ObjectId, scale: System.Double) -> ObjectId
            Sets ScaleZ for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the ScaleZ property for.
            scale: System.Double - The new ScaleZ value.
        SetScaleZ(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets ScaleZ for multiple CogoPoints with different values.
            Remarks: If there are fewer doubles than points, only the first n points in the list will have their ScaleZ property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the ScaleZ property for.
            values: System.Collections.Generic.IEnumerable - A sequence of doubles to set the corresponding point's ScaleZ property to.
        SetScaleZ(pointIds: System.Collections.Generic.IEnumerable, scale: System.Double) -> ObjectIdCollection
            Sets ScaleZ for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the ScaleZ property for.
            scale: System.Double - The new ScaleZ value.
        """
        pass
    
    
    def SetShowTooltips(self):
        """
        SetShowTooltips(pointId: ObjectId, showTooltips: System.Boolean) -> ObjectId
            Sets the ShowTooltips property for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the ShowTooltips property for.
            showTooltips: System.Boolean - The new ShowTooltips value.
        SetShowTooltips(pointIds: System.Collections.Generic.IEnumerable, showTooltips: System.Boolean) -> ObjectIdCollection
            Sets the ShowTooltips property for multiple CogoPoints with the same value.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the ShowTooltips property for.
            showTooltips: System.Boolean - The new ShowTooltips value.
        SetShowTooltips(pointIds: System.Collections.Generic.IEnumerable, values: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the ShowTooltips property for multiple CogoPoints with different values.
            Remarks: If there are fewer booleans than points, only the first n points in the list will have their ShowTooltips property
            set, where n is the number of items in the values list.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the ShowTooltips property for.
            values: System.Collections.Generic.IEnumerable - A sequence of booleans to set the corresponding point's ShowTooltips property to.
        """
        pass
    
    
    def SetStyleId(self):
        """
        SetStyleId(pointId: ObjectId, styleId: ObjectId) -> ObjectId
            Sets the StyleId for a single CogoPoint.
            pointId: ObjectId - The ObjectId of the point you want to set the StyleId property for.
            styleId: ObjectId - The ObjectId of the style you want to set StyleId to (object type PointStyle).
        SetStyleId(pointIds: System.Collections.Generic.IEnumerable, styleId: ObjectId) -> ObjectIdCollection
            Sets the StyleId for multiple CogoPoints with the same style.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the StyleId for.
            styleId: ObjectId - The ObjectId of the style you want to set StyleId to (object type PointStyle).
        SetStyleId(pointIds: System.Collections.Generic.IEnumerable, styleIds: System.Collections.Generic.IEnumerable) -> ObjectIdCollection
            Sets the StyleId for multiple CogoPoints with different styles.
            Remarks: If there are fewer StyleIds than points, only the first n points in the list will have their StyleId property
            set, where n is the number of StyleIds specified.
            pointIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the points you want to set the StyleId for.
            styleIds: System.Collections.Generic.IEnumerable - A sequence of ObjectIds of the PointStyles you want to set the corresponding point's StyleId to.
        """
        pass
    
    pass

class CogoPointEnumerator(object):
    """
    The CogoPointEnumerator class is used to enumerate a CogoPointCollection.
    """
    Current = None
    CurrentObject = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the CogoPointEnumerator
        """
        pass
    
    
    def MoveNext(self):
        """
        MoveNext() -> bool
            Advances the enumerator to the next element of the collection.
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
            Sets the enumerator to its initial position, which is before the first element in the collection.
        """
        pass
    
    pass

class ConnectorPositionType():
    """
    Specifies the connector position.
    """
    pass

class Corridor(Entity):
    """
    Representation of a roadway. A Roadway follows a 3D path defined by a baseline, and is made up of cross sections 
    (AppliedAssembly) and feature lines
    (FeatureLine) connecting common points in each 
    cross section.
    """
    Baselines = None
    CodeSetStyleId = None
    CodeSetStyleName = None
    CorridorSurfaces = None
    FeatureLineCodeInfos = None
    IsOutOfDate = None
    MaximumTriangleSideLength = None
    RebuildAutomatic = None
    RegionLockMode = None
    SlopePatterns = None
    StyleId = None
    StyleName = None
    def ExportFeatureLinesAsCogoPoints(self):
        """
        ExportFeatureLinesAsCogoPoints(pointGroupName: System.String, codes: Autodesk.Civil.DatabaseServices.CorridorPointCodeSelector) -> CorridorPointCodeSelector
            Exports the corridor feature lines indicated by the specified codes collection
            as COGO points.
            Remarks: Feature lines are created by the codes in the applied assemblies. The 
            CorridorPointCodeSelector class
            provides an interface to query and match the feature lines' points and the matching points will be used to
            create COGO Points in the specified point group.
            pointGroupName: System.String - A point group name for the exported CogoPoints.
            codes: Autodesk.Civil.DatabaseServices.CorridorPointCodeSelector - A collection of codes to select which corridor feature lines will be exported.
        ExportFeatureLinesAsCogoPoints(pointGroupName: System.String, codes: Autodesk.Civil.DatabaseServices.CorridorPointCodeSelector, baseLineRange: System.ValueType) -> CorridorPointCodeSelector
            Exports corridor feature lines as COGO points.
            Remarks: Feature lines are created by the codes in the applied assemblies. The 
            CorridorPointCodeSelector class
            provides an interface to query and match the feature lines' points and the matching points will be used to
            create COGO Points in the specified point group.
            This overload allows you to limit the points exported to those in the specified range. The range is indicated
            by Start and End stations, which should be part of the specified Baseline.
            pointGroupName: System.String - A point group name for the exported CogoPoints.
            codes: Autodesk.Civil.DatabaseServices.CorridorPointCodeSelector - A collection of codes that select which corridor feature lines will be exported.
            baseLineRange: System.ValueType - Defines a baseline range (by start station and end station) from which the corridor 
            feature lines are exported. 
        """
        pass
    
    
    def GetLinkCodes(self):
        """
        GetLinkCodes() -> string[]
            Gets all link codes of the corridor.
        """
        pass
    
    
    def GetPointCodes(self):
        """
        GetPointCodes() -> string[]
            Gets all point codes of the corridor.
        """
        pass
    
    
    def GetShapeCodes(self):
        """
        GetShapeCodes() -> string[]
            Gets all shape codes of the corridor.
        """
        pass
    
    
    def GetTargets(self):
        """
        GetTargets() -> SubassemblyTargetInfoCollection
            Gets the targets information.  The returned object can be modified and passed to SetTargets() to update a corridor's subassembly targets information.
        """
        pass
    
    
    def Rebuild(self):
        """
        Rebuild()
            Forces the corridor to rebuild.
            Remarks: Rebuilding the Corridor object can be an expensive operation; therefore, caution should be taken when
            invoking this method. It is recommended you perform all modifications to the Corridor object and invoke this
            method as the last operation, as opposed to calling the method after each operation.  Check the IsOutOfDate property to determine
            whether a corridor requires rebuilding.
        """
        pass
    
    
    def SetTargets(self):
        """
        SetTargets(updatedTargets: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfoCollection) -> SubassemblyTargetInfoCollection
            Sets the target information. The updatedTargets parameter is a SubassemblyTargetInfoCollection object that should be obtained from the GetTargets() method.
            Remarks: The updatedTargets object must be acquired through the GetTargets() method before making
            any modifications.
            updatedTargets: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfoCollection
        """
        pass
    
    pass

class CorridorBaselineType():
    """
    Indicates the type of baseline object.
    """
    pass

class CorridorCodeCollection(object):
    """
    A collection of strings containing corridor codes. A code is used to identify common calculated points in applied assemblies in a corridor. For example, a code can be used to identify the inside upper edge of a sidewalk in each assembly. Points that share a particular code can be connected to form feature lines (FeatureLine).
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(code: System.String)
            Adds a new code to the collection.
            code: System.String
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all code from the collection.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<string>
            Implements the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    pass

class CorridorCollection(object):
    """
    Represents the collection of Corridor objects in the drawing.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(corridorName: System.String) -> ObjectId
            Creates a new, empty Corridor.
            Remarks: This method creates a new, empty Corridor with the specified name. The Corridor object will not contain a 
            Baseline or BaselineRegion. The method does not allow duplicate names; however, Corridor names are
            case-sensitive, so it is possible to add a Corridor "corridor - 1" when a "Corridor - 1" already exists. 
            Adding Corridor objects with names that differ only by case is not recommended.
            corridorName: System.String - Name of the corridor to be created.
        Add(corridorName: System.String, baselineName: System.String, alignmentId: ObjectId, profileId: ObjectId) -> ObjectId
            TODO: NEEDS SAMPLE
            Creates a new Corridor corridor object.
            Remarks: This method creates a new Corridor object. The Corridor has the specified name, and a new Baseline is
            created referencing the specified alignmentId and profileId. The new
            Baseline has the specified baselineName.
            corridorName: System.String - Name of the Corridor to be created.Name of the Corridor to be created.
            baselineName: System.String - Name of the Baseline to be created.Name of the Baseline to be created.
            alignmentId: ObjectId - ObjectId of the Alignment used to create the Baseline.ObjectId of the Alignment used to create the Baseline.
            profileId: ObjectId - ObjectId of the Profile used to create the Baseline.ObjectId of the Profile used to create the Baseline.
        Add(corridorName: System.String, baselineName: System.String, alignmentId: ObjectId, profileId: ObjectId, baselineRegionName: System.String, assemblyId: ObjectId) -> ObjectId
            Creates a new Corridor object.
            Remarks: This method creates a new Corridor object. It allows you to specify the Corridor object name, the new Baseline
            name, the Alignment and Profile ids used to create the Baseline, a region name for a
            new BaselineRegion to be created, and the Assembly id to be used within the region.
            The specified Profile object must
            belong to the specified Alignment.
            corridorName: System.String - Name of the Corridor to be created.
            baselineName: System.String - Name of the Baseline to be created.
            alignmentId: ObjectId - ObjectId of the Alignment used to create the Baseline.
            profileId: ObjectId - ObjectId of the Profile used to create the Baseline.
            baselineRegionName: System.String - Name of the BaselineRegion to be created.
            assemblyId: ObjectId - ObjectId of the Assembly used to create the region.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<ObjectId>
            Implements the method declared in the IEnumerable<T> interface.
            Remarks: This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface.
            Remarks: This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    pass

class CorridorFeatureLine(object):
    """
    A corridor feature line is a connected series of points along a corridor created by joining those points from each assembly that share a particular code. Feature lines are used to build the 3D model of a corridor.
    """
    CodeName = None
    CorridorId = None
    FeatureLinePoints = None
    StyleId = None
    StyleName = None
    def ExportAsAlignment(self):
        """
        ExportAsAlignment(alignmentName: System.String, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, alignmentType: Autodesk.Civil.DatabaseServices.AlignmentType) -> AlignmentType
            Exports a corridor feature line as an alignment.
            alignmentName: System.String - The name of the created Alignment.
            If the name already exists, the method generates another unique name by adding a number as a suffix.
            siteId: ObjectId - The ObjectId of the site on which the Alignment is created.
            layerId: ObjectId - The ObjectId of the layer on which the Alignment is created.
            styleId: ObjectId - The ObjectId of the style applied to the created Alignment.
            labelSetId: ObjectId - The ObjectId of the labelSet applied to the created Alignment.
            alignmentType: Autodesk.Civil.DatabaseServices.AlignmentType - The kind of alignment to create.
        """
        pass
    
    
    def ExportAsGradingFeatureLine(self):
        """
        ExportAsGradingFeatureLine(siteId: ObjectId, isDynamic: System.Boolean) -> ObjectId
            Exports the feature line as a grading feature line.
            siteId: ObjectId - The ObjectId of the site for the Grading FeatureLine.
            isDynamic: System.Boolean
        ExportAsGradingFeatureLine(siteId: ObjectId, isDynamic: System.Boolean, featureLineName: System.String, layerId: ObjectId, styleId: ObjectId, smoothOption: Autodesk.Civil.DatabaseServices.GradingSmoothOption) -> GradingSmoothOption
            Exports the feature line as a grading feature line.
            siteId: ObjectId - The ObjectId of the site for the Grading FeatureLine.
            isDynamic: System.Boolean
            featureLineName: System.String - A name for the Grading FeatureLine.  An empty name is allowed.
            layerId: ObjectId - The ObjectId of the layer for the grading FeatureLine.
            styleId: ObjectId - The ObjectId of the style for the Grading FeatureLine.
            smoothOption: Autodesk.Civil.DatabaseServices.GradingSmoothOption - The smoothing options for creating the grading FeatureLine.
        """
        pass
    
    
    def ExportAsPolyline3d(self):
        """
        ExportAsPolyline3d() -> Autodesk.Civil.DatabaseServices.CorridorFeatureLine.
            Exports the feature line as a polyline.
        """
        pass
    
    
    def ExportAsPolyline3dCollection(self):
        """
        ExportAsPolyline3dCollection() -> ObjectIdCollection
            Exports the feature line as a collection of polyline.
        """
        pass
    
    
    def ExportAsProfile(self):
        """
        ExportAsProfile(profileName: System.String, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId
            Exports a corridor feature line as a profile.
            profileName: System.String - The name for the new profile.
            alignmentId: ObjectId - The ObjectId of the Alignment to place the new profile on.
            layerId: ObjectId - The ObjectId of the Layer for the new profile.
            styleId: ObjectId - The ObjectId of the Style to apply to the new profile.
            labelSetId: ObjectId - The ObjectId of the LabelSet to apply to the new profile.
        """
        pass
    
    pass

class CorridorLinkDisplay():
    """
    
    """
    pass

class CorridorLinkDrawOverride():
    """
    
    """
    pass

class CorridorPointCodeOption(object):
    """
    Identifies feature lines by point code name, and allows you to specify whether the feature line will be selected during 
    export.
    """
    CodeName = None
    Selected = None
    pass

class CorridorPointCodeSelector(object):
    """
    This class exposes functionality for selecting and un-selecting point types.
    It is used to select points for export.
    """
    Count = None
    Item = None
    def GetAllCodes(self):
        """
        GetAllCodes() -> string[]
            Gets all feature line codes.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CorridorPointCodeOption
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator that can
            be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator that can be used 
            to enumerate this collection.
        """
        pass
    
    
    def SelectAll(self):
        """
        SelectAll()
            Selects all supported corridor feature line points.
        """
        pass
    
    
    def UnSelectAll(self):
        """
        UnSelectAll()
            De-selects all supported corridor feature line points.
        """
        pass
    
    pass

class CorridorSection(Entity):
    """
    A section of a Corridor.
    """
    StyleId = None
    StyleName = None
    def GetCorridor(self):
        """
        GetCorridor() -> ObjectId
            Gets the ObjectId of the parent Corridor.
        """
        pass
    
    
    def GetLinkCodes(self):
        """
        GetLinkCodes() -> string[]
            Gets the link codes from current CorridorSection's subassemblies.
        """
        pass
    
    
    def GetPointCodes(self):
        """
        GetPointCodes() -> string[]
            Gets the point codes from current CorridorSection's subassemblies.
        """
        pass
    
    
    def GetShapeCodes(self):
        """
        GetShapeCodes() -> string[]
            Gets the shape codes from current CorridorSection's subassemblies.
        """
        pass
    
    
    def SetCorridor(self):
        """
        SetCorridor(corridorId: ObjectId)
            Sets the source Corridor for the section.
            corridorId: ObjectId
        SetCorridor(corridorName: System.String)
            Sets the source Corridor for the section.
            corridorName: System.String
        """
        pass
    
    pass

class CorridorSlopePattern(object):
    """
    Slope patterns are slope indicator lines. They have one or more repeating lines that are aligned with the flow direction. The lines can be the length of the slope or less. They can have a predefined symbol or an AutoCAD block inserted at one end.
    """
    BaselineId = None
    CorridorId = None
    EndStation = None
    FeatureLine1 = None
    FeatureLine2 = None
    StartStation = None
    StyleId = None
    StyleName = None
    pass

class CorridorSlopePatternCollection(object):
    """
    A collection of slope pattern (CorridorSlopePattern) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(featureLine1: Autodesk.Civil.DatabaseServices.CorridorFeatureLine, featureLine2: Autodesk.Civil.DatabaseServices.CorridorFeatureLine, slopePatternStyleId: ObjectId) -> CorridorSlopePattern
            Creates a CorridorSlopePattern with two feature lines and the style.
            featureLine1: Autodesk.Civil.DatabaseServices.CorridorFeatureLine
            featureLine2: Autodesk.Civil.DatabaseServices.CorridorFeatureLine
            slopePatternStyleId: ObjectId
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CorridorSlopePattern
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator that can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator that can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(slopePattern: Autodesk.Civil.DatabaseServices.CorridorSlopePattern) -> CorridorSlopePattern
            Removes the given CorridorSlopePattern object.
            slopePattern: Autodesk.Civil.DatabaseServices.CorridorSlopePattern
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32) -> bool
            Removes CorridorSlopePattern object with the given index.
            index: System.Int32
        """
        pass
    
    pass

class CorridorSurface(object):
    """
    Represents a layer of a corridor, and is computed from a set of feature lines, calculated points, and calculated links.
    """
    Boundaries = None
    CorridorId = None
    Description = None
    IsBuild = None
    IsDraw = None
    Masks = None
    Name = None
    OverhangCorrection = None
    RenderMaterialId = None
    SectionStyleId = None
    SurfaceId = None
    SurfaceStyleId = None
    def AddFeatureLineCode(self):
        """
        AddFeatureLineCode(codeName: System.String)
            Adds a feature line code to corridor surface.
            codeName: System.String
        """
        pass
    
    
    def AddLinkCode(self):
        """
        AddLinkCode(codeName: System.String, addAsBreakLine: System.Boolean)
            Adds a link code to corridor surface.
            codeName: System.String
            addAsBreakLine: System.Boolean
        """
        pass
    
    
    def FeatureLineCodeIsBreak(self):
        """
        FeatureLineCodeIsBreak(name: System.String) -> bool
            Gets the IsBreak value of the link code.
            name: System.String
        """
        pass
    
    
    def FeatureLineCodes(self):
        """
        FeatureLineCodes() -> string[]
            Gets the feature line codes used to construct the surface.
        """
        pass
    
    
    def FindElevationAtXY(self):
        """
        FindElevationAtXY(x: System.Double, y: System.Double) -> double
            Finds the elevation of the surface at the specified XY location.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def GetSampleElevations(self):
        """
        GetSampleElevations(startX: System.Double, startY: System.Double, endX: System.Double, endY: System.Double) -> Point3dCollection
            Gets the collection of sample elevations.
            startX: System.Double
            startY: System.Double
            endX: System.Double
            endY: System.Double
        """
        pass
    
    
    def IsLinkCodeAsBreakLine(self):
        """
        IsLinkCodeAsBreakLine(codeName: System.String) -> bool
            Gets the link code as break line or not.
            codeName: System.String
        """
        pass
    
    
    def LinkCodes(self):
        """
        LinkCodes() -> string[]
            Gets the link codes used to construct the surface.
        """
        pass
    
    
    def PointCodes(self):
        """
        PointCodes() -> string[]
            Gets the point codes used to construct the surface.
        """
        pass
    
    
    def RemoveFeatureLineCode(self):
        """
        RemoveFeatureLineCode(codeName: System.String) -> bool
            Removes a feature line code from corridor surface.
            codeName: System.String
        """
        pass
    
    
    def RemoveLinkCode(self):
        """
        RemoveLinkCode(codeName: System.String) -> bool
            Removes a link code from corridor surface.
            codeName: System.String
        """
        pass
    
    
    def SetLinkCodeAsBreakLine(self):
        """
        SetLinkCodeAsBreakLine(codeName: System.String, asBreakLine: System.Boolean)
            Sets the link code as break line or not.
            codeName: System.String
            asBreakLine: System.Boolean
        """
        pass
    
    pass

class CorridorSurfaceBaseMask(CorridorSurfaceBoundary):
    """
    Base class for CorridorSurfaceMask and CorridorSurfaceBoundary.
    """
    CorridorId = None
    Description = None
    FeatureLineComponents = None
    IsDefinedFromPolygon = None
    Name = None
    def PolygonPoints(self):
        """
        PolygonPoints() -> Point3d[]
            Gets the points of the polygon that make up the edge of the boundary or mask.
        """
        pass
    
    pass

class CorridorSurfaceBoundary(CorridorSurfaceBaseMask):
    """
    A corridor surface boundary represents an outside or inside edge of a corridor surface (CorridorSurface). It is defined by a polygon or a series of feature line components (FeatureLineComponent).
    """
    BoundaryType = None
    IsCorridorExtents = None

    pass

class CorridorSurfaceBoundaryCollection(object):
    """
    Collection of corridor surface boundary (CorridorSurfaceBoundary) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(boundaryName: System.String) -> CorridorSurfaceBoundary
            Adds an empty outside boundary with the given boundary name.
            Remarks: After the boundary is created, its definitions can be customized by modifying FeatureLineComponents.
            boundaryName: System.String - Name of the newly created boundary.
        Add(boundaryName: System.String, polylineId: ObjectId) -> CorridorSurfaceBoundary
            Adds an outside boundary with the given boundary name and polyline.
            Remarks: Only Autodesk.AutoCAD.DatabaseServices.Polyline, Autodesk.AutoCAD.DatabaseServices.Polyline2d and Autodesk.AutoCAD.DatabaseServices.Polyline3d are supported.
            boundaryName: System.String - Name of the newly created boundary.
            polylineId: ObjectId - ObjectId of the polyline used to create boundary.
        Add(boundaryName: System.String, points: Point3dCollection) -> CorridorSurfaceBoundary
            Adds an outside boundary with the given boundary name and polygon points.
            boundaryName: System.String - Name of the newly created boundary.
            points: Point3dCollection - Points used to create boundary.
        Add(boundaryName: System.String, featureLineCode: System.String) -> CorridorSurfaceBoundary
            Adds an outside boundary with the given boundary name and feature line code.
            boundaryName: System.String - Name of the newly created boundary.
            featureLineCode: System.String - Feature line code used to create boundary.
        """
        pass
    
    
    def AddCorridorExtentsBoundary(self):
        """
        AddCorridorExtentsBoundary(boundaryName: System.String) -> CorridorSurfaceBoundary
            Adds corridor extents as outer boundary with the given boundary name.
            Remarks: The type of newly added boundary is always outside boundary and cannot be changed.
            Use Autodesk.Civil.DatabaseServices.CorridorSurfaceBoundary.IsCorridorExtents to check whether a boundary is defined with corridor extents.
            boundaryName: System.String - Name of the newly created boundary.
        """
        pass
    
    
    def BoundaryNames(self):
        """
        BoundaryNames() -> string[]
            Gets an array of boundary names.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CorridorSurfaceBoundary
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(boundaryName: System.String) -> bool
            Removes a CorridorSurfaceBoundary object with the given name.
            boundaryName: System.String - Name of the removed CorridorSurfaceBoundary object.
        Remove(boundary: Autodesk.Civil.DatabaseServices.CorridorSurfaceBoundary) -> CorridorSurfaceBoundary
            Removes the given CorridorSurfaceBoundary object.
            boundary: Autodesk.Civil.DatabaseServices.CorridorSurfaceBoundary - The removed CorridorSurfaceBoundary object.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a CorridorSurfaceBoundary object by index.
            index: System.Int32 - Index of the removed CorridorSurfaceBoundary object.
        """
        pass
    
    pass

class CorridorSurfaceBoundaryType():
    """
    Defines CorridorSurfaceBoundary types.
    """
    pass

class CorridorSurfaceCollection(object):
    """
    A collection of corridor surface (CorridorSurface) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(corridorSurfaceName: System.String) -> CorridorSurface
            Adds an empty corridor surface with name and default style.
            corridorSurfaceName: System.String - Name used to create the corridor surface.
        Add(corridorSurfaceName: System.String, styleId: ObjectId) -> CorridorSurface
            Adds an empty corridor surface with name and style.
            corridorSurfaceName: System.String - Name used to create the corridor surface.
            styleId: ObjectId - Name used to create the corridor surface.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CorridorSurface
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(corridorSurfaceName: System.String) -> bool
            Removes a CorridorSurface with the given name.
            corridorSurfaceName: System.String - Name of the CorridorSurface.
        Remove(corridorSurface: Autodesk.Civil.DatabaseServices.CorridorSurface) -> CorridorSurface
            Removes the given CorridorSurface.
            corridorSurface: Autodesk.Civil.DatabaseServices.CorridorSurface - The CorridorSurface object to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a CorridorSurface by index.
            index: System.Int32 - Index of the CorridorSurface to be removed.
        """
        pass
    
    
    def SurfaceNames(self):
        """
        SurfaceNames() -> string[]
            Gets an array of surface names from the collection.
        """
        pass
    
    pass

class CorridorSurfaceMask(CorridorSurfaceBaseMask):
    """
    The corridor surface mask is a region defined by a polygon or a series of feature line components (FeatureLineComponent) describing the part of a corridor surface (CorridorSurface) that is visible.
    """
    RenderMaterialId = None

    pass

class CorridorSurfaceMaskCollection(object):
    """
    Collection of corridor surface mask (CorridorSurfaceMask) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(maskName: System.String) -> CorridorSurfaceMask
            Adds an empty mask with the given mask name.
            Remarks: After the mask is created, its definitions can be customized by modifying FeatureLineComponents.
            maskName: System.String - Name of the newly created mask.
        Add(maskName: System.String, polylineId: ObjectId) -> CorridorSurfaceMask
            Adds a mask with the given mask name and polyline.
            Remarks: Only Autodesk.AutoCAD.DatabaseServices.Polyline, Autodesk.AutoCAD.DatabaseServices.Polyline2d and Autodesk.AutoCAD.DatabaseServices.Polyline3d are supported.
            maskName: System.String - Name of the newly created mask.
            polylineId: ObjectId - ObjectId of the polyline used to create mask.
        Add(maskName: System.String, points: Point3dCollection) -> CorridorSurfaceMask
            Adds a mask with the given mask name and polygon points.
            maskName: System.String - Name of the newly created mask.
            points: Point3dCollection - Points used to create mask.
        Add(maskName: System.String, featureLineCode: System.String) -> CorridorSurfaceMask
            Adds a mask with the given mask name and feature line code.
            maskName: System.String - Name of the newly created mask.
            featureLineCode: System.String - Feature line code used to create mask.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> CorridorSurfaceMask
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def MaskNames(self):
        """
        MaskNames() -> string[]
            Gets an array of mask names.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(maskName: System.String) -> bool
            Removes a CorridorSurfaceMask object with the given name.
            maskName: System.String
        Remove(mask: Autodesk.Civil.DatabaseServices.CorridorSurfaceMask) -> CorridorSurfaceMask
            Removes the given CorridorSurfaceMask object.
            mask: Autodesk.Civil.DatabaseServices.CorridorSurfaceMask
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a CorridorSurfaceMask object by index.
            index: System.Int32 - Index of the removed CorridorSurfaceMask object.
        """
        pass
    
    pass

class CurbReturnJoiningType():
    """
    Specifies the method that is used to define the curb return profile.
    """
    pass

class CurveCurveReverseCurveTransitionDescription(TransitionDescriptionBase):
    """
    This class represents a transition that contains Curve/Curve/Reverse Curve/Curve components.
    """
    FirstCurveRadius = None
    ReverseCurveRadius = None
    SecondCurveRadius = None
    pass

class CurveLineCurveTransitionDescription(TransitionDescriptionBase):
    """
    This class represents a transition that contains Curve/Line/Curve components.
    """
    EntryCurveRadius = None
    ExitCurveRadius = None
    pass

class CurveParamType():
    """
    Defines the free curve type.
    """
    pass

class CurveReverseCurveTransitionDescription(TransitionDescriptionBase):
    """
    This class represents a transition that contains Curve/Reverse Curve/Curve components.
    """
    EntryCurveRadius = None
    ReverseCurveRadius = None
    pass

class CurveType():
    """
    Defines the free curve type.
    """
    pass

class CustomPointGroupQuery(PointGroupQuery):
    """
    A custom PointGroup query.
    """
    QueryString = None
    pass

class DBObject(Folder):
    """
    The base class for database entities.
    """
    Application = None
    Description = None
    Document = None
    Name = None
    pass

class DatumRoundingType():
    """
    Specifies where to round the vertical split location.
    """
    pass

class DesignSpeed(object):
    """
    The Alignment DesignSpeed class.  Specifies a single design speed used for criteria-based Alignment design.
    """
    Comment = None
    SpeedNumber = None
    Station = None
    Value = None
    pass

class DesignSpeedCollection(object):
    """
    A collection of DesignSpeed objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(station: System.Double, speed: System.Double) -> DesignSpeed
            Adds a DesignSpeed to the collection for the given Station value.
            station: System.Double - Station value in the design speed collection.
            speed: System.Double - Speed value in the design speed collection.
        """
        pass
    
    
    def GetDesignSpeed(self):
        """
        GetDesignSpeed(rawStation: System.Double) -> DesignSpeed
            Gets the DesignSpeed object in the collection by raw Station value.
            rawStation: System.Double - Raw station value.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> DesignSpeed
            Implements the method declared in the IEnumerable<T> interface. 
            This method return an enumertor which can be used to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. 
            This method return an enumertor which can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(rawStation: System.Double)
            Removes a DesignSpeed from the collection by raw Station value.
            rawStation: System.Double - Raw station value.
        Remove(Index: System.Int32)
            Removes a DesignSpeed from the collection at the given index.
            Index: System.Int32 - Index of the DesignSpeed object to remove.
        """
        pass
    
    pass

class DomainType():
    """
    Specifies a Part domain type.
    """
    pass

class ElevationRangeType():
    """
    Defines the ways to specify the vertical range of the profile view.
    """
    pass

class Entity(Catchment):
    """
    The base class for entities, such as Feature, Table, Grading, Site, etc.
    """
    Application = None
    Description = None
    DisplayName = None
    Document = None
    FingerPrint = None
    FolderId = None
    IsReferenceObject = None
    IsReferenceStale = None
    IsReferenceSubObject = None
    IsReferenceValid = None
    Name = None
    ShowToolTip = None
    StyleId = None
    StyleName = None
    def ComputeFingerPrint(self):
        """
        ComputeFingerPrint() -> ulong
            Compute FingerPrint of the Entity.
        """
        pass
    
    pass

class EntityAttachType():
    """
    Defines the type to attach the entity.
    """
    pass

class EntityVerticalConstraintType():
    """
    Specifies the construction constraint type of ProfileEntity, for example, use PassThroughPt1AndPt2 if you create this entity by two fixed points. 
    Note that some items are only valid for ProfileLine while others are only valid for three parabolic entities.
    """
    pass

class Feature(Entity):
    """
    Base class for Alignment, FeatureLine, ParcelSegment, and Profile.
    """
    IsEditable = None
    def IsEditableFeature(self):
        """
        IsEditableFeature(featureId: ObjectId) -> bool
            Check whether the Feature-derived entity (Alignment,Profile,etc) is editable.
            featureId: ObjectId - ObjectId for the Feature-derived entity you want to check.
        """
        pass
    
    pass

class FeatureLabel(Entity):
    """
    A base class for feature label classes, such as AlignmentCurveLabel.
    """


    pass

class FeatureLine(Entity):
    """
    A feature line is a connected series of points along a corridor created by joining those points from each assembly that share a particular code. Feature lines are used to build the 3D model of a corridor.
    """
    ElevationPointsCount = None
    Length2D = None
    Length3D = None
    MaxElevation = None
    MaxGrade = None
    MinElevation = None
    MinGrade = None
    PIPointsCount = None
    PointsCount = None
    SiteId = None
    StyleId = None
    StyleName = None
    def AssignElevationsFromSurface(self):
        """
        AssignElevationsFromSurface(surfaceId: ObjectId, bIncIntermediate: System.Boolean)
            Assigns elevations from surface.
            surfaceId: ObjectId - The ObjectId of specified surface.
            bIncIntermediate: System.Boolean - Inserts intermediate grade break points or not.
        """
        pass
    
    
    def Create(self):
        """
        Create(featurelineName: System.String, idCreatedFrom: ObjectId) -> ObjectId
            Creates a FeatureLine from the specified Line, Arc, Polyline, Polyline2d or Polyline3d.
            featurelineName: System.String - Name of the created FeatureLine, and this name can be null or empty string for creating an unnamed feature line.
            idCreatedFrom: ObjectId - The ObjectId of specified Line, Arc, Polyline, Polyline2d or Polyline3d created from.
        Create(featurelineName: System.String, idCreatedFrom: ObjectId, siteId: ObjectId) -> ObjectId
            Creates a FeatureLine from the specified Line, Arc, Polyline, Polyline2d or Polyline3d.
            featurelineName: System.String - Name of the created FeatureLine, and this name can be null or empty string for creating an unnamed feature line.
            idCreatedFrom: ObjectId - The ObjectId of specified Line, Arc, Polyline, Polyline2d or Polyline3d created from.
            siteId: ObjectId - The ObjectId of Site.
        """
        pass
    
    
    def DeleteElevationPoint(self):
        """
        DeleteElevationPoint(pt: Point3d)
            Deletes an elevation point along the FeatureLine.
            pt: Point3d - The elevation point to delete.
        """
        pass
    
    
    def DeletePIPoint(self):
        """
        DeletePIPoint(pt: Point3d)
            Deletes a PI point along the FeatureLine.
            pt: Point3d - The PI point to delete.
        """
        pass
    
    
    def Get3dDistanceAtPoint(self):
        """
        Get3dDistanceAtPoint(pt: Point3d) -> double
            Gets the 3d distance at given point along the FeatureLine.
            pt: Point3d - The specified point on the feature line.
        """
        pass
    
    
    def GetBulge(self):
        """
        GetBulge(index: System.Int32) -> double
            Gets the bulge at the index of feature line's segment.
            index: System.Int32 - The index of feature line's segment.
        """
        pass
    
    
    def GetDeflectionAngleAtPoint(self):
        """
        GetDeflectionAngleAtPoint(pt: Point3d) -> double
            Gets the deflection angle in radians at given point along the FeatureLine.
            pt: Point3d - The specified point on the feature line.
        """
        pass
    
    
    def GetGradeInAtPoint(self):
        """
        GetGradeInAtPoint(pt: Point3d) -> double
            Gets the in grade at given point along the FeatureLine.
            pt: Point3d - The specified point on the feature line.
        """
        pass
    
    
    def GetGradeOutAtPoint(self):
        """
        GetGradeOutAtPoint(pt: Point3d) -> double
            Gets the out grade at given point along the FeatureLine.
            pt: Point3d - The specified point on the feature line.
        """
        pass
    
    
    def GetPoints(self):
        """
        GetPoints(type: Autodesk.Civil.FeatureLinePointType) -> FeatureLinePointType
            Gets the feature line points by type.
            type: Autodesk.Civil.FeatureLinePointType
        """
        pass
    
    
    def InsertElevationPoint(self):
        """
        InsertElevationPoint(pt: Point3d)
            Inserts an elevation point along the FeatureLine.
            pt: Point3d - The specified point on the feature line.
        """
        pass
    
    
    def InsertPIPoint(self):
        """
        InsertPIPoint(pt: Point3d)
            Inserts a PI point along the FeatureLine.
            pt: Point3d - The specified point on the feature line.
        """
        pass
    
    
    def MoveToNoneSite(self):
        """
        MoveToNoneSite(featureLineId: ObjectId)
            Move FeatureLine to none Site.
            featureLineId: ObjectId - The ObjectId of FeatureLine to be moved.
        """
        pass
    
    
    def MoveToSite(self):
        """
        MoveToSite(featureLineId: ObjectId, destinationSiteId: ObjectId)
            Move FeatureLine to another Site.
            featureLineId: ObjectId - The ObjectId of FeatureLine to be moved.
            destinationSiteId: ObjectId - The ObjectId of destination Site.
        """
        pass
    
    
    def SetBulge(self):
        """
        SetBulge(index: System.Int32, bugle: System.Double)
            Sets the bulge at the index of feature line's segment.
            index: System.Int32 - The index of feature line's segment.
            bugle: System.Double - The bugle of feature line's segment to be set.
        """
        pass
    
    
    def SetPointElevation(self):
        """
        SetPointElevation(index: System.Int32, elevation: System.Double)
            Set an elevation to existing Feature Point.
            index: System.Int32 - The index of feature line's point.
            elevation: System.Double - The new elevation to be set.
        """
        pass
    
    pass

class FeatureLineCodeInfo(object):
    """
    Information about the code used to construct a feature line.
    """
    CodeName = None
    CorridorId = None
    IsConnect = None
    IsConnected = None
    IsDraw = None
    PayItems = None
    pass

class FeatureLineCodeInfoCollection(object):
    """
    A collection of feature line code information (FeatureLineCodeInfo) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def CodeNames(self):
        """
        CodeNames() -> string[]
            Gets a list of code names in the collection.
        """
        pass
    
    
    def GetConnectedFeatureLineCodeInfos(self):
        """
        GetConnectedFeatureLineCodeInfos() -> FeatureLineCodeInfo
            Gets an array of the connected FeatureLineCodeInfo.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> FeatureLineCodeInfo
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    pass

class FeatureLineCollection(object):
    """
    Collection of feature lines that share a particular code. Multiple points in a single assembly may contain the same code, so feature lines can branch along a corridor. This collection represents a single interconnected series of feature lines branches.
    """
    ConnectDirection = None
    CorridorId = None
    Count = None
    FeatureLineCodeInfo = None
    IsConnectExtraPoints = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> CorridorFeatureLine
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator that can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator that can be used to enumerate this collection.
        """
        pass
    
    pass

class FeatureLineCollectionMap(object):
    """
    A collection of multiple feature line collections (FeatureLineCollection) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def CodeNames(self):
        """
        CodeNames() -> string[]
            Gets an array of code names used in all feature lines in the collection.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> FeatureLineCollection
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    pass

class FeatureLineComponent(object):
    """
    A portion of an entire feature line, delimited by a starting and ending station.
    """
    BaselineAlignmentId = None
    CorridorId = None
    EndStation = None
    FeatureLine = None
    IsReversed = None
    StartStation = None
    UseEndStation = None
    UseStartStation = None
    pass

class FeatureLineComponentCollection(object):
    """
    A collection of feature line component (FeatureLineComponent) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def Add(self):
        """
        Add(featureLine: Autodesk.Civil.DatabaseServices.CorridorFeatureLine) -> FeatureLineComponent
            Adds a new FeatureLineComponent from a CorridorFeatureLine.
            featureLine: Autodesk.Civil.DatabaseServices.CorridorFeatureLine
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> FeatureLineComponent
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(featureLineComponent: Autodesk.Civil.DatabaseServices.FeatureLineComponent) -> FeatureLineComponent
            Removes the specified FeatureLineComponent object.
            featureLineComponent: Autodesk.Civil.DatabaseServices.FeatureLineComponent
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes an item at the given index.
            index: System.Int32
        """
        pass
    
    
    def Swap(self):
        """
        Swap(component1: Autodesk.Civil.DatabaseServices.FeatureLineComponent, component2: Autodesk.Civil.DatabaseServices.FeatureLineComponent) -> FeatureLineComponent
            Change the boundary draw order by Swapping the position of two FeatureLineComponent.
            component1: Autodesk.Civil.DatabaseServices.FeatureLineComponent - The FeatureLineComponent to be swapped.
            component2: Autodesk.Civil.DatabaseServices.FeatureLineComponent - The FeatureLineComponent to be swapped.
        """
        pass
    
    
    def SwapAt(self):
        """
        SwapAt(index1: System.Int32, index2: System.Int32)
            Change the boundary draw order by Swapping the position of FeatureLineComponent by index.
            index1: System.Int32 - The index of first FeatureLineComponent to be swapped.
            index2: System.Int32 - The index of second FeatureLineComponent to be swapped.
        """
        pass
    
    
    def Validate(self):
        """
        Validate() -> bool
            Verifies whether the feature line components construct a well formed polygon (without crossing on itself).
        """
        pass
    
    pass

class FeatureLinePoint(object):
    """
    A point in a feature line (FeatureLine object). A feature line is created by connecting common points within applied assemblies (AppliedAssembly objects) along a corridor. Points in each applied assembly are identified by codes. For example, a feature line can represent the inside upper edge of a sidewalk along a stretch of road.
    """
    CorridorId = None
    IsBreak = None
    Offset = None
    Station = None
    XYZ = None
    pass

class FeatureLinePointCollection(object):
    """
    A collection of feature line point (FeatureLinePoint) objects.
    """
    CorridorId = None
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> FeatureLinePoint
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    pass

class FlowDirectionMethodType():
    """
    Specifies the method that is used to determine the flow for a pipe.
    """
    pass

class FlowDirectionType():
    """
    Specifies the current flow direction of a pipe.
    """
    pass

class FlowPath(object):
    """
    This class encapsulates a catchment flow path.  
    A flow path defines the path that water travels in the catchment between the hydraulically most distant point in the catchment and the discharge point.
    A FlowPath is made up of one or more FlowSegment objects.
    """
    FlowSegmentCount = None
    def GetFlowSegmentAt(self):
        """
        GetFlowSegmentAt(index: System.Int32) -> FlowSegment
            Gets a FlowSegment by index from the FlowPath.
            index: System.Int32
        """
        pass
    
    pass

class FlowSegment(object):
    """
    This class encapsulates a single segment of a catchment flow path (represented by the FlowPath class).
    """
    pass

class FlowSegmentLabel(Entity):
    """
    This class represents a FlowSegment label.
    """
    FlowSegmentIndex = None
    Ratio = None
    def Create(self):
        """
        Create(flowSegment: Autodesk.Civil.DatabaseServices.FlowSegment) -> FlowSegment
            Creates a new instance of a FlowSegmentLabel on the specified FlowSegment with the default label style.
            flowSegment: Autodesk.Civil.DatabaseServices.FlowSegment - The FlowSegment Object to create the label on.
        Create(flowSegment: Autodesk.Civil.DatabaseServices.FlowSegment, labelStyleId: ObjectId) -> FlowSegment
            Creates a new instance of a FlowSegmentLabel on the specified FlowSegment with the specified label style.
            flowSegment: Autodesk.Civil.DatabaseServices.FlowSegment - The FlowSegment Object to create the label on.
            labelStyleId: ObjectId - The ObjectId of the FlowSegmentLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(catchmentId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the FlowSegmentLabels on the specified Catchment.
            catchmentId: ObjectId - The ObjectId of the Catchment to get the FlowSegmentLabels for.
        """
        pass
    
    pass

class Folder(DBObject):
    """
    This class encapsulates folder in the current drawing.
    """

    def AddEntity(self):
        """
        AddEntity(entityId: ObjectId)
            Adds the Entity specified by entityId to the folder
            entityId: ObjectId
        """
        pass
    
    
    def CreateFolder(self):
        """
        CreateFolder(name: System.String) -> ObjectId
            Creates a child folder with the input folder name, return the created child folder ObjectId
            name: System.String
        """
        pass
    
    
    def DeleteFolder(self):
        """
        DeleteFolder()
            Deletes the folder
        """
        pass
    
    
    def GetFolder(self):
        """
        GetFolder(nameOrPath: System.String) -> ObjectId
            Gets child folder ObjectId by name or path
            Remarks: Returns ObjectId::Null if the folder is not found
            nameOrPath: System.String - 
            Name of the direct child folder is supported; path using "\" as separator is also supported, for example: Folder\Folder1\Folder11
        """
        pass
    
    
    def GetParent(self):
        """
        GetParent() -> ObjectId
            Gets the parent folder ObjectId
            Remarks: Returns ObjectId::Null if it is root folder
        """
        pass
    
    
    def GetPath(self):
        """
        GetPath() -> string
            Gets a String containing the path relative to the root folder
            Remarks: Returns a path String using "\" as delimiter, for example: "Folder\Folder1"
            Returns an empty String if it is a root folder
        """
        pass
    
    
    def GetSubFolders(self):
        """
        GetSubFolders() -> ObjectIdCollection
            Gets the ObjectIdCollection of Sub Folders
        """
        pass
    
    
    def RenameFolder(self):
        """
        RenameFolder(newName: System.String)
            Renames the folder
            newName: System.String
        """
        pass
    
    pass

class FolderUtil(object):
    """
    
    """
    def GetAlignmentRootFolder(self):
        """
        GetAlignmentRootFolder(aType: Autodesk.Civil.DatabaseServices.AlignmentType, database: Database) -> AlignmentType
            Gets root folder ObjectId for specified alignment type
            aType: Autodesk.Civil.DatabaseServices.AlignmentType
            database: Database
        """
        pass
    
    
    def GetNonAlignmentRootFolder(self):
        """
        GetNonAlignmentRootFolder(rxClass: RXClass, database: Database) -> ObjectId
            Gets root folder ObjectId for non-alignment type
            Supported list: surface, pipe network, pressure network, corridor, view frame group, intersection
            rxClass: RXClass
            database: Database
        """
        pass
    
    pass

class GeneralSegmentLabel(Entity):
    """
    This class represents a general label.
    """
    CurveLabelStyleId = None
    LineLabelStyleId = None
    Ratio = None
    StyleName = None
    def Create(self):
        """
        Create(featureId: ObjectId, ratio: System.Double) -> ObjectId
            Creates a new instance of a GeneralSegmentLabel at a specified location on a feature object with the default line label style and curve label style.
            Remarks: featureId should be the ObjectId of a Line, Arc, Polyline or Featureline.For Line and Arc objects, the ratio should be in the range of [0, 1].For Polyline and FeatureLine objects with n segments, the ratio should be in the range of [0, n].
            featureId: ObjectId - The ObjectId of the feature object to label.
            ratio: System.Double - The ratio that sets the relative position of the label to the feature.
        Create(featureId: ObjectId, ratio: System.Double, lineLabelStyleId: ObjectId, curveLabelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a GeneralSegmentLabel on a feature object with the specified line label and curve label styles.
            Remarks: featureId should be the ObjectId of a Line, Arc, Polyline or Featureline.For Line and Arc objects, the ratio should be in the range of [0, 1].For Polyline and FeatureLine objects, the ratio should be in the range [0, n], where n is the number of segments in the object.
            featureId: ObjectId - The ObjectId of the feature object to label (object type Line, Arc, Polyline or Featureline).
            ratio: System.Double - The ratio that sets the relative position of the label to the feature.
            lineLabelStyleId: ObjectId - The ObjectId of the line Label style (object type LabelStyle) to use.
            curveLabelStyleId: ObjectId - The ObjectId of the curve Label style (object type LabelStyle) to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(featureId: ObjectId) -> ObjectIdCollection
            Gets the ObjectIdCollection of all GeneralSegmentLabels for a feature.
            Remarks: featureId should be the ObjectId of a Line, Arc, Polyline or Featureline.
            featureId: ObjectId - The ObjectId of a feature object (Line, Arc, Polyline or Featureline).
        """
        pass
    
    pass

class GeneralSurfaceProperties(object):
    """
    This class encapsulates general surface statistics information.
    """

    pass

class GeoEntity(Entity):
    """
    The base class for geometry db entities.
    """


    pass

class Grading(Entity):
    """
    The Grading class.
    """


    pass

class GradingSmoothOption():
    """
    This class is used to save horizontal deviation, weeding distance, and arc inclusion distance options for smoothing operations.
    """
    ArcInclusionDistance = None
    HorizDeviation = None
    NeedSmooth = None
    WeedingDistance = None
    pass

class Graph(Entity):
    """
    The base class for graphic entities.
    """
    Location = None

    pass

class GraphBandSet(ProfileViewBandSet):
    """
    
    """
    MatchIncrementToGridIntervals = None
    def ImportBandSetStyle(self):
        """
        ImportBandSetStyle(bandSetId: ObjectId)
            Import  an existing band set style to the current graph.
            bandSetId: ObjectId
        """
        pass
    
    
    def SaveAsBandSetStyle(self):
        """
        SaveAsBandSetStyle(name: System.String) -> ObjectId
            Saves the current band set data as a band set style.
            name: System.String
        """
        pass
    
    pass

class GraphOverride(PipeOverride):
    """
    The base class for graphic override.
    """
    Draw = None
    OverrideStyleId = None
    OverrideStyleName = None
    UseOverrideStyle = None
    pass

class GraphOverrideCollection(PipeOverrideCollection):
    """
    The GraphOverride collection class represents the collection of all override items listed in the Graph.
    """
    ClipGridAt = None
    Count = None
    Item = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the GraphOverrideCollection<ItemType>
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<ItemType>
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

class GridLocation():
    """
    The GridLocation class.
    This class represents a location in a GridSurface.
    """
    ColumnIndex = None
    RowIndex = None
    def Equals(self):
        """
        Equals(obj: System.Object) -> bool
            obj: System.Object
        """
        pass
    
    pass

class GridSurface(Entity):
    """
    This class encapsulates a GridSurface.
    """
    Cells = None
    DEMFilesDefinition = None
    Vertices = None
    def AddPoint(self):
        """
        AddPoint(location: Autodesk.Civil.DatabaseServices.GridLocation, elevation: System.Double) -> SurfaceOperationAddGridPoint
            Adds a point to the GridSurface.
            location: Autodesk.Civil.DatabaseServices.GridLocation - 
            The location where the grid point will be added.
            elevation: System.Double - 
            The elevation of the grid point to be added.
        """
        pass
    
    
    def Create(self):
        """
        Create(database: Database, surfaceName: System.String, spacingX: System.Double, spacingY: System.Double, orientation: System.Double) -> ObjectId
            Creates a new instance of a GridSurface and adds it to the specified database.
            Remarks: The units for spacingX, spacingY and orientation are taken from the settings in SettingsCmdCreateSurface.
            The default surface style is applied to the new GridSurface object.
            database: Database - The database where the new GridSurface is created.
            surfaceName: System.String - The name of the GridSurface.
            spacingX: System.Double - The x spacing of the GridSurface.
            spacingY: System.Double - The y spacing of the GridSurface.
            orientation: System.Double - The orientation of the GridSurface.
        Create(surfaceName: System.String, spacingX: System.Double, spacingY: System.Double, orientation: System.Double, styleId: ObjectId) -> ObjectId
            Creates a new instance of a GridSurface and adds it to the database that contains styleId.
            Remarks: The units for spacingX, spacingY and orientation are taken from the settings in SettingsCmdCreateSurface.
            surfaceName: System.String - The name of the new GridSurface.
            spacingX: System.Double - The x spacing of the GridSurface.
            spacingY: System.Double - The y spacing of the GridSurface.
            orientation: System.Double - The orientation of the GridSurface.
            styleId: ObjectId - The ObjectId of the style to apply to the GridSurface.
        """
        pass
    
    
    def CreateFromDEM(self):
        """
        CreateFromDEM(database: Database, DEMFileName: System.String) -> ObjectId
            Creates a new instance of a GridSurface from a DEM file and adds it to the specified database.
            Remarks: The default surface style is applied to the new GridSurface object.
            database: Database - The database where the new GridSurface is created.
            DEMFileName: System.String - The path of the DEM file.
        CreateFromDEM(DEMFileName: System.String, styleId: ObjectId) -> ObjectId
            Creates a new instance of a GridSurface from a DEM file and adds it to the database that contains styleId.
            DEMFileName: System.String - The path of the DEM file.
            styleId: ObjectId - The ObjectId of the SurfaceStyle for the GridSurface.
        """
        pass
    
    
    def DeleteLine(self):
        """
        DeleteLine(edge: Autodesk.Civil.DatabaseServices.GridSurfaceEdge) -> SurfaceOperationDeleteLine
            Deletes a line from the GridSurface object.
            edge: Autodesk.Civil.DatabaseServices.GridSurfaceEdge - The grid surface edge to be deleted.
        """
        pass
    
    
    def DeleteLines(self):
        """
        DeleteLines(edges: System.Collections.Generic.IEnumerable) -> SurfaceOperationDeleteMultipleLines
            Deletes multiple lines from the GridSurface object.
            edges: System.Collections.Generic.IEnumerable - The grid surface edges to be deleted.
        """
        pass
    
    
    def DeletePoint(self):
        """
        DeletePoint(location: Autodesk.Civil.DatabaseServices.GridLocation) -> SurfaceOperationDeleteGridPoint
            Deletes a point from the GridSurface object.
            location: Autodesk.Civil.DatabaseServices.GridLocation - The location of the point to be deleted.
        """
        pass
    
    
    def DeletePoints(self):
        """
        DeletePoints(locations: System.Collections.Generic.IEnumerable) -> SurfaceOperationDeleteMultipleGridPoints
            Deletes multiple points from the GridSurface object.
            locations: System.Collections.Generic.IEnumerable - Locations of points to be deleted.
        """
        pass
    
    
    def ExtractBorder(self):
        """
        ExtractBorder(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface border information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the border information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def ExtractContours(self):
        """
        ExtractContours(interval: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation interval.
            interval: System.Double - 
            The specified elevation interval.
        ExtractContours(interval: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation interval with smoothing.
            interval: System.Double - 
            The specified elevation interval.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only.
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        ExtractContours(lowElev: System.Double, highElev: System.Double, interval: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation range and interval.
            lowElev: System.Double - 
            The specified lower elevation.
            highElev: System.Double - 
            The specified high elevation.
            interval: System.Double - 
            The specified elevation interval.
        ExtractContours(lowElev: System.Double, highElev: System.Double, interval: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation range and interval with smoothing.
            lowElev: System.Double - 
            The specified lower elevation.
            highElev: System.Double - 
            The specified high elevation.
            interval: System.Double - 
            The specified elevation interval.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractContoursAt(self):
        """
        ExtractContoursAt(elevation: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation.
            elevation: System.Double - 
            The specified elevation.
        ExtractContoursAt(elevation: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation with smoothing.
            elevation: System.Double - 
            The specified elevation.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, the smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractGridded(self):
        """
        ExtractGridded(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface grid information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the grid information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def ExtractMajorContours(self):
        """
        ExtractMajorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface major contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        ExtractMajorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> SurfaceExtractionSettingsType
            Extracts the surface major contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractMinorContours(self):
        """
        ExtractMinorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface minor contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        ExtractMinorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> SurfaceExtractionSettingsType
            Extracts the surface minor contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractWatershed(self):
        """
        ExtractWatershed(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface watershed information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the watershed information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def FindCellAtXY(self):
        """
        FindCellAtXY(x: System.Double, y: System.Double) -> GridSurfaceCell
            Finds the grid cell containing location (x, y).
            Remarks: When the method can't find a cell at location (x, y), it means that (x, y) is not on the surface.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def FindEdgeAtXY(self):
        """
        FindEdgeAtXY(x: System.Double, y: System.Double) -> GridSurfaceEdge
            Finds out the closest GridSurfaceEdge near location (x, y).
            Remarks: When the method can't find an edge at location (x, y), it means that (x, y) is not on the surface.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def FindVertexAtXY(self):
        """
        FindVertexAtXY(x: System.Double, y: System.Double) -> GridSurfaceVertex
            Finds out the closest GridSurfaceVertex near location (x, y).
            Remarks: When the method can't find a vertex at location (x, y), it means that (x, y) is not on the surface.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def GetCells(self):
        """
        GetCells(includeInvisible: System.Boolean) -> GridSurfaceCellCollection
            Gets all cells in the GridSurface.
            includeInvisible: System.Boolean - Indicates whether this method should return invisible cells.
        """
        pass
    
    
    def GetGridProperties(self):
        """
        GetGridProperties() -> GridSurfaceProperties
            Gets the Grid properties of the surface.
        """
        pass
    
    
    def GetTerrainProperties(self):
        """
        GetTerrainProperties() -> TerrainSurfaceProperties
            Gets the Terrain properties of the surface.
        """
        pass
    
    
    def GetVertices(self):
        """
        GetVertices(includeInvisible: System.Boolean) -> GridSurfaceVertexCollection
            Gets all vertices in the GridSurface.
            includeInvisible: System.Boolean - Indicates whether this method should return invisible vertices.
        """
        pass
    
    
    def RaisePoints(self):
        """
        RaisePoints(locations: System.Collections.Generic.IEnumerable, deltaElevation: System.Double) -> SurfaceOperationModifyMultipleGridPointsElevation
            Raises or lowers multiple points in the GridSurface object.
            Remarks: If deltaElevation is positive, points are raised.  If deltaElevation is negative, points are lowered.
            locations: System.Collections.Generic.IEnumerable - The locations of points to be raised or lowered.
            deltaElevation: System.Double - Delta elevation for the points.
        """
        pass
    
    
    def RaiseSurface(self):
        """
        RaiseSurface(deltaElevation: System.Double) -> SurfaceOperationRaise
            Raises or lowers the surface.
            deltaElevation: System.Double - 
            The elevation delta. A positive value raises the elevation while a negative value lowers the elevation.
        """
        pass
    
    
    def SampleElevations(self):
        """
        SampleElevations(curveId: ObjectId) -> Point3dCollection
            Gets the sampled points along a curve entity.
            curveId: ObjectId - An ObjectId of Autodesk.AutoCAD.DatabaseServices.Curve. The curve can be a line, arc and so on.
        SampleElevations(pt1: Point3d, pt2: Point3d) -> Point3dCollection
            pt1: Point3d
            pt2: Point3d
        """
        pass
    
    
    def SetPointElevation(self):
        """
        SetPointElevation(location: Autodesk.Civil.DatabaseServices.GridLocation, newElevation: System.Double) -> SurfaceOperationModifyGridPointElevation
            Sets the elevation of a point in the GridSurface object.
            location: Autodesk.Civil.DatabaseServices.GridLocation - The location of point to be set with new elevation.
            newElevation: System.Double - New elevation for the point.
        """
        pass
    
    
    def SetPointsElevation(self):
        """
        SetPointsElevation(locations: System.Collections.Generic.IEnumerable, newElevation: System.Double) -> SurfaceOperationModifyMultipleGridPointsElevation
            Sets the elevation of multiple points in the GridSurface object.
            locations: System.Collections.Generic.IEnumerable - The locations of points to be set with new elevation.
            newElevation: System.Double - New elevation for the points.
        """
        pass
    
    pass

class GridSurfaceCell(GridSurfaceObject):
    """
    This class encapsulates a cell in a GridSurface.
    """
    BottomEdge = None
    BottomLeftVertex = None
    BottomRightVertex = None
    GridLocation = None
    LeftEdge = None
    RightEdge = None
    TopEdge = None
    TopLeftVertex = None
    TopRightVertex = None
    def Equals(self):
        """
        Equals(rhs: System.Object) -> bool
            rhs: System.Object
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode() -> int
        """
        pass
    
    pass

class GridSurfaceCellCollection(object):
    """
    This class encapsulates a collection of GridSurfaceCell objects.
    """
    Count = None
    def Contains(self):
        """
        Contains(location: Autodesk.Civil.DatabaseServices.GridLocation) -> GridLocation
            Gets whether there's a cell at the specified grid location.
            location: Autodesk.Civil.DatabaseServices.GridLocation
        """
        pass
    
    
    def GetAt(self):
        """
        GetAt(location: Autodesk.Civil.DatabaseServices.GridLocation) -> GridSurfaceCell
            Gets the cell at the specified location.
            location: Autodesk.Civil.DatabaseServices.GridLocation
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> GridSurfaceCell
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetIndexRange(self):
        """
        GetIndexRange(minColIndex: System.Int32, minRowIndex: System.Int32, maxColIndex: System.Int32, maxRowIndex: System.Int32)
            Gets the minimum column index, minimum row index, maximum column index and maximum row index.
            Remarks: The index can be negative.
            minColIndex: System.Int32
            minRowIndex: System.Int32
            maxColIndex: System.Int32
            maxRowIndex: System.Int32
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class GridSurfaceCellEnumerator(object):
    """
    
    """
    Current = None
    CurrentObject = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the GridSurfaceCellEnumerator
        """
        pass
    
    
    def MoveNext(self):
        """
        MoveNext() -> bool
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
        """
        pass
    
    pass

class GridSurfaceEdge(GridSurfaceObject):
    """
    This class encapsulates the edge of a GridSurface.
    """
    Cell1 = None
    Cell2 = None
    IsValid = None
    Vertex1 = None
    Vertex2 = None
    def Equals(self):
        """
        Equals(rhs: System.Object) -> bool
            rhs: System.Object
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode() -> int
        """
        pass
    
    pass

class GridSurfaceObject(GridSurfaceCell):
    """
    The base class for GridSurface data objects, such as GridSurfaceVertex, GridSurfaceTriangle, etc.
    """
    IsValid = None
    Surface = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the GridSurfaceObject
        """
        pass
    
    pass

class GridSurfaceProperties(object):
    """
    This class encapsulates grid surface statistics information.
    """

    pass

class GridSurfaceVertex(GridSurfaceObject):
    """
    This class encapsulates a vertex in a GridSurface.
    """
    GridLocation = None
    Location = None
    def Equals(self):
        """
        Equals(rhs: System.Object) -> bool
            rhs: System.Object
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode() -> int
        """
        pass
    
    pass

class GridSurfaceVertexCollection(object):
    """
    This class encapsulates a collection of GridSurfaceVertex objects.
    """
    Count = None
    def Contains(self):
        """
        Contains(location: Autodesk.Civil.DatabaseServices.GridLocation) -> GridLocation
            Gets whether there's a vertex at the specified grid location.
            location: Autodesk.Civil.DatabaseServices.GridLocation
        """
        pass
    
    
    def GetAt(self):
        """
        GetAt(location: Autodesk.Civil.DatabaseServices.GridLocation) -> GridSurfaceVertex
            Gets the vertex at the specified location.
            location: Autodesk.Civil.DatabaseServices.GridLocation
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> GridSurfaceVertex
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetIndexRange(self):
        """
        GetIndexRange(minColIndex: System.Int32, minRowIndex: System.Int32, maxColIndex: System.Int32, maxRowIndex: System.Int32)
            Gets the minimum column index, minimum row index, maximum column index and maximum row index.
            Remarks: The index can be negative.
            minColIndex: System.Int32
            minRowIndex: System.Int32
            maxColIndex: System.Int32
            maxRowIndex: System.Int32
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class GridSurfaceVertexEnumerator(object):
    """
    
    """
    Current = None
    CurrentObject = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the GridSurfaceVertexEnumerator
        """
        pass
    
    
    def MoveNext(self):
        """
        MoveNext() -> bool
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
        """
        pass
    
    pass

class GridVolumeSurface(Entity):
    """
    The GridVolumeSurface class.
    This class encapsulates a grid volume surface.
    """
    CutFactor = None
    FillFactor = None
    def Create(self):
        """
        Create(surfaceName: System.String, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, spacingX: System.Double, spacingY: System.Double, orientation: System.Double) -> ObjectId
            Creates a new instance of a GridVolumeSurface object and adds it to the database where the base surface specified by baseSurfaceId is located.
            Remarks: This method uses the default style for the surface so you don't need to provide a style ObjectId.
            surfaceName: System.String - The name of the new GridVolumeSurface.
            baseSurfaceId: ObjectId - The ObjectId of the base surface for the GridVolumeSurface.
            comparisonSurfaceId: ObjectId - The ObjectId of the comparison (top) surface for the GridVolumeSurface.
            spacingX: System.Double - The x spacing of the GridVolumeSurface.
            spacingY: System.Double - The y spacing of the GridVolumeSurface.
            orientation: System.Double - The orientation of the GridVolumeSurface.
        Create(surfaceName: System.String, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, spacingX: System.Double, spacingY: System.Double, orientation: System.Double, styleId: ObjectId) -> ObjectId
            Creates a new instance of a GridVolumeSurface object and adds it to the database where the base surface specified by baseSurfaceId is located.
            Remarks: This method takes a style, specified by styleId, to apply to the newly created surface.
            surfaceName: System.String - The name of the new GridVolumeSurface.
            baseSurfaceId: ObjectId - The ObjectId of the base surface for the GridVolumeSurface.
            comparisonSurfaceId: ObjectId - The ObjectId of the comparison surface for the GridVolumeSurface.
            spacingX: System.Double - The x spacing of the GridVolumeSurface.
            spacingY: System.Double - The y spacing of the GridVolumeSurface.
            orientation: System.Double - The orientation of the GridVolumeSurface.
            styleId: ObjectId - The ObjectId of the style for the GridVolumeSurface.
        """
        pass
    
    
    def GetGridProperties(self):
        """
        GetGridProperties() -> GridSurfaceProperties
            Gets the Grid properties of the surface.
            Remarks: The grid surface properties include orientation, and x and y spacing.
        """
        pass
    
    
    def GetVolumeProperties(self):
        """
        GetVolumeProperties() -> VolumeSurfaceProperties
            Gets the Volume properties of the surface.
        """
        pass
    
    pass

class HardcodedOffsetBaseline(BaseBaseline):
    """
    An offset baseline is a secondary baseline within a corridor that is offset from the main baseline. The distance 
    between this kind offset baseline and the main baseline is a constant. These are used to create complicated corridor 
    structures or to attach assemblies to a point outside the main baseline of a corridor.
    """
    AlignmentId = None
    BaselineType = None
    Name = None
    OffsetElevationFromMainBaseline = None
    ProfileId = None
    RelatedOffsetBaselineFeatureLines = None
    def IsFeatureLineBased(self):
        """
        IsFeatureLineBased() -> bool
            Indicates whether the specific baseline of corridor is feature line based or not.
            Remarks: If this hard coded offset baseline is feature line based, then it will return true.
        """
        pass
    
    
    def SortedStations(self):
        """
        SortedStations() -> double[]
            Returns an array of all the station values for the Baseline.
        """
        pass
    
    pass

class HatchCriteriaBoundaryType():
    """
    Defines the hatch criteria's boundary type.
    """
    pass

class HoldOnResizeType():
    """
    Specifies the pipe behavior that occurs when the pipe is automatically resized.
    """
    pass

class HorizontalGeometryBandLabelGroup(Entity):
    """
    
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all HorizontalGeometryBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns a collection of object ids pointing to all the available HorizontalGeometryBandLabelGroup objects on the specified profile view.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of HorizontalGeometryBandLabelGroup.
        """
        pass
    
    pass

class IAppliedSubassemblyParam():
    """
    An interface used to get or set applied subassembly parameter properties.
    """
    Comment = None
    DesignValueAsObject = None
    DisplayName = None
    IsOverriden = None
    KeyName = None
    ValueAsObject = None
    ValueType = None
    def ClearOverride(self):
        """
        ClearOverride() -> bool
            Clear parameter override.
        """
        pass
    
    pass

class ICommonLabel():
    """
    The interface ICommonLabel declares properties and methods common to all classes representing labels.
    """
    AnchorInfo = None
    AnchorMarkerRotationAngle = None
    AnchorMarkerStyleId = None
    CanRotate = None
    DimensionAnchorInfo = None
    DimensionAnchorOption = None
    DimensionAnchorValue = None
    Dragged = None
    DraggedOffset = None
    Flipped = None
    LeaderAttachment = None
    LeaderTailVisibility = None
    LeaderVisibility = None
    Pinned = None
    Reversed = None
    RotationAngle = None
    StyleId = None
    def ClearAllTextComponentOverrides(self):
        """
        ClearAllTextComponentOverrides()
            Clears all text component overrides in the label.
        """
        pass
    
    
    def GetReferenceTextTarget(self):
        """
        GetReferenceTextTarget(referenceTextComponentId: ObjectId) -> ObjectId
            Get the ObjectId of civil object which is referred by specified reference text component.
            referenceTextComponentId: ObjectId - The ObjectId of the reference text component.
        """
        pass
    
    
    def GetTextComponentIds(self):
        """
        GetTextComponentIds() -> ObjectIdCollection
            Gets a collection of object ids that represent the text components in a label.
            Remarks: Gets all the components with a type of LabelStyleComponentType.Text, ReferenceText or TextForEach.
        """
        pass
    
    
    def GetTextComponentJustificationOverride(self):
        """
        GetTextComponentJustificationOverride(labelStyleComponentId: ObjectId) -> TextJustificationType
            Get the overriden justification on the specified text component.
            labelStyleComponentId: ObjectId
        """
        pass
    
    
    def GetTextComponentOverride(self):
        """
        GetTextComponentOverride(labelStyleComponentId: ObjectId) -> string
            Get the overriden text on the specified text component.
            labelStyleComponentId: ObjectId
        """
        pass
    
    
    def IsTextComponentOverriden(self):
        """
        IsTextComponentOverriden(labelStyleComponentId: ObjectId) -> bool
            Returns whether the specified text component is overridden.
            labelStyleComponentId: ObjectId - The object id of text component.
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
            Resets the label object to its defaults.
        """
        pass
    
    
    def ResetLocation(self):
        """
        ResetLocation()
            Resets the location of the label object to its default.
        """
        pass
    
    
    def ResetProperties(self):
        """
        ResetProperties()
            Resets the properties of the label object to its defaults.
        """
        pass
    
    
    def SetReferenceTextTarget(self):
        """
        SetReferenceTextTarget(referenceTextComponentId: ObjectId, referenceObjectId: ObjectId)
            Makes the reference text component refer to other civil object.
            referenceTextComponentId: ObjectId - The ObjectId of the reference text component.
            referenceObjectId: ObjectId - The ObjectId of a Civil Object which will be referenced by text component.
        """
        pass
    
    
    def SetTextComponentJustificationOverride(self):
        """
        SetTextComponentJustificationOverride(labelStyleComponentId: ObjectId, textJustificationType: Autodesk.Civil.TextJustificationType) -> TextJustificationType
            Overrides the justification on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textJustificationType: Autodesk.Civil.TextJustificationType - The type of text justification to set.
        """
        pass
    
    
    def SetTextComponentOverride(self):
        """
        SetTextComponentOverride(labelStyleComponentId: ObjectId, textOverride: System.String)
            Overrides the text on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textOverride: System.String - The override label text.
        SetTextComponentOverride(labelStyleComponentId: ObjectId, textOverride: System.String, textJustificationType: Autodesk.Civil.TextJustificationType) -> TextJustificationType
            Overrides the text and justification on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textOverride: System.String - The override label text.
            textJustificationType: Autodesk.Civil.TextJustificationType - The type of text justification.
        """
        pass
    
    pass

class ICommonLabelOptions():
    """
    The interface ICommonLabelOptions declares common behavioral options on labels.
    """
    AllowsAnchorMarker = None
    AllowsDimensionAnchors = None
    AllowsDragging = None
    AllowsFlipping = None
    AllowsLeaderAttachment = None
    AllowsPinning = None
    AllowsReversing = None
    DefaultDimensionAnchorOption = None
    DefaultDimensionAnchorValue = None
    RotationType = None
    pass

class IGridSurface():
    """
    This interface declares common methods for Grid Surfaces.
    """
    def GetGridProperties(self):
        """
        GetGridProperties() -> GridSurfaceProperties
            Gets the Grid properties of the surface.
        """
        pass
    
    pass

class IPoint():
    """
    
    """
    Codes = None
    Elevation = None
    Index = None
    Offset = None
    Station = None
    pass

class ITerrainSurface():
    """
    This interface declares common methods for Terrain Surfaces.
    """
    DEMFilesDefinition = None
    def ExtractBorder(self):
        """
        ExtractBorder(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface border information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the border information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def ExtractContours(self):
        """
        ExtractContours(interval: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation interval.
            interval: System.Double - 
            The specified elevation interval.
        ExtractContours(interval: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation interval with smoothing.
            interval: System.Double - 
            The specified elevation interval.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only.
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        ExtractContours(lowElev: System.Double, highElev: System.Double, interval: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation range and interval.
            lowElev: System.Double - 
            The specified lower elevation.
            highElev: System.Double - 
            The specified high elevation.
            interval: System.Double - 
            The specified elevation interval.
        ExtractContours(lowElev: System.Double, highElev: System.Double, interval: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation range and interval with smoothing.
            lowElev: System.Double - 
            The specified lower elevation.
            highElev: System.Double - 
            The specified high elevation.
            interval: System.Double - 
            The specified elevation interval.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractContoursAt(self):
        """
        ExtractContoursAt(elevation: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation.
            elevation: System.Double - 
            The specified elevation.
        ExtractContoursAt(elevation: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation with smoothing.
            elevation: System.Double - 
            The specified elevation.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, the smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractGridded(self):
        """
        ExtractGridded(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface grid information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the grid information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def ExtractMajorContours(self):
        """
        ExtractMajorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface major contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        ExtractMajorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> SurfaceExtractionSettingsType
            Extracts the surface major contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractMinorContours(self):
        """
        ExtractMinorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface minor contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        ExtractMinorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> SurfaceExtractionSettingsType
            Extracts the surface minor contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractWatershed(self):
        """
        ExtractWatershed(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface watershed information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the watershed information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def GetTerrainProperties(self):
        """
        GetTerrainProperties() -> TerrainSurfaceProperties
            Gets the Terrain properties of the surface.
        """
        pass
    
    
    def RaiseSurface(self):
        """
        RaiseSurface(deltaElevation: System.Double) -> SurfaceOperationRaise
            Raises or lowers the surface.
            deltaElevation: System.Double - 
            The elevation delta. A positive value raises the elevation while a negative value lowers the elevation.
        """
        pass
    
    
    def SampleElevations(self):
        """
        SampleElevations(curveId: ObjectId) -> Point3dCollection
            Gets the sampled points along a curve entity.
            curveId: ObjectId - An ObjectId of Autodesk.AutoCAD.DatabaseServices.Curve. The curve can be a line, arc and so on.
        """
        pass
    
    pass

class ITinSurface():
    """
    This interface declares common methods for TIN Surfaces.
    """
    def GetTinProperties(self):
        """
        GetTinProperties() -> TinSurfaceProperties
            Gets the TIN properties of the surface.
        """
        pass
    
    pass

class IVolumeSurface():
    """
    This interface declares common methods and properties for Volume Surfaces.
    """
    CutFactor = None
    FillFactor = None
    def GetVolumeProperties(self):
        """
        GetVolumeProperties() -> VolumeSurfaceProperties
            Gets the Volume properties of the surface.
        """
        pass
    
    pass

class Interference(Entity):
    """
    Represents one location where elements of a pipe network interfere with each other.
    """
    Network1Id = None
    Network2Id = None

    pass

class InterferenceCheck(Entity):
    """
    Determines where pipes and structures intersect or are too close to each other, and holds a collection of the resulting interferences (Interference).
    """


    pass

class Intersection(Entity):
    """
    An object that manages the intersection of two Alignments. An intersection object builds on and manages various object data, including alignments, profiles, corridors, assemblies, subassemblies, and surfaces.
    """
    CorridorId = None
    GradeRuleType = None
    IntersectionRegions = None
    IntersectionRoads = None
    Location = None
    RoadwayDrivingDirection = None
    def GetIntersectionLocaitonLabelIds(self):
        """
        GetIntersectionLocaitonLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the IntersectionLocaitonLabels on the Intersection.
        """
        pass
    
    pass

class IntersectionCorridorType():
    """
    Specifies the corridor grade option for the corridors created in the intersection area. 
    Primary Road Crown Maintained: When this options is selected, the primary road crown is maintained through the intersection. 
    All Crowns Maintained: When this options is selected, the crowns of both roads included in the intersection are maintained through the intersection.
    """
    pass

class IntersectionLocationLabel(Entity):
    """
    This class represents an intersection location label.
    """

    def Create(self):
        """
        Create(intersectionId: ObjectId) -> ObjectId
            Creates a new instance of IntersectionLocationLabel on the specified Intersection using the default label style.
            intersectionId: ObjectId - The ObjectId of the Intersection to label.
        Create(intersectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of an IntersectionLocationLabel on the specified Intersection using the specified label style.
            intersectionId: ObjectId - The ObjectId of the Intersection to label.
            labelStyleId: ObjectId - The ObjectId of IntersectionLocationLabel style (object type LabelStyle).
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(intersectionId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of all IntersectionLocationLabel objects for the specified Intersection.
            intersectionId: ObjectId - The ObjectId of the Intersection.
        """
        pass
    
    pass

class IntersectionRegion(object):
    """
    Corridor regions in an Intersection area.
    """
    Angle = None
    CurbReturnAlignmentId = None
    CurbReturnProfileId = None
    InAlignmentId = None
    Name = None
    OutAlignmentId = None
    pass

class IntersectionRegionCollection(object):
    """
    A collection of IntersectionRegion objects.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> IntersectionRegion
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    pass

class IntersectionRoad(object):
    """
    Road components managed by an Intersection object.
    """
    CenterlineAlignmentId = None
    CenterlineProfileId = None
    OffsetLeftAlignmentId = None
    OffsetLeftProfileId = None
    OffsetRightAlignmentId = None
    OffsetRightProfileId = None
    pass

class IntersectionRoadCollection(object):
    """
    A collection of IntersectionRoad objecs managed by an Intersection object.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> IntersectionRoad
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

class KrigingMethodOptions(object):
    """
    The class encapsulates information about the sample data and semivariogram model required to smooth a surface using the Kriging method.
    """
    NuggetEffect = None
    SampleVertices = None
    SemivariogramModel = None
    VariogramParamA = None
    VariogramParamC = None
    pass

class Label(Entity):
    """
    The base class for all single-entity label objects.
    """
    AnchorInfo = None
    AnchorMarkerRotationAngle = None
    AnchorMarkerStyleId = None
    CanRotate = None
    DimensionAnchorInfo = None
    DimensionAnchorOption = None
    DimensionAnchorValue = None
    Dragged = None
    DraggedOffset = None
    Flipped = None
    LabelLocation = None
    LeaderAttachment = None
    LeaderTailVisibility = None
    LeaderVisibility = None
    Pinned = None
    Reversed = None
    RotationAngle = None
    StyleId = None
    StyleName = None
    def ClearAllTextComponentOverrides(self):
        """
        ClearAllTextComponentOverrides()
            Clears all text component overrides in the label.
        """
        pass
    
    
    def GetReferenceTextTarget(self):
        """
        GetReferenceTextTarget(referenceTextComponentId: ObjectId) -> ObjectId
            Get the ObjectId of civil object which is referred by specified reference text component.
            referenceTextComponentId: ObjectId - The ObjectId of the reference text component.
        """
        pass
    
    
    def GetTextComponentIds(self):
        """
        GetTextComponentIds() -> ObjectIdCollection
            Gets a collection of object ids that represent the text components in a label.
            Remarks: Gets all the components with a type of LabelStyleComponentType.Text, ReferenceText or TextForEach.
        """
        pass
    
    
    def GetTextComponentJustificationOverride(self):
        """
        GetTextComponentJustificationOverride(labelStyleComponentId: ObjectId) -> TextJustificationType
            Get the overriden justification on the specified text component.
            labelStyleComponentId: ObjectId
        """
        pass
    
    
    def GetTextComponentOverride(self):
        """
        GetTextComponentOverride(labelStyleComponentId: ObjectId) -> string
            Get the overriden text on the specified text component.
            labelStyleComponentId: ObjectId
        """
        pass
    
    
    def IsTextComponentOverriden(self):
        """
        IsTextComponentOverriden(labelStyleComponentId: ObjectId) -> bool
            Returns whether the specified text component is overridden.
            labelStyleComponentId: ObjectId - The object id of text component.
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
            Resets the label object to its defaults.
        """
        pass
    
    
    def ResetLocation(self):
        """
        ResetLocation()
            Resets the location of the label object to its default.
        """
        pass
    
    
    def ResetProperties(self):
        """
        ResetProperties()
            Resets the properties of the label object to its defaults.
        """
        pass
    
    
    def SetReferenceTextTarget(self):
        """
        SetReferenceTextTarget(referenceTextComponentId: ObjectId, referenceObjectId: ObjectId)
            Makes the reference text component refer to other civil object.
            referenceTextComponentId: ObjectId - The ObjectId of the reference text component.
            referenceObjectId: ObjectId - The ObjectId of a Civil Object which will be referenced by text component.
        """
        pass
    
    
    def SetTextComponentJustificationOverride(self):
        """
        SetTextComponentJustificationOverride(labelStyleComponentId: ObjectId, textJustificationType: Autodesk.Civil.TextJustificationType) -> TextJustificationType
            Overrides the justification on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textJustificationType: Autodesk.Civil.TextJustificationType - The type of text justification to set.
        """
        pass
    
    
    def SetTextComponentOverride(self):
        """
        SetTextComponentOverride(labelStyleComponentId: ObjectId, textOverride: System.String)
            Overrides the text on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textOverride: System.String - The override label text.
        SetTextComponentOverride(labelStyleComponentId: ObjectId, textOverride: System.String, textJustificationType: Autodesk.Civil.TextJustificationType) -> TextJustificationType
            Overrides the text and justification on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textOverride: System.String - The override label text.
            textJustificationType: Autodesk.Civil.TextJustificationType - The type of text justification.
        """
        pass
    
    pass

class LabelBase(Entity):
    """
    The base class for all label classes, including single-feature labels (FeatureLabel derived classes) and group labels (LabelGroup derived classes).  This class implements the ICommonLabelOptions interface, which defines common label behaviors.
    """
    AllowsAnchorMarker = None
    AllowsDimensionAnchors = None
    AllowsDragging = None
    AllowsFlipping = None
    AllowsLeaderAttachment = None
    AllowsPinning = None
    AllowsReversing = None
    AutoStagger = None
    DefaultDimensionAnchorOption = None
    DefaultDimensionAnchorValue = None
    FeatureId = None
    Mask = None
    RotationType = None
    ViewId = None

    pass

class LabelGroup(Entity):
    """
    The base class for all label group objects, such as AutoFeatureLabelGroup.
    """
    DefaultDimensionAnchorOption = None
    DefaultDimensionAnchorValue = None
    StyleId = None
    StyleName = None
    SubEntities = None
    SubEntityCount = None
    def GetAt(self):
        """
        GetAt(index: System.UInt32) -> LabelGroupSubEntity
            Gets one LabelGroupSubEntity from label group according the index.
            index: System.UInt32
        """
        pass
    
    
    def ResetAllSubCommonLabelLocations(self):
        """
        ResetAllSubCommonLabelLocations()
            Resets the location of all the sub-entity labels to their defaults.
        """
        pass
    
    
    def ResetAllSubCommonLabelProperties(self):
        """
        ResetAllSubCommonLabelProperties()
            Resets the properties of all the sub-entity labels to their defaults.
        """
        pass
    
    
    def ResetAllSubCommonLabels(self):
        """
        ResetAllSubCommonLabels()
            Resets all the sub-entity labels (properties and location).
        """
        pass
    
    pass

class LabelGroupSubEntity(object):
    """
    A class that represents individual labels in a label group.
    """
    AllowsAnchorMarker = None
    AllowsDimensionAnchors = None
    AllowsDragging = None
    AllowsFlipping = None
    AllowsLeaderAttachment = None
    AllowsPinning = None
    AllowsReversing = None
    AnchorInfo = None
    AnchorMarkerRotationAngle = None
    AnchorMarkerStyleId = None
    CanRotate = None
    DefaultDimensionAnchorOption = None
    DefaultDimensionAnchorValue = None
    DimensionAnchorInfo = None
    DimensionAnchorOption = None
    DimensionAnchorValue = None
    Dragged = None
    DraggedOffset = None
    Flipped = None
    Index = None
    LabelLocation = None
    LeaderAttachment = None
    LeaderTailVisibility = None
    LeaderVisibility = None
    Parent = None
    Pinned = None
    Reversed = None
    RotationAngle = None
    RotationType = None
    StyleId = None
    Visibility = None
    def ClearAllTextComponentOverrides(self):
        """
        ClearAllTextComponentOverrides()
            Clears all text component overrides in the label.
        """
        pass
    
    
    def GetReferenceTextTarget(self):
        """
        GetReferenceTextTarget(referenceTextComponentId: ObjectId) -> ObjectId
            Get the ObjectId of civil object which is referred by specified reference text component.
            referenceTextComponentId: ObjectId - The ObjectId of the reference text component.
        """
        pass
    
    
    def GetTextComponentIds(self):
        """
        GetTextComponentIds() -> ObjectIdCollection
            Gets a collection of object ids that represent the text components in a label.
            Remarks: Gets all the components with a type of LabelStyleComponentType.Text, ReferenceText or TextForEach.
        """
        pass
    
    
    def GetTextComponentJustificationOverride(self):
        """
        GetTextComponentJustificationOverride(labelStyleComponentId: ObjectId) -> TextJustificationType
            Get the overriden justification on the specified text component.
            labelStyleComponentId: ObjectId
        """
        pass
    
    
    def GetTextComponentOverride(self):
        """
        GetTextComponentOverride(labelStyleComponentId: ObjectId) -> string
            Get the overriden text on the specified text component.
            labelStyleComponentId: ObjectId
        """
        pass
    
    
    def IsTextComponentOverriden(self):
        """
        IsTextComponentOverriden(newVal: ObjectId) -> bool
            Returns whether the specified text component is overridden.
            newVal: ObjectId
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
            Resets the label object to its defaults.
        """
        pass
    
    
    def ResetLocation(self):
        """
        ResetLocation()
            Resets the location of the label object to its default.
        """
        pass
    
    
    def ResetProperties(self):
        """
        ResetProperties()
            Resets the properties of the label object to its defaults.
        """
        pass
    
    
    def SetReferenceTextTarget(self):
        """
        SetReferenceTextTarget(referenceTextComponentId: ObjectId, referenceObjectId: ObjectId)
            Makes the reference text component refer to other civil object.
            referenceTextComponentId: ObjectId - The ObjectId of the reference text component.
            referenceObjectId: ObjectId - The ObjectId of a Civil Object which will be referenced by text component.
        """
        pass
    
    
    def SetTextComponentJustificationOverride(self):
        """
        SetTextComponentJustificationOverride(labelStyleComponentId: ObjectId, textJustificationType: Autodesk.Civil.TextJustificationType) -> TextJustificationType
            Overrides the justification on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textJustificationType: Autodesk.Civil.TextJustificationType - The type of text justification to set.
        """
        pass
    
    
    def SetTextComponentOverride(self):
        """
        SetTextComponentOverride(labelStyleComponentId: ObjectId, textOverride: System.String)
            Overrides the text on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textOverride: System.String - The override label text.
        SetTextComponentOverride(labelStyleComponentId: ObjectId, textOverride: System.String, textJustificationType: Autodesk.Civil.TextJustificationType) -> TextJustificationType
            Overrides the text and justification on the specified text component.
            labelStyleComponentId: ObjectId - The object id of the text component.
            textOverride: System.String - The override label text.
            textJustificationType: Autodesk.Civil.TextJustificationType - The type of text justification.
        """
        pass
    
    pass

class LabelSelectionProperties(object):
    """
    Not intended for external use.
    """

    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the LabelSelectionProperties
        """
        pass
    
    
    def Instance(self):
        """
        Instance(objIds: ObjectIdCollection) -> LabelSelectionProperties
            objIds: ObjectIdCollection
        """
        pass
    
    pass

class LabelType():
    """
    An enumeration that describes all possible label types that a base label object can be.
    """
    pass

class LegendTable(Entity):
    """
    A table that displays colors and range values for a surface analysis.
    """


    pass

class LinearTransitionDescription(TransitionDescriptionBase):
    """
    This class represents a straight, linear transition between two regions of an offset alignment.
    """
    TaperInput = None
    TaperRatio = None
    pass

class Link(object):
    """
    Roadway Link object. Connects roadway points in a subassembly.
    """
    Codes = None
    Index = None
    IsHidden = None
    Points = None
    pass

class LinkCollection(object):
    """
    A collection of Link objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(points: Autodesk.Civil.DatabaseServices.IPoint, code: System.String) -> Link
            Add a link using the default Normal display mode.
            points: Autodesk.Civil.DatabaseServices.IPoint - 
            Points of the link.
            code: System.String - 
            The code of the link.
        Add(points: Autodesk.Civil.DatabaseServices.IPoint, codes: System.String) -> Link
            Add a link using the default Normal display mode.
            points: Autodesk.Civil.DatabaseServices.IPoint - 
            Points of the link.
            codes: System.String - 
            The codes of the link.
        Add(point1: Autodesk.Civil.DatabaseServices.IPoint, point2: Autodesk.Civil.DatabaseServices.IPoint, code: System.String) -> Link
            Add a link. A link is defined by 2 points in most cases, using the default Normal display mode.
            point1: Autodesk.Civil.DatabaseServices.IPoint - 
            First point of the link.
            point2: Autodesk.Civil.DatabaseServices.IPoint - 
            Second point of the link.
            code: System.String - 
            The code of the link.
        Add(point1: Autodesk.Civil.DatabaseServices.IPoint, point2: Autodesk.Civil.DatabaseServices.IPoint, codes: System.String) -> Link
            Add a link. In most cases using the default Normal display mode., a link is defined by 2 points .
            point1: Autodesk.Civil.DatabaseServices.IPoint - 
            First point of the link.
            point2: Autodesk.Civil.DatabaseServices.IPoint - 
            Second point of the link.
            codes: System.String - 
            The codes of the link.
        Add(points: Autodesk.Civil.DatabaseServices.IPoint, code: System.String, displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay) -> Link
            Add a link.
            points: Autodesk.Civil.DatabaseServices.IPoint - 
            Points of the link.
            code: System.String - 
            The code of the link.
            displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay - 
            How to draw the link (solid, dashed, with/without arrowhead). 
        Add(points: Autodesk.Civil.DatabaseServices.IPoint, codes: System.String, displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay) -> Link
            Add a link.
            points: Autodesk.Civil.DatabaseServices.IPoint - 
            Points of the link.
            codes: System.String - 
            The codes of the link.
            displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay - 
            Specifies how to draw the link (solid, dashed, with/without arrowhead). 
        Add(point1: Autodesk.Civil.DatabaseServices.IPoint, point2: Autodesk.Civil.DatabaseServices.IPoint, code: System.String, displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay) -> Link
            Add a link. In most cases, a link is defined by 2 points.
            point1: Autodesk.Civil.DatabaseServices.IPoint - 
            First point of the link.
            point2: Autodesk.Civil.DatabaseServices.IPoint - 
            Second point of the link.
            code: System.String - 
            The code of the link.
            displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay - 
            How to draw the link (solid, dashed, with/without arrowhead). 
        Add(point1: Autodesk.Civil.DatabaseServices.IPoint, point2: Autodesk.Civil.DatabaseServices.IPoint, codes: System.String, displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay) -> Link
            Add a link. In most cases, a link is defined by 2 points.
            point1: Autodesk.Civil.DatabaseServices.IPoint - 
            First point of the link.
            point2: Autodesk.Civil.DatabaseServices.IPoint - 
            Second point of the link.
            codes: System.String - 
            The codes of the link.
            displayMode: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay - 
            How to draw the link (solid, dashed, with/without arrowhead). 
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> Link
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(index: System.Int32)
            Removes a link from the collection.
            index: System.Int32 - 
            Index of the link.
        Remove(link: Autodesk.Civil.DatabaseServices.Link) -> Link
            Removes a link from the collection.
            link: Autodesk.Civil.DatabaseServices.Link - 
            The Link need to be removed.
        """
        pass
    
    pass

class MassHaulLine(Entity):
    """
    A line that displays free haul and overhaul volumes in a mass haul view..
    """


    pass

class MassHaulView(Entity):
    """
    A mass haul diagram view.
    """
    MassHaulLineId = None

    pass

class MatchLine(Entity):
    """
    A match line is a straight line that indicate locations in a view frame group where one view frame intersects or matches up with another view frame.
    """
    AlignmentId = None
    GroupId = None
    IsLeftLabelVisible = None
    IsRightLabelVisible = None
    LeftLabelAnchorPosition = None
    LeftLabelStyleId = None
    Number = None
    RightLabelAnchorPosition = None
    RightLabelStyleId = None
    Station = None

    pass

class MatchLineLabelGroup(Entity):
    """
    This class represents a MatchLine label group.
    """
    Side = None
    def Create(self):
        """
        Create(viewFrameGroupId: ObjectId, side: Autodesk.Civil.EntitySideType) -> EntitySideType
            Creates a new instance of MatchLineLabelGroup on one side of the ViewFrameGroup with the default label style and anchor position.
            viewFrameGroupId: ObjectId - The ObjectId of the ViewFrameGroup where the label group is located.
            side: Autodesk.Civil.EntitySideType - An enum value indicating the side of the Matchline where the labelGroup is to be created.
        Create(viewFrameGroupId: ObjectId, side: Autodesk.Civil.EntitySideType, labelStyleId: ObjectId, anchorPosition: Autodesk.Civil.MatchLineLabelLocationType) -> EntitySideType
            Creates a new instance of MatchLineLabelGroup on one side of the ViewFrameGroup with the specified label style and anchor position.
            viewFrameGroupId: ObjectId - The ObjectId of the ViewFrameGroup where the label group is located.
            side: Autodesk.Civil.EntitySideType - An enum value indicating the side of the Matchlines where the labelGroup is to be created.
            labelStyleId: ObjectId - The ObjectId of MatchLineLabel style to use.
            anchorPosition: Autodesk.Civil.MatchLineLabelLocationType - The relative anchor position of MatchLineLabelGroup.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(viewFrameGroupId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all the MatchLineLabelGroup objects in the specified ViewFrameGroup.
            viewFrameGroupId: ObjectId - The ObjectId of the ViewFrameGroup where the labelGroups are located.
        """
        pass
    
    
    def GetLabelGroupIdBySide(self):
        """
        GetLabelGroupIdBySide(viewFrameGroupId: ObjectId, side: Autodesk.Civil.EntitySideType) -> EntitySideType
            Returns The ObjectId of the MatchLineLabelGroup on the specified side in ViewFrameGroup.
            viewFrameGroupId: ObjectId
            side: Autodesk.Civil.EntitySideType
        """
        pass
    
    pass

class MaterialConditionType():
    """
    An enumeration that specifies the material condition type.
    """
    pass

class MaterialFactorType():
    """
    This class defines the QTO material factor types.
    """
    pass

class MaterialItemType():
    """
    An enumeration that specifies the material item type.
    """
    pass

class MaterialQuantityType():
    """
    An enumeration that specifies the material quantity type.
    """
    pass

class MaterialSection(Entity):
    """
    The AeccDbMaterialSection wrapper.
    """
    StyleId = None
    StyleName = None

    pass

class MaterialSectionSource(object):
    """
    This defines a material section source in SampleLineGroup.
    """
    IsSampled = None
    Material = None
    SourceType = None
    StyleId = None
    UpdateMode = None
    def GetMaterialSectionIds(self):
        """
        GetMaterialSectionIds() -> ObjectIdCollection
            Gets the objectId collection of MaterialSection on the section source.
        """
        pass
    
    pass

class MaterialSectionSourceCollection(object):
    """
    The collection of MaterialSectionSource in SampleLineGroup.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> MaterialSectionSource
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    pass

class MaterialVolumeCalculationMethodType():
    """
    
    """
    pass

class MultipleProfileViewsCreationOptions(object):
    """
    This class encapsulates the options for creating multiple ProfileViews.
    """
    DrawOrder = None
    GapBetweenViewsInColumn = None
    GapBetweenViewsInRow = None
    LengthOfEachView = None
    MaxViewInRowOrColumn = None
    StartCorner = None
    pass

class Network(Entity):
    """
    The container object used to associate pipes and structures that are part of the same pipe run or pipe network.
    """
    PartsListId = None
    PartsListName = None
    PipeNameTemplate = None
    PipeNetworkSectionLayerId = None
    PipeNetworkSectionLayerName = None
    PipePlanLabelStyleId = None
    PipePlanLabelStyleName = None
    PipePlanLayerId = None
    PipePlanLayerName = None
    PipeProfileLabelStyleId = None
    PipeProfileLabelStyleName = None
    PipeProfileLayerId = None
    PipeProfileLayerName = None
    ReferenceAlignmentId = None
    ReferenceAlignmentName = None
    ReferenceSurfaceId = None
    ReferenceSurfaceName = None
    StructureNameTemplate = None
    StructurePlanLabelStyleId = None
    StructurePlanLabelStyleName = None
    StructurePlanLayerId = None
    StructurePlanLayerName = None
    StructureProfileLabelStyleId = None
    StructureProfileLabelStyleName = None
    StructureProfileLayerId = None
    StructureProfileLayerName = None
    def AddCurvePipe(self):
        """
        AddCurvePipe(pipeFamilyId: ObjectId, pipeSizeId: ObjectId, curve: Curve3d, clockwise: System.Boolean, newPipeId: ObjectId, applyRules: System.Boolean)
            Add a curve pipe by using the geometry information of an input curve.
            pipeFamilyId: ObjectId - Pipe family id.
            pipeSizeId: ObjectId - Object id of the Pipe Size.
            curve: Curve3d - The curve which supplies the geometry information.
            clockwise: System.Boolean - Returns true if the new pipe has clockwise direction, false otherwise.
            newPipeId: ObjectId - Returns the object id of the newly added pipe.
            applyRules: System.Boolean - Returns whether the method needed to apply rules.
        """
        pass
    
    
    def AddLinePipe(self):
        """
        AddLinePipe(pipeFamilyId: ObjectId, pipeSizeId: ObjectId, line: LineSegment3d, newPipeId: ObjectId, applyRules: System.Boolean)
            Add a line pipe by using the geometry information of an input line.
            pipeFamilyId: ObjectId - Pipe family id.
            pipeSizeId: ObjectId - Object id of the Pipe Size.
            line: LineSegment3d - The line which supplies the geometry information.
            newPipeId: ObjectId - Returns the object id of the added new pipe.
            applyRules: System.Boolean - Returns whether the method needed to apply rules.
        """
        pass
    
    
    def AddStructure(self):
        """
        AddStructure(structureId: ObjectId)
            Add an existing structure into the network.
            structureId: ObjectId - The Object Id for the structure to add.
        AddStructure(structureFamilyId: ObjectId, structureSizeId: ObjectId, location: Point3d, rotation: System.Double, newStructureId: ObjectId, applyRules: System.Boolean)
            Create and add a new structure into the network.
            structureFamilyId: ObjectId - Structure family id.
            structureSizeId: ObjectId - Object id for the Structure Size.
            location: Point3d - The location of the newly added structure.
            rotation: System.Double - The rotation of new added structure.
            newStructureId: ObjectId - Returns the object id of the newly added structure.
            applyRules: System.Boolean - Returns whether the method needed to apply rules.
        """
        pass
    
    
    def BreakPipe(self):
        """
        BreakPipe(pipeIdToBreak: ObjectId, breakPoint: Point3d, existingStructureId: ObjectId, newPipeId: ObjectId)
            Break the specified pipe with a specified existing structure at a point.
            pipeIdToBreak: ObjectId - The pipe to break.
            breakPoint: Point3d - Break point on pipe.
            existingStructureId: ObjectId - The existing Structure to place at the break point.
            newPipeId: ObjectId - Returns the object id of the newly added pipe created by the break.
        """
        pass
    
    
    def Create(self):
        """
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, networkName: System.String) -> CivilDocument
            Creates a pipe network specified by name.
            Remarks: If the name (such as "abc") is a duplicate of an existing network, the name is changed to "abc (n)". 
            The value of n is an integer that increments until the name "abc (n)" is unique.
            document: Autodesk.Civil.ApplicationServices.CivilDocument - CivilDocument object in which the network is created. 
            networkName: System.String - The name of the new pipe network. If the name is duplicated, it is 
            changed to a new name (see remarks below).
        """
        pass
    
    
    def FindShortestNetworkPath(self):
        """
        FindShortestNetworkPath(startPartId: ObjectId, endPartId: ObjectId, minLength: System.Double) -> ObjectIdCollection
            Find a shortest path in the network.
            startPartId: ObjectId - Starting part for the path.
            endPartId: ObjectId - Ending part for the path.
            minLength: System.Double - Returns the length of the shortest path.
        """
        pass
    
    
    def GetPipeIds(self):
        """
        GetPipeIds() -> ObjectIdCollection
            Gets the objectId collection of all pipes belonging to this pipe network.
        """
        pass
    
    
    def GetSpanningPipePlanLabelIds(self):
        """
        GetSpanningPipePlanLabelIds() -> ObjectIdCollection
            Gets the spanning pipe plan label collection.
        """
        pass
    
    
    def GetSpanningPipeProfileLabelIds(self):
        """
        GetSpanningPipeProfileLabelIds() -> ObjectIdCollection
            Get the spanning pipe profile label collection.
        """
        pass
    
    
    def GetStructureIds(self):
        """
        GetStructureIds() -> ObjectIdCollection
            Gets the objectId collection of all structures belonging to this pipe network.
        """
        pass
    
    
    def MoveParts(self):
        """
        MoveParts(partIds: ObjectIdCollection, dstNetworkId: ObjectId)
            Moves the specified parts of the network into another network.
            Remarks: No exception is thrown if the source and destination are the same.
            partIds: ObjectIdCollection - Object ids of the Parts to be moved.
            dstNetworkId: ObjectId - Object id of the destination network.
        """
        pass
    
    pass

class NetworkCatalogDef(object):
    """
    The NetworkCatalogDef class.
    This class allows you to use a part catalog definition at runtime.
    """
    def DeclareNewParameter(self):
        """
        DeclareNewParameter(globalContext: System.String, displayContext: System.String, paramName: System.String, paramDesc: System.String, dataType: Autodesk.Civil.DatabaseServices.PartCatalogDataType, usage: Autodesk.Civil.DatabaseServices.PartParamUsageType, defaultUnits: System.String, singleton: System.Boolean, catManagedList: System.Boolean) -> PartCatalogDataType
            Declares a new part catalog parameter
            globalContext: System.String - Specifies the parameter's global context, which should be already declared.
            displayContext: System.String - Specifies the display string of the parameter's context.
            paramName: System.String - Specifies the parameter's name.
            paramDesc: System.String - Specifies a description for the parameter.
            dataType: Autodesk.Civil.DatabaseServices.PartCatalogDataType - Specifies the parameter's value data type.
            usage: Autodesk.Civil.DatabaseServices.PartParamUsageType - Specifies the parameter's usage.
            defaultUnits: System.String - Specifies the parameter's default units.
            singleton: System.Boolean - Specifies if the parameter is a singleton.
            catManagedList: System.Boolean - Specifies if the parameter belongs to a managed list.
        """
        pass
    
    
    def DeclarePartProperty(self):
        """
        DeclarePartProperty(globalContext: System.String, domain: Autodesk.Civil.DatabaseServices.DomainType, partType: Autodesk.Civil.DatabaseServices.PartType) -> DomainType
            Declares a new part property.
            globalContext: System.String - Specifies the parameter's global context, which should already exist.
            domain: Autodesk.Civil.DatabaseServices.DomainType - Specifies the part's domain.
            partType: Autodesk.Civil.DatabaseServices.PartType - Specifies the part's type.
        """
        pass
    
    pass

class NetworkRule(DBObject):
    """
    Holds parameter collections for pipe and structure rules.
    """
    ParamsDouble = None
    ParamsLong = None
    pass

class NoteLabel(Entity):
    """
    This class represents a note label.
    """

    def Create(self):
        """
        Create(database: Database, location: Point3d) -> ObjectId
            Creates a new instance of a NoteLabel in the specified database.
            database: Database - The database in which to insert the NoteLabel.
            location: Point3d - The location at which to insert the NoteLabel in the drawing.
        Create(location: Point3d, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId
            Creates a new instance of a NoteLabel with the specified label style and marker display style.
            location: Point3d - The location in the drawing for the NoteLabel.
            labelStyleId: ObjectId - The ObjectId of the style to apply to the NoteLabel (object type LabelStyle).
            markerStyleId: ObjectId - The ObjectId of the marker display style for the NoteLabel maker (object type MarkerStyle).
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(database: Database) -> ObjectIdCollection
            Gets an ObjectIdCollection of all NoteLabels in a database.
            database: Database - The database where to get the ObjectIdCollection.
        """
        pass
    
    pass

class OffsetAlignmentInfo(object):
    """
    This class encapsulates the properties and operations of an offset alignment object.
    """
    LockMode = None
    LockToEndStation = None
    LockToStartStation = None
    NominalOffset = None
    ParentAlignmentId = None
    Regions = None
    Side = None
    Transitions = None
    UpdateMode = None
    def AddAutoWidenings(self):
        """
        AddAutoWidenings(wideningCriteria: Autodesk.Civil.DatabaseServices.AutoWideningCriteriaInfo, curveGroups: Autodesk.Civil.DatabaseServices.AlignmentSubEntityArc) -> AutoWideningCriteriaInfo
            Adds automatic widenings using criteria on the specified specified curve groups of parent Alignment.
            wideningCriteria: Autodesk.Civil.DatabaseServices.AutoWideningCriteriaInfo - The automatic widening criteria.
            curveGroups: Autodesk.Civil.DatabaseServices.AlignmentSubEntityArc - The curve groups on the prarent alignment where the automatic widenings need to add.
        AddAutoWidenings(wideningCriteria: Autodesk.Civil.DatabaseServices.AutoWideningCriteriaInfo, location: Autodesk.Civil.SweptCurveLocation) -> AutoWideningCriteriaInfo
            Adds automatic widenings using criteria on the specified specified location of Offset Alignment.
            wideningCriteria: Autodesk.Civil.DatabaseServices.AutoWideningCriteriaInfo - The automatic widening criteria.
            location: Autodesk.Civil.SweptCurveLocation - The location where the automatic widenings need to add.
        AddAutoWidenings(wideningInfo: Autodesk.Civil.DatabaseServices.AutoWideningInfo, curveGroups: Autodesk.Civil.DatabaseServices.AlignmentSubEntityArc) -> AutoWideningInfo
            Adds automatic widenings using manual windening properties on the specified curve groups of the parent Alignment.
            wideningInfo: Autodesk.Civil.DatabaseServices.AutoWideningInfo - The automatic widening properties.
            curveGroups: Autodesk.Civil.DatabaseServices.AlignmentSubEntityArc - The curve groups on the prarent alignment where the automatic widenings need to add.
        AddAutoWidenings(wideningInfo: Autodesk.Civil.DatabaseServices.AutoWideningInfo, location: Autodesk.Civil.SweptCurveLocation) -> AutoWideningInfo
            Adds automatic widenings using manual windening properties on the specified location of the Offset Alignment.
            wideningInfo: Autodesk.Civil.DatabaseServices.AutoWideningInfo - The automatic widening properties.
            location: Autodesk.Civil.SweptCurveLocation - The location where the automatic widenings need to add.
        """
        pass
    
    
    def AddWidening(self):
        """
        AddWidening(startStation: System.Double, endStation: System.Double, offsetDistance: System.Double)
            Adds a widening with two 0-length linear transitions to the Offset Alignment.
            Remarks: This method will create a specific region from startStation to endStation with slim entry transition and exit transition.
            startStation: System.Double - The start station of the widening.
            endStation: System.Double - The end station of the widening.
            offsetDistance: System.Double - The offset distance value from the parent alignment.
        """
        pass
    
    pass

class OffsetAlignmentWideningCriteria(object):
    """
    This class encapsulates the properties of an offset alignment wideninig criteria.
    """
    AttainmentMethod = None
    LaneWidth = None
    LeftLanesCount = None
    MinimumRadiusTableName = None
    RightLanesCount = None
    SpiralPercentForSC = None
    TangentPercentForTC = None
    TransitionLengthTableName = None
    WheelbaseLength = None
    WideningMethod = None
    WideningSide = None
    pass

class OffsetAssembly(object):
    """
    Specify a controlling offset within an assembly.
    """
    AssemblyId = None
    Groups = None
    Name = None
    Offset = None
    def AddSubassembly(self):
        """
        AddSubassembly(subassemblyId: ObjectId) -> AssemblyGroup
            Adds a subassembly to the offset assembly.
            subassemblyId: ObjectId - The ObjectId of the source subassembly to be added.
        AddSubassembly(subassemblyId: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Adds a subassembly to the offset assembly and hooks to the specified point of a subassembly.
            subassemblyId: ObjectId - The ObjectId of the source subassembly to be added.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def CopySubassembly(self):
        """
        CopySubassembly(subassemblyIdFrom: ObjectId) -> AssemblyGroup
            Copies a subassembly to the offset assembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source subassembly to be copied.
        CopySubassembly(subassemblyIdFrom: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Copies a subassembly to the offset assembly and hooks to the specified point of a subassembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source subassembly to be copied.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the OffsetAssembly
        """
        pass
    
    
    def InsertSubassemblyAfter(self):
        """
        InsertSubassemblyAfter(subassemblyId: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Inserts an unassigned subassembly after a subassembly in the offset assembly and hooks to the specified point.
            Remarks: This method also can be used to insert a subassembly after the subassembly to which no subassembly is hooked.
            subassemblyId: ObjectId - The ObjectId of the source subassembly to be added.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def InsertSubassemblyBefore(self):
        """
        InsertSubassemblyBefore(subassemblyId: ObjectId, targetSubassemblyId: ObjectId)
            Inserts an unassigned subassembly before a subassembly in the offset assembly.
            subassemblyId: ObjectId - The ObjectId of the subassembly to be inserted before the target subassembly.
            targetSubassemblyId: ObjectId - The ObjectId of the subassembly before which a new subassembly is inserted.
        """
        pass
    
    
    def MirrorSubassembly(self):
        """
        MirrorSubassembly(subassemblyIdFrom: ObjectId) -> AssemblyGroup
            Mirrors a subassembly to the offset assembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source subassembly to be mirrored.
        MirrorSubassembly(subassemblyIdFrom: ObjectId, pointHookTo: Autodesk.Civil.DatabaseServices.Point) -> Point
            Mirrors a subassembly to the offset assembly and hooks to the specified point of a subassembly.
            subassemblyIdFrom: ObjectId - The ObjectId of the source subassembly to be mirrored.
            pointHookTo: Autodesk.Civil.DatabaseServices.Point - The point to be hooked to.
        """
        pass
    
    
    def ReplaceSubassembly(self):
        """
        ReplaceSubassembly(subassemblyId: ObjectId, targetSubassemblyId: ObjectId)
            Replaces a subassembly in the assembly with another unassigned subassembly.
            subassemblyId: ObjectId - The ObjectId of the subassembly to be added to replace the target subassembly.
            targetSubassemblyId: ObjectId - The ObjectId of the subassembly to be replaced in the assembly.
        """
        pass
    
    pass

class OffsetAssemblyCollection(object):
    """
    A collection of OffsetAssembly objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(offsetAssemblyName: System.String, offset: Vector2d) -> OffsetAssembly
            Adds an OffsetAssembly with the specified name and offset.
            offsetAssemblyName: System.String - Specifies the name of OffsetAssembly.
            offset: Vector2d - Specifies the offset from main Assembly.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> OffsetAssembly
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(offsetAssemblyName: System.String) -> bool
            Removes the OffsetAssembly with the given name.
            offsetAssemblyName: System.String - Specifies the name of OffsetAssembly.
        Remove(offsetAssembly: Autodesk.Civil.DatabaseServices.OffsetAssembly) -> OffsetAssembly
            Removes the given OffsetAssembly.
            offsetAssembly: Autodesk.Civil.DatabaseServices.OffsetAssembly - The removed OffsetAssembly object.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes an OffsetAssembly by index.
            index: System.Int32 - Index of the removed OffsetAssembly.
        """
        pass
    
    pass

class OffsetBaseline(BaseBaseline):
    """
    TODO: FINAL REVIEW WAITINGTODO: NEEDS SAMPLE
    An offset baseline represents a secondary baseline following the main baseline at an offset.
    """
    AlignmentId = None
    BaselineType = None
    EndStation = None
    EndStationOnMainBaseline = None
    Name = None
    ProfileId = None
    RelatedOffsetBaselineFeatureLines = None
    StartStation = None
    StartStationOnMainBaseline = None
    def GetOffsetElevationFromMainBaselineStation(self):
        """
        GetOffsetElevationFromMainBaselineStation(mainBaselineStation: System.Double) -> Point2d
            TODO: FINAL REVIEW WAITINGTODO: NEEDS SAMPLE
            Returns the offset and elevation at the specified station.
            Remarks: This method returns the offset and elevation at a specified station on the main baseline. When 
            BaselineType is HardcodedOffsetBaseline, the method will ignore the 
            mainBaselineStation parameter and return the offset between OffsetBaseline and mainBaseline defined in assembly.
            mainBaselineStation: System.Double - Main baseline station to retrieve the offset and elevation.
        """
        pass
    
    
    def IsFeatureLineBased(self):
        """
        IsFeatureLineBased() -> bool
            Indicates whether the specific baseline of corridor is feature line based or not.
            Remarks: If this offset baseline is feature line based, then it will return true.
        """
        pass
    
    
    def MainBaselineStationToOffsetBaselineStation(self):
        """
        MainBaselineStationToOffsetBaselineStation(mainBaselineStation: System.Double) -> double
            TODO: FINAL REVIEW WAITINGTODO: NEEDS SAMPLE
            Returns the offset baseline station value from the specified main baseline station.
            Remarks: This method takes a station value on the main baseline and returns the offset baseline station value.
            mainBaselineStation: System.Double - Main baseline station value to convert.
        """
        pass
    
    
    def OffsetBaselineStationToMainBaselineStation(self):
        """
        OffsetBaselineStationToMainBaselineStation(offsetBaselineStation: System.Double) -> double
            TODO: FINAL REVIEW WAITINGTODO: NEEDS SAMPLE
            Returns the main baseline station value from the specified offset baseline station.
            Remarks: This method takes a station value on the offset baseline and returns the main baseline station value.
            offsetBaselineStation: System.Double - Offset baseline station value to convert.
        """
        pass
    
    
    def SortedStations(self):
        """
        SortedStations() -> double[]
            Gets the sorted stations for the baseline.Note: This method doesn't work for
            DREF corridor, in this case, you should first get the applies asemblies and then call Stations() 
            to achieve the similar result.
        """
        pass
    
    pass

class OffsetBaselineCollection(object):
    """
    Exposed by the Corridor object, it contains the
    collection of OffsetBaseline objects for the corridor.
    """
    CorridorId = None
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> OffsetBaseline
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def OffsetBaselineNames(self):
        """
        OffsetBaselineNames() -> string[]
            Gets an array of OffsetBaseline names.
        """
        pass
    
    pass

class OffsetLengthOption():
    """
    Specifies how the length of the offset alignment is determined. 
    When Select To Intersection Extents is selected, offset alignments are extended to the length of the extent of the intersection object. 
    When Alignment Start To End is selected, offset alignments are created the length of the parent alignment.
    """
    pass

class OverhangCorrectionType():
    """
    Specifies the way an overhang to be corrected when rendered.
    """
    pass

class OverriddenStationInfo():
    """
    This struct is used to represent corridor overridden station information
    """
    pass

class Parcel(Entity):
    """
    An object that represents real estate parcels, such as lots in a subdivision, and other features that have closed 
    boundaries (such as bodies of water and soil regions).
    """
    AreaLocation = None
    AreaSelectionLabelLocation = None
    AreaSelectionLabelStyleId = None
    Centroid = None
    IsAreaSelectionLabelPinned = None
    Number = None
    def GetAvailableParcelAreaLabelIds(self):
        """
        GetAvailableParcelAreaLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the ParcelAreaLabels in a Parcel.
            Remarks: The returned ObjectIdCollection does not contain the parcel area selection label, which is an embedded object used to select a Parcel.
        """
        pass
    
    
    def ResetAreaSelectionLabel(self):
        """
        ResetAreaSelectionLabel()
            Resets the parcel area selection label to its defaults.
        """
        pass
    
    pass

class ParcelAreaLabel(Entity):
    """
    This class represents a Parcel area label.
    """

    def Create(self):
        """
        Create(parcelId: ObjectId) -> ObjectId
            Creates a new instance of ParcelAreaLabel on the specified Parcel with the default label style.
            parcelId: ObjectId - The ObjectId of the Parcel in which the label is located.
        Create(parcelId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a ParcelAreaLabel on the specified Parcel with the specified label style.
            parcelId: ObjectId - The ObjectId of the Parcel in which the label is located.
            labelStyleId: ObjectId - The ObjectId of ParcelArea style (object type LabelStyle).
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(parcelId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of all ParcelAreaLabels for the specified Parcel.
            Remarks: The returned ObjectIdCollection does not contain the parcel area selection label, as this is an embedded object used to select a Parcel.
            parcelId: ObjectId - The ObjectId of a Parcel to get the ParcelAreaLabels for.
        """
        pass
    
    pass

class ParcelSegment(Entity):
    """
    A parcel segment is a line segment, arc, or AutoCAD entity within a site. When parcel segments form a closed region, that region becomes a Parcel.
    """


    pass

class ParcelSegmentTable(Entity):
    """
    A Table associated with a ParcelSegment.
    """


    pass

class ParcelTable(Entity):
    """
    A table associated with a Parcel.
    """


    pass

class Part(Entity):
    """
    A pipe network part, base class for Pipe and Structure classes.
    """
    ConnectedPartCount = None
    Domain = None
    Material = None
    Name = None
    NetworkId = None
    NetworkName = None
    OverrideRuleSet = None
    ParamsBool = None
    ParamsDouble = None
    ParamsLong = None
    ParamsString = None
    PartData = None
    PartDefId = None
    PartDescription = None
    PartSizeName = None
    PartSubType = None
    PartType = None
    Position = None
    ProfileViewPartId = None
    RefAlignmentId = None
    RefAlignmentName = None
    RefSurfaceId = None
    RefSurfaceName = None
    RuleSetStyleId = None
    RuleSetStyleName = None
    SectionViewPartId = None
    Solid3dBody = None
    SurfaceId = None
    WallThickness = None
    def AddToProfileView(self):
        """
        AddToProfileView(profileViewId: ObjectId)
            Draws the part into the specified profile view.
            profileViewId: ObjectId - The ObjectId of the target profile view.
        """
        pass
    
    
    def AddToSectionView(self):
        """
        AddToSectionView(sectionViewId: ObjectId)
            Draws the part into the specified section view.
            sectionViewId: ObjectId - The ObjectId of the target section view.
        """
        pass
    
    
    def ApplyRules(self):
        """
        ApplyRules() -> bool
        """
        pass
    
    
    def GetOverriddenRuleIds(self):
        """
        GetOverriddenRuleIds() -> ObjectIdCollection
            Gets the overridden Rule ids which this part contains.
        """
        pass
    
    
    def GetProfileViewsDisplayingMe(self):
        """
        GetProfileViewsDisplayingMe() -> ObjectIdCollection
            Gets the object id collection of all the profile views in which this part was drawn.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.ProfileView
        """
        pass
    
    
    def GetSectionViewsDisplayingMe(self):
        """
        GetSectionViewsDisplayingMe() -> ObjectIdCollection
            Gets the object id collection of all the section views in which this part was drawn.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.SectionView
        """
        pass
    
    
    def RemoveFromAllProfileViews(self):
        """
        RemoveFromAllProfileViews()
            Remove the part from all the profile views in which it is drawn.
        """
        pass
    
    
    def RemoveFromAllSectionViews(self):
        """
        RemoveFromAllSectionViews()
            Removes the part from all the section views in which it is drawn.
        """
        pass
    
    
    def RemoveFromProfileView(self):
        """
        RemoveFromProfileView(profileViewId: ObjectId)
            Remove the part from the specified profile view in which it is drawn.
            profileViewId: ObjectId - The ObjectId of the target profile view.
        """
        pass
    
    
    def RemoveFromSectionView(self):
        """
        RemoveFromSectionView(sectionViewId: ObjectId)
            Removes the part from the specified section view in which it is drawn.
            sectionViewId: ObjectId - The ObjectId of the target section view.
        """
        pass
    
    
    def SwapPartFamilyAndSize(self):
        """
        SwapPartFamilyAndSize(partFamilyId: ObjectId, partSizeId: ObjectId)
            Swaps the part family and size.
            partFamilyId: ObjectId
            partSizeId: ObjectId
        """
        pass
    
    pass

class PartCatalogDataType():
    """
    Specifies the data type of the reserved data.
    """
    pass

class PartContextType():
    """
    Specifies the context type, which corresponds to every property of a Part.
    """
    pass

class PartDataField(SizeFilterField):
    """
    An extensible field of part data.
    """
    Context = None
    ContextString = None
    DataType = None
    Description = None
    Index = None
    IsFromList = None
    IsFromRange = None
    IsReadOnly = None
    Name = None
    Units = None
    Value = None
    ValueList = None
    ValueRange = None
    pass

class PartDataList(object):
    """
    The part data list associated with a PartDataField or SizeFilterField.
    """
    Context = None
    Count = None
    DataType = None
    Index = None
    Item = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the PartDataList
        """
        pass
    
    
    def IsValidValue(self):
        """
        IsValidValue(value: System.Object) -> bool
            Gets if the specified value is in the list
            value: System.Object
        """
        pass
    
    pass

class PartDataRange(object):
    """
    Defines the range of valid data for a PartDataField.
    """
    Context = None
    DataType = None
    Index = None
    RangeDefault = None
    RangeMax = None
    RangeMin = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the PartDataRange
        """
        pass
    
    
    def IsValidValue(self):
        """
        IsValidValue(value: System.Object) -> bool
            Gets if the specified value is in the range.
            value: System.Object
        """
        pass
    
    pass

class PartDataRecord(object):
    """
    A single data record for a Part object.
    """
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the PartDataRecord
        """
        pass
    
    
    def GetAllDataFields(self):
        """
        GetAllDataFields() -> PartDataField
            Gets all data fields.
        """
        pass
    
    
    def GetDataFieldBy(self):
        """
        GetDataFieldBy(name: System.String) -> PartDataField
            Gets the object of DataField by Name.
            name: System.String - The name of the DataField to get.
        GetDataFieldBy(context: Autodesk.Civil.DatabaseServices.PartContextType) -> PartDataField
            Gets the object of DataField by Context.
            context: Autodesk.Civil.DatabaseServices.PartContextType - The part context type to get.
        GetDataFieldBy(context: Autodesk.Civil.DatabaseServices.PartContextType, index: System.Int32) -> PartDataField
            Gets the object of DataField by Context and index.
            context: Autodesk.Civil.DatabaseServices.PartContextType - The part context type to get.
            index: System.Int32 - The index of the PartDataField to get.
        """
        pass
    
    
    def GetMaxIndex(self):
        """
        GetMaxIndex(context: Autodesk.Civil.DatabaseServices.PartContextType) -> PartContextType
            Gets the maximum index of one context type.
            context: Autodesk.Civil.DatabaseServices.PartContextType - The part context type to check.
        """
        pass
    
    
    def GetSupportedContexts(self):
        """
        GetSupportedContexts() -> PartContextType
            Gets the collection of supported ContextType.
        """
        pass
    
    pass

class PartDef(object):
    """
    A part definition for Pipe or Structure objects.
    """
    def Get3dBody(self):
        """
        Get3dBody() -> Solid3d
            Gets the 3d solid body.
        """
        pass
    
    
    def GetBoundingShapeBody(self):
        """
        GetBoundingShapeBody() -> Solid3d
            Gets the bounding shape body.
        """
        pass
    
    
    def GetNetworkPartViewDef(self):
        """
        GetNetworkPartViewDef() -> PartViewDef
            Gets the network part view def.
        """
        pass
    
    
    def GetProfileInFrontView(self):
        """
        GetProfileInFrontView() -> Profile
            Gets the profile in front view.
        """
        pass
    
    pass

class PartParamUsageType():
    """
    Defines the usage of a part catalog parameter.
    """
    pass

class PartProfileLabel(Entity):
    """
    This class represents a label on a part in a profile.
    """
    ReferenceAlignmentId = None

    pass

class PartSectionLabel(Entity):
    """
    This class represents a PartSectionLabel.
    """
    ReferenceAlignmentId = None

    pass

class PartType():
    """
    Specifies a Part type.
    """
    pass

class PartViewDef(object):
    """
    Contains information about how a part is displayed.
    """
    BoundingBodyBlockId = None
    BoundingBodyBlockName = None
    PartBodyGraphicsBlockId = None
    PartBodyGraphicsBlockName = None
    pass

class PayItemFileFormat():
    """
    Defines pay item file format
    """
    pass

class Pipe(Entity):
    """
    A pipe network part serving to move fluids from one point to another.
    """
    Bearing = None
    CoverOfEndpoint = None
    CoverOfStartPoint = None
    CrossSectionalShape = None
    Curve2d = None
    EndOffset = None
    EndPoint = None
    EndStation = None
    EndStructureId = None
    EnergyGradeLineDown = None
    EnergyGradeLineUp = None
    FlowDirection = None
    FlowDirectionMethod = None
    FlowRate = None
    HoldOnResizeType = None
    HydraulicGradeLineDown = None
    HydraulicGradeLineUp = None
    InnerDiameterOrWidth = None
    InnerHeight = None
    JunctionLoss = None
    Length2D = None
    Length2DCenterToCenter = None
    Length2DToInsideEdge = None
    Length3D = None
    Length3DCenterToCenter = None
    Length3DToInsideEdge = None
    MaximumCover = None
    MinimumCover = None
    OuterDiameterOrWidth = None
    OuterHeight = None
    Radius = None
    ReturnPeriod = None
    Slope = None
    StartOffset = None
    StartPoint = None
    StartStation = None
    StartStructureId = None
    StyleId = None
    SubEntityType = None
    def AdjustEndpoint(self):
        """
        AdjustEndpoint(endpointToAdjust: Autodesk.Civil.DatabaseServices.ConnectorPositionType, targetLocation: Autodesk.Civil.DatabaseServices.PipeEndLocation, dOffset: System.Double) -> ConnectorPositionType
            Adjusts the location where the pipe endpoint connects within the connected structure. You can adjust the 
            the pipe to connect to the structure's center, inner wall or outer wall.  You can also specify a positive offset.
            endpointToAdjust: Autodesk.Civil.DatabaseServices.ConnectorPositionType - Specifies which pipe endpoint you want to adjust.
            targetLocation: Autodesk.Civil.DatabaseServices.PipeEndLocation - Specifies the target location within the structure: 0 = Center, 1 = Inner wall, 2 = Outer wall.
            dOffset: System.Double - Specifies the distance from the target location to the adjusted endpoint along the pipe's centerline.
        """
        pass
    
    
    def ConnectToPipe(self):
        """
        ConnectToPipe(sourceType: Autodesk.Civil.DatabaseServices.ConnectorPositionType, destinationPipeId: ObjectId, destinationType: Autodesk.Civil.DatabaseServices.ConnectorPositionType, structureFamilyId: ObjectId, structureSizeId: ObjectId, newStructureId: ObjectId, applyRules: System.Boolean, force: System.Boolean) -> ConnectorPositionType
            Connect one pipe to another pipe. If needed, disconnect the original one and move the pipe to that pipe for connecting and add a structure.
            sourceType: Autodesk.Civil.DatabaseServices.ConnectorPositionType - If start or end point to connect of source pipe.
            destinationPipeId: ObjectId - The destination pipe for connection.
            destinationType: Autodesk.Civil.DatabaseServices.ConnectorPositionType - If start or end point to connect of destination pipe.
            structureFamilyId: ObjectId - Family id of the needed structure.
            structureSizeId: ObjectId - Object id of Structure Size.
            newStructureId: ObjectId - The new structure id.
            applyRules: System.Boolean - Whether needed to apply the rules.
            force: System.Boolean - Whether force the pipe to disconnect the original connected structure.
        """
        pass
    
    
    def ConnectToStructure(self):
        """
        ConnectToStructure(sourcePosition: Autodesk.Civil.DatabaseServices.ConnectorPositionType, destinationStructureId: ObjectId, force: System.Boolean) -> ConnectorPositionType
            Connect one pipe to another structure. If needed, disconnect the original one and move the pipe to that structure for connecting.
            sourcePosition: Autodesk.Civil.DatabaseServices.ConnectorPositionType - If start or end point to connect.
            destinationStructureId: ObjectId - The destination structure id.
            force: System.Boolean - If force the pipe to disconnect the original connected structure.
        """
        pass
    
    
    def Disconnect(self):
        """
        Disconnect(pos: Autodesk.Civil.DatabaseServices.ConnectorPositionType) -> ConnectorPositionType
            Disconnect pipe.
            pos: Autodesk.Civil.DatabaseServices.ConnectorPositionType - Which end of this pipe to disconnect.
        """
        pass
    
    
    def GetAvailablePipeLabelIds(self):
        """
        GetAvailablePipeLabelIds() -> ObjectIdCollection
            Gets an  ObjectIdCollection of available PipeLabels.
        """
        pass
    
    
    def GetAvailableSpanningPipeLabelIds(self):
        """
        GetAvailableSpanningPipeLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of SpanningPipeLabels.
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(sourcePoint: Point3d) -> Point3d
            Gets the closest point found to the given point on a pipe.
            sourcePoint: Point3d - A 3d point in the drawing.
        """
        pass
    
    
    def GetLabelIds(self):
        """
        GetLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of labels on the pipe.
        """
        pass
    
    
    def GetParamAtPoint(self):
        """
        GetParamAtPoint(point: Point3d) -> double
            Gets the scale on the pipe for the given point.
            point: Point3d - The point used to get the scale on the pipe.
        """
        pass
    
    
    def GetPipeLabelIds(self):
        """
        GetPipeLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of labels on the pipe.
            Remarks: The returned ObjectIdCollection including the ObjectIds of PipeLabel and SpanningPipeLabel.
        """
        pass
    
    
    def GetPointAtParam(self):
        """
        GetPointAtParam(paramInterval: System.Double) -> Point3d
            Gets a 3d point for the given parameter.
            paramInterval: System.Double - The scale of the returned point on the pipe.
        """
        pass
    
    
    def GetProject2dPointVertically(self):
        """
        GetProject2dPointVertically(sourcePoint: Point2d, projectPoint: Point3d) -> bool
            Returns true if get the Project2dPoint successfully, otherwise false.
            sourcePoint: Point2d - A 2D point.
            projectPoint: Point3d - Project 2d point.
        """
        pass
    
    
    def IsMaxCoverViolated(self):
        """
        IsMaxCoverViolated(maxCover: System.Double, pointsViolated: Point3d, differences: System.Double, params: System.Double) -> bool
            Returns true if the Maximum Cover is violated.
            maxCover: System.Double - Max cover.
            pointsViolated: Point3d - The points which are on pipe and their distances to surface are shorter than maxCover.
            differences: System.Double - The distances of pointsViolated to surface.
            params: System.Double - The scales of pointsViolated on the pipe.
        """
        pass
    
    
    def IsMinCoverViolated(self):
        """
        IsMinCoverViolated(minCover: System.Double, pointsViolated: Point3d, differences: System.Double, params: System.Double) -> bool
            Returns true if the Minimum Cover is violated.
            minCover: System.Double - Min cover.
            pointsViolated: Point3d - The points which are on pipe and their distances to surface are shorter than minCover.
            differences: System.Double - The distances of pointsViolated to surface.
            params: System.Double - The scales of pointsViolated on the pipe.
        """
        pass
    
    
    def ResizeByInnerDiameterOrWidth(self):
        """
        ResizeByInnerDiameterOrWidth(innerDiameterOrWidth: System.Double, useClosestSize: System.Boolean)
            Resize the pipe by inner diameter or width.
            innerDiameterOrWidth: System.Double - Inner diameter or width value, takes unit of the catalog 
            useClosestSize: System.Boolean - True if this pipe should be resized to the closed size in the part family. False otherwise.
        """
        pass
    
    
    def SetSlopeHoldEnd(self):
        """
        SetSlopeHoldEnd(endValue: System.Double)
            Sets the slope of the pipe away from the pipe’s end point.
            endValue: System.Double - The slope value.
        """
        pass
    
    
    def SetSlopeHoldStart(self):
        """
        SetSlopeHoldStart(startValue: System.Double)
            Sets the slope of the pipe away from the pipe’s start point.
            startValue: System.Double - The slope value.
        """
        pass
    
    pass

class PipeEndLocation():
    """
    Specifies the pipe endpoint insertion location in the connected structure
    """
    pass

class PipeLabel(Entity):
    """
    This class encapsulates a PipeLabel.
    """
    Ratio = None
    ReferenceAlignmentId = None
    def Create(self):
        """
        Create(pipeId: ObjectId, ratio: System.Double) -> ObjectId
            Creates a new instance of a PipeLabel on the specified Pipe using the default label style.
            Remarks: The ratio should be in the range [0, 1].
            pipeId: ObjectId - The ObjectId of Pipe on which the label is located.
            ratio: System.Double - The relative position of the label to the pipe.
        Create(pipeId: ObjectId, ratio: System.Double, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of PipeLabel on a specified Pipe with the specified label style.
            Remarks: The ratio should be in the range [0, 1].
            pipeId: ObjectId - The ObjectId of Pipe on which the label is located.
            ratio: System.Double - The relative position of the label to the pipe.
            labelStyleId: ObjectId - The ObjectId of a PipeLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(pipeId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of all PipeLabels for the specified Pipe.
            pipeId: ObjectId - The ObjectId of a Pipe.
        """
        pass
    
    pass

class PipeNetworkBandLabelGroup(Entity):
    """
    
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all PipeNetworkBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all PipeNetworkBandLabelGroup objects on the specified profile view.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of PipeNetworkBandLabelGroup.
        """
        pass
    
    pass

class PipeOverride(GraphOverride):
    """
    Object used to change the style or label set for a pipe.
    """
    Draw = None
    OverrideStyleId = None
    OverrideStyleName = None
    PipeId = None
    PipeName = None
    pass

class PipeOverrideCollection(GraphOverrideCollection):
    """
    The PipeOverrideCollection collection class represents the collection of all pipes listed in the ProfileView.
    """
    SplitAt = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> PipeOverride
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class PipeProfileLabel(Entity):
    """
    This class represents a PipeProfileLabel.
    """
    Ratio = None
    def Create(self):
        """
        Create(profileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectId
            Creates a new instance of a PipeProfileLabel on the middle of a ProfileViewPart with the default label style.
            profileViewPartId: ObjectId - The ObjectId of the ProfileViewPart on which the label is located.
            profileViewId: ObjectId - The ObjectId of the ProfileView in which the label is located.
        Create(profileViewPartId: ObjectId, profileViewId: ObjectId, ratio: System.Double, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a PipeProfileLabel on the specified ProfileViewPart with the specified label style.
            Remarks: The ratio should be in the range [0, 1].
            profileViewPartId: ObjectId - The ObjectId of a ProfileViewPart on which the label is located.
            profileViewId: ObjectId - The ObjectId of the ProfileView in which the label is located.
            ratio: System.Double - The relative position of the label to the ProfileViewPart.
            labelStyleId: ObjectId - The ObjectId of a PipeProfileLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the PipeProfileLabels on the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of a ProfileView.
        """
        pass
    
    pass

class PipeSectionLabel(Entity):
    """
    This class represents a PipeSectionLabel.
    """

    def Create(self):
        """
        Create(sectionViewId: ObjectId, pipeId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: System.Int32) -> ObjectId
            Creates a new instance of a PipeSectionLabel on a SectionPipeNetwork using the default label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView in which the label is located.
            pipeId: ObjectId - The ObjectId of a Pipe that is one of the sources of the SectionPipeNetwork.
            sectionPipeNetworkId: ObjectId - The ObjectId of a SectionPipeNetwork.
            partIndex: System.Int32 - The index of a part in the SectionPipeNetwork with the specified Pipe source.
        Create(sectionViewId: ObjectId, pipeId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: System.Int32, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a PipeSectionLabel on a SectionPipeNetwork with the specified label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView in which the label is located.
            pipeId: ObjectId - The ObjectId of the Pipe that is one of the sources of a SectionPipeNetwork.
            sectionPipeNetworkId: ObjectId - The ObjectId of a SectionPipeNetwork.
            partIndex: System.Int32 - The zero-based index of a part in the SectionPipeNetwork with the specified Pipe source.
            labelStyleId: ObjectId - The ObjectId of a PipeSectionLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the PipeSectionLabels in the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of a SectionView.
        """
        pass
    
    pass

class PipeSubEntityType():
    """
    Specifies the subentity type of a pipe.
    """
    pass

class Point(object):
    """
    Roadway Point object. Represents a single point within a subassembly.
    """
    Codes = None
    Elevation = None
    Index = None
    IsHidden = None
    IsLoopPoint = None
    Offset = None
    Station = None
    def GetXYZ(self):
        """
        GetXYZ(x: System.Double, y: System.Double, z: System.Double)
            Gets the XYZ world coordinates from the soe cordinates
            x: System.Double
            y: System.Double
            z: System.Double
        """
        pass
    
    pass

class PointCloud(object):
    """
    The PointCloud class. This class wraps AutoCAD's AcDbPointCloud entity.
    PointClouds are objects that can contain very large numbers of points.
    """
    pass

class PointCloudUtility(object):
    """
    
    """
    def GetCivilPointCloudName(self):
        """
        GetCivilPointCloudName(A_0: ObjectId) -> string
            Returns the name of the Civil Point Cloud.
            A_0: ObjectId
        """
        pass
    
    
    def IsCivilPointCloud(self):
        """
        IsCivilPointCloud(A_0: ObjectId) -> bool
            Returns true if the entity specified by ObjectId is a Civil Point Cloud.
            A_0: ObjectId
        """
        pass
    
    pass

class PointCollection(object):
    """
    A collection of Roadway Point objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(offset: System.Double, elevation: System.Double, code: System.String) -> Point
            Constructor
            offset: System.Double - 
            The offset of the point.
            elevation: System.Double - 
            The elevation of the point.
            code: System.String - 
            The code of the point.
        Add(offset: System.Double, elevation: System.Double, codes: System.String) -> Point
            Constructor
            offset: System.Double - 
            The offset of the point.
            elevation: System.Double - 
            The elevation of the point.
            codes: System.String - 
            The codes of the point.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> Point
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(index: System.Int32)
            Remove the point from collection.
            index: System.Int32 - 
            Index of the point.
        Remove(point: Autodesk.Civil.DatabaseServices.Point) -> Point
            Remove the point from collection.
            point: Autodesk.Civil.DatabaseServices.Point - 
            The point need to be removed.
        """
        pass
    
    pass

class PointDescriptionKey(object):
    """
    This class encapsulates a point description key.
    """
    ApplyDrawingScale = None
    ApplyFixedLabelRotation = None
    ApplyFixedMarkerRotation = None
    ApplyFixedScaleFactor = None
    ApplyLabelRotationParameter = None
    ApplyLabelStyleId = None
    ApplyLayerId = None
    ApplyMarkerRotationParameter = None
    ApplyScaleParameter = None
    ApplyScaleXY = None
    ApplyScaleZ = None
    ApplyStyleId = None
    Code = None
    FixedLabelRotation = None
    FixedMarkerRotation = None
    FixedScaleFactor = None
    Format = None
    LabelRotationParameter = None
    LabelStyleId = None
    LayerId = None
    MarkerRotationParameter = None
    RotationDirection = None
    ScaleParameter = None
    StyleId = None
    pass

class PointDescriptionKeySet(DBObject):
    """
    This class encapsulates a point description key set.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(codeName: System.String) -> ObjectId
            Adds a new PointDescriptionKey object to the PointDescriptionKeySet.
            codeName: System.String - Specifies the name of new PointDescriptionKey object.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all PointDescriptionKey objects from the PointDescriptionKeySet.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(objectId: ObjectId) -> bool
            Determines whether an element specified by ObjectId is in the collection.
            objectId: ObjectId - The ObjectId of the PointDescriptionKey to look for.
        Contains(name: System.String) -> bool
            Determines whether an element specified by name is in the collection.
            name: System.String - The name of the PointDescriptionKey to look for.
        """
        pass
    
    
    def GetPointDescriptionKeyIds(self):
        """
        GetPointDescriptionKeyIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of PointDescriptionKey objects in the drawing.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(keyId: ObjectId) -> bool
            Removes a PointDescriptionKey object from the PointDescriptionKeySet.
            keyId: ObjectId - The ObjectId of the PointDescriptionKey object to be removed.
        """
        pass
    
    pass

class PointDescriptionKeySetCollection(object):
    """
    This class encapsulates the collection of all PointDescriptionKeySet objects in a drawing.
    """
    Count = None
    Item = None
    SearchOrder = None
    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            Adds a new PointDescriptionKeySet object to the drawing.
            name: System.String - Specifies the name of new PointDescriptionKeySet object.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all PointDescriptionKeySet objects from the drawing.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(objectId: ObjectId) -> bool
            Indicates whether an element specified by ObjectId exists in the collection.
            objectId: ObjectId
        Contains(name: System.String) -> bool
            Indicates whether an element specified by name exists in the collection.
            name: System.String
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
    
    
    def GetPointDescriptionKeySets(self):
        """
        GetPointDescriptionKeySets(database: Database) -> PointDescriptionKeySetCollection
            Gets the PointDescriptionKeySetCollection object for a drawing.
            database: Database
        """
        pass
    
    
    def Remove(self):
        """
        Remove(objectId: ObjectId)
            Removes a PointDescriptionKeySet object specified by ObjectId from the drawing.
            objectId: ObjectId - Specifies the objectId of the PointDescriptionKeySet object to remove.
        Remove(name: System.String)
            Removes a PointDescriptionKeySet object specified by name from the drawing.
            name: System.String - Specifies the name of the PointDescriptionKeySet object to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a PointDescriptionKeySet object specified by index from the drawing.
            index: System.Int32 - Specifies the index of the PointDescriptionKeySet object to remove.
        """
        pass
    
    pass

class PointFileFormat(object):
    """
    This class encapsulates a point file format for the current drawing.  A drawing typically defines several point file formats, held in 
    its [!:PointFileFormatCollection].  A point file format is used by the AddPointFile() methods to import points into a drawing.
    """
    CommentTag = None
    Delimiter = None
    FileExtension = None
    FileFormatType = None
    Name = None
    def Equals(self):
        """
        Equals(obj: System.Object) -> bool
            obj: System.Object
        """
        pass
    
    pass

class PointFileFormatCollection(object):
    """
    This class encapsulates a collection of all the point file formats in the current drawing.
    A point file format is required to import points into a drawing.
    """
    Count = None
    Item = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the PointFileFormatCollection
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> PointFileFormat
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetPointFileFormats(self):
        """
        GetPointFileFormats(pDatabase: Database) -> PointFileFormatCollection
            Gets the collection of point file formats supported by the specified database.
            pDatabase: Database
        """
        pass
    
    pass

class PointGroup(DBObject):
    """
    This class encapsulates a point group in the current drawing.
    """
    AllPointsGroupName = None
    ElevationOverride = None
    IsElevationOverridden = None
    IsLocked = None
    IsOutOfDate = None
    IsPointLabelStyleOverridden = None
    IsPointStyleOverridden = None
    IsRawDescriptionOverridden = None
    Name = None
    PointLabelStyleId = None
    PointsCount = None
    PointStyleId = None
    RawDescription = None
    RawDescriptionOverride = None
    UDPClassificationApplyType = None
    UDPClassificationName = None
    def ApplyDescriptionKeys(self):
        """
        ApplyDescriptionKeys()
            Applies the DescriptionKeys to the points in the PointGroup.
        """
        pass
    
    
    def ContainsPoint(self):
        """
        ContainsPoint(pointNumber: System.UInt32) -> bool
            Gets whether the PointGroup contains a CogoPoint with the given point number.
            pointNumber: System.UInt32
        """
        pass
    
    
    def DeletePoints(self):
        """
        DeletePoints()
            Deletes all the points in the PointGroup.
        """
        pass
    
    
    def GetPendingChanges(self):
        """
        GetPendingChanges() -> PointGroupChangeInfo
            Gets all pending change information for the PointGroup.
            Remarks: Changes to a PointGroup are registered when points are added or removed from a drawing, and before PointGroup.Update() is called.
            However, changes are not registered if the PointGroup query is changed to include or exclude additional points. 
            Note that the AllPoints PointGroup does not register changes.
        """
        pass
    
    
    def GetPointNumbers(self):
        """
        GetPointNumbers() -> uint[]
            Gets an array that contains the point numbers for all COGO points in the PointGroup.
        """
        pass
    
    
    def GetQuery(self):
        """
        GetQuery() -> PointGroupQuery
            Returns the Point Group query object.
            Remarks: You can check the type of the returned object to see if it is a StandardPointGroupQuery or a CustomPointGroupQuery.
        """
        pass
    
    
    def LockPoints(self):
        """
        LockPoints()
            Locks all the points in the PointGroup.
        """
        pass
    
    
    def SetQuery(self):
        """
        SetQuery(query: Autodesk.Civil.DatabaseServices.PointGroupQuery) -> PointGroupQuery
            Sets the Point Group query object.
            Remarks: The method sets the query object in the point group, which defines
            the points contained within the group.
            query: Autodesk.Civil.DatabaseServices.PointGroupQuery
        """
        pass
    
    
    def UnlockPoints(self):
        """
        UnlockPoints()
            Unlocks all the points in the PointGroup.
        """
        pass
    
    
    def Update(self):
        """
        Update()
            Updates the pending changes on the PointGroup object. After the PointGroup is updated, the property IsOutOfDate is false.
        """
        pass
    
    
    def UseAllClassifications(self):
        """
        UseAllClassifications()
            Applies all the User-Defined Property classifications to the current point group.
        """
        pass
    
    
    def UseCustomClassification(self):
        """
        UseCustomClassification(name: System.String)
            Applies a custom User-Defined Property classification by name to the current point group.
            name: System.String - The name of the custom UDP to apply.
        UseCustomClassification(udpClassification: Autodesk.Civil.DatabaseServices.UDPClassification) -> UDPClassification
            Applies a custom User-Defined Property classification to the current point group.
            udpClassification: Autodesk.Civil.DatabaseServices.UDPClassification
        """
        pass
    
    
    def UseNoneClassification(self):
        """
        UseNoneClassification()
            Sets the User-Defined Property classification for the current point group to "none".
        """
        pass
    
    pass

class PointGroupChangeInfo(object):
    """
    This class represents PointGroup change information.  An instance of this class is returned by [!:PointGroup.GetPendingChanges].
    """
    PointsToAdd = None
    PointsToRemove = None
    pass

class PointGroupCollection(object):
    """
    This class encapsulates a collction of point groups in the current drawing.
    """
    AllPointsPointGroupId = None
    Count = None
    DrawOrder = None
    Item = None
    def Add(self):
        """
        Add(name: System.String) -> ObjectId
            Adds a new PointGroup with a given name.
            Remarks: If the "_All Points" PointGroup doesn't exist in the current drawing, it is created the first time you add a PointGroup.
            name: System.String
        """
        pass
    
    
    def Contains(self):
        """
        Contains(pointGroupId: ObjectId) -> bool
            Gets whether the collection contains a PointGroup with the given ObjectId.
            pointGroupId: ObjectId
        Contains(name: System.String) -> bool
            Gets whether the collection contains a PointGroup with the given name.
            name: System.String
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> IEnumerator<ObjectId>
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator that can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declared in the IEnumerable interface. This method returns an enumerator that can be use to enumerate this collection.
        """
        pass
    
    
    def GetOutOfDatePointGroupIds(self):
        """
        GetOutOfDatePointGroupIds() -> ObjectIdCollection
            Gets an ObjectIdCollection that contains all the PointGroups that are out of date.
        """
        pass
    
    
    def GetPointGroups(self):
        """
        GetPointGroups(pDatabase: Database) -> PointGroupCollection
            Gets the collection of all PointGroups in the specified database.
            pDatabase: Database
        """
        pass
    
    
    def Remove(self):
        """
        Remove(pointGroupId: ObjectId)
            Removes a PointGroup by ObjectId.
            pointGroupId: ObjectId
        Remove(name: System.String)
            Removes a PointGroup by name.
            name: System.String
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a PointGroup by index.
            index: System.Int32
        """
        pass
    
    
    def UpdateAllPointGroups(self):
        """
        UpdateAllPointGroups()
            Updates all the PointGroups in the current collection.
        """
        pass
    
    pass

class PointGroupElevationOverrideInfo(PointGroupOverrideInfo):
    """
    Defines the information contained in a PointGroup Elevation override.
    """
    FixedElevation = None
    UDP = None
    pass

class PointGroupOverrideInfo(PointGroupElevationOverrideInfo):
    """
    Defines the information in a PointGroup override.
    """
    ActiveOverrideType = None
    XDRefId = None
    pass

class PointGroupOverrideType():
    """
    Defines the types of PointGroup overrides.
    """
    pass

class PointGroupQuery(CustomPointGroupQuery):
    """
    The abstract base class for point group queries.
    """
    QueryString = None
    UseCaseSensitiveMatch = None
    pass

class PointGroupQueryInvalidPointGroupValueException(object):
    """
    This exception is thrown when the value for a PointGroup field in a query is
    invalid.
    """
    InvalidPointGroup = None

    pass

class PointGroupQueryOperationFailedException(object):
    """
    This exception is thrown if the PointGroup object fails to set
    or get the query object.
    """


    pass

class PointGroupQueryParserException(object):
    """
    
    """
    Position = None
    Query = None

    pass

class PointGroupQueryToken(object):
    """
    A class that exposes constants that can be used to add special characters to query strings.
    """
    AND = None
    ClosingParenthesis = None
    Equal = None
    FullDescriptionField = None
    GreaterThan = None
    GreaterThanOrEqual = None
    LessThan = None
    LessThanOrEqual = None
    NameField = None
    NOT = None
    NotEqual = None
    OpeningParenthesis = None
    OR = None
    PointElevationField = None
    PointGroupField = None
    PointNumberField = None
    RawDescriptionField = None
    SingleQuoteCode = None
    ValueDelimiter = None
    pass

class PointGroupRawDescriptionOverrideInfo(PointGroupOverrideInfo):
    """
    Defines the information contained in a PointGroup RawDescription override.
    """
    FixedRawDescription = None
    UDP = None
    pass

class PointInMem(object):
    """
    The point class.
    """
    Codes = None
    Elevation = None
    Index = None
    Offset = None
    Station = None
    pass

class PointNumberResolveType():
    """
    Specifies how to resolve conflicting point number when renumber.
    """
    pass

class PointTable(Entity):
    """
    The AeccDbPointScheduleTable wrapper.
    """


    pass

class PolylineOptions():
    """
    The PolylineOptions class.
    This class specifies the options for creating an Alignment using a polyline.
    """
    AddCurvesBetweenTangents = None
    EraseExistingEntities = None
    PlineId = None
    def Equals(self):
        """
        Equals(obj: System.Object) -> bool
            Compares a PolylineOptions object with a System::Object, returns true if they are equal.
            obj: System.Object
        Equals(other: Autodesk.Civil.DatabaseServices.PolylineOptions) -> PolylineOptions
            Compares two PolylineOptions objects, returns true if they are equal.
            other: Autodesk.Civil.DatabaseServices.PolylineOptions
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode() -> int
            Gets a hash code for the PolylineOptions object.
        """
        pass
    
    pass

class Profile(Entity):
    """
    A record of elevation against distance along a horizontal Alignment or other line. Profiles are used to visualize the terrain 
    along a route of interest, such as a proposed road, or simply to show how the elevation changes across a particular region.
    """
    AlignmentId = None
    DataSourceId = None
    DataSourceName = None
    DesignCheckSetId = None
    DesignCheckSetName = None
    DesignSpeedBased = None
    ElevationMax = None
    ElevationMin = None
    EndingStation = None
    Entities = None
    Length = None
    Offset = None
    Plinegen = None
    ProfileType = None
    PVIs = None
    StartingStation = None
    StyleId = None
    StyleName = None
    UpdateMode = None
    UseDesignCheckSet = None
    UseDesignCriteriaFile = None
    def CreateByLayout(self):
        """
        CreateByLayout(profileName: System.String, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId
            Creates a profile of FG type.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Profile
            profileName: System.String - Name for the new profile, make sure this name is not used by another profile under the specified alignment
            alignmentId: ObjectId - Alignment id to place the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Alignment
            layerId: ObjectId - Layer id to place the new profile, OBJECTID TYPE: Autodesk.AutoCAD.DatabaseServices.LayerTableRecord
            styleId: ObjectId - Style id to apply to the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Styles.AlignmentStyle
            labelSetId: ObjectId - LabelSet id to apply to the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetStyle
        CreateByLayout(profileName: System.String, document: Autodesk.Civil.ApplicationServices.CivilDocument, alignmentName: System.String, layerName: System.String, styleName: System.String, labelSetName: System.String) -> CivilDocument
            Creates a profile of FG type.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Profile
            profileName: System.String - Name for the new profile, make sure this name is not used by another profile under the specified alignment
            document: Autodesk.Civil.ApplicationServices.CivilDocument - CivilDocument to place this new profile
            alignmentName: System.String - Name of the alignment to place this new profile.
            layerName: System.String - Name of the layer for this profile
            styleName: System.String - Name of the style for this profile
            labelSetName: System.String - Name of the label set for this profile
        """
        pass
    
    
    def CreateFromFeatureLine(self):
        """
        CreateFromFeatureLine(profileName: System.String, corridorFeatureLine: Autodesk.Civil.DatabaseServices.CorridorFeatureLine, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> CorridorFeatureLine
            Creates a profile of EG type from a corridor feature line.
            profileName: System.String - The name for the new profile. Make sure this name is not used by another profile under the specified alignment.
            corridorFeatureLine: Autodesk.Civil.DatabaseServices.CorridorFeatureLine - The Corridor Feature Line to be used to create this profile.
            alignmentId: ObjectId - The ObjectId of Alignment for the new profile.
            layerId: ObjectId - The ObjectId of the Layer on which to place the new profile.
            styleId: ObjectId - The ObjectId of the Style to apply to the new profile.
            labelSetId: ObjectId - The ObjectId of the LabelSet to apply to the new profile.
        """
        pass
    
    
    def CreateFromSurface(self):
        """
        CreateFromSurface(profileName: System.String, alignmentId: ObjectId, surfaceId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId
            Creates a profile of EG type from a surface.
            Remarks: This method will use default values for offset, start station and end station.
            default offset = 0, default start station and end station will bind with the parent alignment station.
            profileName: System.String - Name for the new profile, make sure this name is not used by another profile under the specified alignment
            alignmentId: ObjectId - Alignment id to place the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Alignment
            surfaceId: ObjectId - Surface id to place the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Surface
            layerId: ObjectId - Layer id to place the new profile, OBJECTID TYPE: Autodesk.AutoCAD.DatabaseServices.LayerTableRecord
            styleId: ObjectId - Style id to apply to the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Styles.AlignmentStyle
            labelSetId: ObjectId - LabelSet id to apply to the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetStyle
        CreateFromSurface(profileName: System.String, document: Autodesk.Civil.ApplicationServices.CivilDocument, alignmentName: System.String, surfaceName: System.String, layerName: System.String, styleName: System.String, labelSetName: System.String) -> CivilDocument
            Creates a profile of EG type from a surface.
            Remarks: This method will use default values for offset, start station and end station.
            default offset = 0, default start station and end station will bind with the parent alignment station.
            profileName: System.String - The name for the new profile.  Make sure this name is not used by another profile under the specified alignment
            document: Autodesk.Civil.ApplicationServices.CivilDocument - The CivilDocument in which to place this new profile
            alignmentName: System.String - The name of the alignment for this new profile.
            surfaceName: System.String - The name of the surface on which to place this new profile.
            layerName: System.String - The name of the layer for this profile
            styleName: System.String - The name of the style for this profile
            labelSetName: System.String - The name of the label set for this profile
        CreateFromSurface(profileName: System.String, alignmentId: ObjectId, surfaceId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, offset: System.Double, sampleStart: System.Double, sampleEnd: System.Double) -> ObjectId
            Creates a profile of EG type from a surface.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Profile
            profileName: System.String - Name for the new profile, make sure this name is not used by another profile under the specified alignment
            alignmentId: ObjectId - Alignment id to place the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Alignment
            surfaceId: ObjectId - Surface id to place the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Surface
            layerId: ObjectId - Layer id to place the new profile, OBJECTID TYPE: Autodesk.AutoCAD.DatabaseServices.LayerTableRecord
            styleId: ObjectId - Style id to apply to the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Styles.AlignmentStyle
            labelSetId: ObjectId - LabelSet id to apply to the new profile, OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetStyle
            offset: System.Double - Sets the offset value to create this Profile. 
            sampleStart: System.Double - Sets the start sample station for this Profile, it should be within Alignment station range
            sampleEnd: System.Double - Sets the end sample station for this Profile, it should be within Alignment station range
        CreateFromSurface(profileName: System.String, document: Autodesk.Civil.ApplicationServices.CivilDocument, alignmentName: System.String, surfaceName: System.String, layerName: System.String, styleName: System.String, labelSetName: System.String, offset: System.Double, sampleStart: System.Double, sampleEnd: System.Double) -> CivilDocument
            Creates a profile of EG type from a surface.
            Remarks: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Profile
            profileName: System.String - Name for the new profile, make sure this name is not used by another profile under the specified alignment
            document: Autodesk.Civil.ApplicationServices.CivilDocument - CivilDocument to place this new profile
            alignmentName: System.String - Name of the alignment to place this new profile.
            surfaceName: System.String - Name of the surface to place this new profile.
            layerName: System.String - Name of the layer for this profile
            styleName: System.String - Name of the style for this profile
            labelSetName: System.String - Name of the label set for this profile
            offset: System.Double - Sets the offset value to create this Profile. 
            sampleStart: System.Double - Sets the start sample station for this Profile, it should be within Alignment station range
            sampleEnd: System.Double - Sets the end sample station for this Profile, it should be within Alignment station range
        """
        pass
    
    
    def ElevationAt(self):
        """
        ElevationAt(station: System.Double) -> double
            Gets the elevation at a specified station.
            station: System.Double - Station value.
        """
        pass
    
    
    def GradeAt(self):
        """
        GradeAt(station: System.Double) -> double
            Given a station, gets the instantaneous grade and the algebraic difference.
            station: System.Double - Station value.
        """
        pass
    
    pass

class ProfileBandLabelGroup(Entity):
    """
    This class serves as a base class for all profile band related group labels.
    """
    StyleId = None
    StyleName = None
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(runtimeClass: RXClass, profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all band label groups that match the specified runtimeClass in the ProfileView.
            runtimeClass: RXClass - The type of the label group class.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of HorizontalGeometryBandLabelGroup.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(runtimeClass: RXClass, profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns a collection of object ids pointing to all the available band label groups that match the specified runtimeClass in the profile view.
            runtimeClass: RXClass - The type of the label group class.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of HorizontalGeometryBandLabelGroup.
        """
        pass
    
    pass

class ProfileCircular(ProfileEntity):
    """
    The ProfileCircular class.  
    This class represents an ProfileEntity made up of a circular curve.
    """
    CurveType = None
    EntityType = None
    GradeChange = None
    GradeIn = None
    GradeOut = None
    HighLowPointElevation = None
    HighLowPointStation = None
    K = None
    M = None
    PVIElevation = None
    PVIStation = None
    Radius = None
    TangentOffsetAtPVI = None

    pass

class ProfileCrestCurveLabelGroup(Entity):
    """
    This class represents a profile crest curve label group.
    """

    def Create(self):
        """
        Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId
            Creates a new instance of ProfileCrestCurveLabelGroup on the profile in the specified with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label group is located.
            profileId: ObjectId - The ObjectId of profile in which the label group is located.
            styleId: ObjectId - The ObjectId of ProfileCrestCurveLabelGroup style.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileCrestCurveLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileCrestCurveLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileCrestCurveLabelGroup.
        """
        pass
    
    pass

class ProfileCriteria(object):
    """
    A critera that specifies the profile that defines the upper or lower boundary of a ProfileHatchArea.  Each ProfileHatchArea has two criteria to define the upper and lower boundaries.
    """
    BoundaryType = None
    ProfileId = None
    ProfileName = None
    pass

class ProfileCriteriaCollection(object):
    """
    The ProfileCriteria collection class represents the collection of all criteria in the hatch area.  Criteria define the profiles that set the upper and lower boundaries of the hatch area.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(profileId: ObjectId, type: Autodesk.Civil.DatabaseServices.HatchCriteriaBoundaryType) -> HatchCriteriaBoundaryType
            Adds an Autodesk.Civil.DatabaseServices.ProfileCriteria to the collection.
            profileId: ObjectId - The profile id of the hatch area criteria.
            type: Autodesk.Civil.DatabaseServices.HatchCriteriaBoundaryType - The profile hatch area criteria's boundary type.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileCriteria
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
            Removes an Autodesk.Civil.DatabaseServices.ProfileCriteria from the collection.
            index: System.Int32 - The index of the ProfileCriteria in the ProfileCriteriaCollection.
        """
        pass
    
    pass

class ProfileCrossing(Entity):
    """
    The AeccDbProfileCrossing class.
    """


    pass

class ProfileDataBandLabelGroup(Entity):
    """
    
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileDataBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileDataBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileDataBandLabelGroup.
        """
        pass
    
    pass

class ProfileEntity(ProfileCircular):
    """
    The abstract class of profile entity. ProfileEntity has four derived classes: ProfileLine, ProfileAsymmetric, ProfileCircular,
    and ProfileParabolic.
    """
    Constraint1 = None
    Constraint2 = None
    EndElevation = None
    EndStation = None
    EntityAfter = None
    EntityBefore = None
    EntityId = None
    EntityType = None
    HighestDesignSpeed = None
    Length = None
    MinimumKValueHSD = None
    MinimumKValuePSD = None
    MinimumKValueSSD = None
    StartElevation = None
    StartStation = None
    def DesignChecks(self):
        """
        DesignChecks() -> ProfileDesignCheck
            Gets the collection of applicable design checks.
        """
        pass
    
    
    def ValidateDesignCheck(self):
        """
        ValidateDesignCheck(designCheck: Autodesk.Civil.ProfileDesignCheck, curveType: Autodesk.Civil.ProfileApplyCurveType) -> ProfileDesignCheck
            Validate a specific design check on this entity.
            designCheck: Autodesk.Civil.ProfileDesignCheck - The design check to validate.
            curveType: Autodesk.Civil.ProfileApplyCurveType - The curve type to use for the validation.
        """
        pass
    
    pass

class ProfileEntityCollection(object):
    """
    The ProfileEntity collection class.  This class represents the collection of all ProfileEntity objects that belong to the Profile.
    """
    Count = None
    FirstEntity = None
    Item = None
    LastEntity = None
    def AddFixedSymmetricParabolaByEntityEndAndThroughPoint(self):
        """
        AddFixedSymmetricParabolaByEntityEndAndThroughPoint(attachEntityId: System.UInt32, passPoint: Point2d) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by the entity to attach to and pass-through point.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            attachEntityId: System.UInt32 - Id of the entity to attach to.
            passPoint: Point2d - The pass-through point.
        AddFixedSymmetricParabolaByEntityEndAndThroughPoint(attachEntityId: System.UInt32, passPoint: Point3d) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by the entity to attach to and pass-through point.
            attachEntityId: System.UInt32 - Id of the entity to attach to.
            passPoint: Point3d - The pass-through point.
        """
        pass
    
    
    def AddFixedSymmetricParabolaByThreePoints(self):
        """
        AddFixedSymmetricParabolaByThreePoints(point: Point2d, point2: Point2d, point3: Point2d) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 3 pass-through points.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            point: Point2d - The first pass-through point.
            point2: Point2d - The second pass-through point.
            point3: Point2d - The third pass-through point.
        AddFixedSymmetricParabolaByThreePoints(point: Point3d, point2: Point3d, point3: Point3d) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 3 pass-through points.
            point: Point3d - The first pass-through point.
            point2: Point3d - The second pass-through point.
            point3: Point3d - The third pass-through point.
        """
        pass
    
    
    def AddFixedSymmetricParabolaByTwoPointsAndEndGrade(self):
        """
        AddFixedSymmetricParabolaByTwoPointsAndEndGrade(point1: Point2d, point2: Point2d, endGrade: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and the grade at the end point.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            point1: Point2d - The first pass-through point.
            point2: Point2d - The second pass-through point.
            endGrade: System.Double - The grade at the end point.
        AddFixedSymmetricParabolaByTwoPointsAndEndGrade(point1: Point3d, point2: Point3d, endGrade: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and the grade at the end point.
            point1: Point3d - The first pass-through point.
            point2: Point3d - The second pass-through point.
            endGrade: System.Double - The grade at the end point.
        """
        pass
    
    
    def AddFixedSymmetricParabolaByTwoPointsAndK(self):
        """
        AddFixedSymmetricParabolaByTwoPointsAndK(point1: Point2d, point2: Point2d, curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType, k: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and K value.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            point1: Point2d - The first pass-through point.
            point2: Point2d - The second pass-through point.
            curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType - Specifies the vertical curve type, crest or sag.
            k: System.Double - The K value.
        AddFixedSymmetricParabolaByTwoPointsAndK(point1: Point3d, point2: Point3d, curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType, k: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and K value.
            point1: Point3d - The first pass-through point.
            point2: Point3d - The second pass-through point.
            curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType - Specifies the vertical curve type, crest or sag.
            k: System.Double - The K value.
        """
        pass
    
    
    def AddFixedSymmetricParabolaByTwoPointsAndRadius(self):
        """
        AddFixedSymmetricParabolaByTwoPointsAndRadius(point1: Point2d, point2: Point2d, curType: Autodesk.Civil.DatabaseServices.VerticalCurveType, radius: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and radius.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            point1: Point2d - The first pass-through point.
            point2: Point2d - The second pass-through point.
            curType: Autodesk.Civil.DatabaseServices.VerticalCurveType - Specifies the vertical curve type, crest or sag.
            radius: System.Double - The radius value.
        AddFixedSymmetricParabolaByTwoPointsAndRadius(point1: Point3d, point2: Point3d, curType: Autodesk.Civil.DatabaseServices.VerticalCurveType, radius: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and radius.
            point1: Point3d - The first pass-through point.
            point2: Point3d - The second pass-through point.
            curType: Autodesk.Civil.DatabaseServices.VerticalCurveType - Specifies the vertical curve type, crest or sag.
            radius: System.Double - The radius value.
        """
        pass
    
    
    def AddFixedSymmetricParabolaByTwoPointsAndStartGrade(self):
        """
        AddFixedSymmetricParabolaByTwoPointsAndStartGrade(point1: Point2d, point2: Point2d, startGrade: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and the grade at the start point.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            point1: Point2d - The first pass-through point.
            point2: Point2d - The second pass-through point.
            startGrade: System.Double - The grade at the start point.
        AddFixedSymmetricParabolaByTwoPointsAndStartGrade(point1: Point3d, point2: Point3d, startGrade: System.Double) -> ProfileParabolaSymmetric
            Creates a fixed Symmetric Parabola defined by 2 pass-through points and the grade at the start point.
            point1: Point3d - The first pass-through point.
            point2: Point3d - The second pass-through point.
            startGrade: System.Double - The grade at the start point.
        """
        pass
    
    
    def AddFixedTangent(self):
        """
        AddFixedTangent(startPoint: Point2d, endPoint: Point2d) -> ProfileTangent
            Creates a fixed Tangent defined by 2 pass-through points.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            startPoint: Point2d - The first pass-through point.
            endPoint: Point2d - The second pass-through point.
        AddFixedTangent(startPoint: Point3d, endPoint: Point3d) -> ProfileTangent
            Creates a fixed Tangent defined by 2 pass-through points.
            startPoint: Point3d - The first pass-through point.
            endPoint: Point3d - The second pass-through point.
        """
        pass
    
    
    def AddFixedTangentWithPreviousEntity(self):
        """
        AddFixedTangentWithPreviousEntity(previousEntityId: System.UInt32, startPoint: Point2d, endPoint: Point2d) -> ProfileTangent
            Creates a fixed Tangent defined by 2 pass-through points and previous entity id.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            previousEntityId: System.UInt32 - Previous entity id to connect this entity. If previous entity is 
            disconnected with the new entity, this parameter will be ommited.
            startPoint: Point2d - The first pass-through point.
            endPoint: Point2d - The second pass-through point.
        AddFixedTangentWithPreviousEntity(previousEntityId: System.UInt32, startPoint: Point3d, endPoint: Point3d) -> ProfileTangent
            Creates a fixed Tangent defined by 2 pass-through points and previous entity id.
            previousEntityId: System.UInt32 - Previous entity id to connect this entity. If previous entity is 
            disconnected with the new entity, this parameter will be ommited.
            startPoint: Point3d - The first pass-through point.
            endPoint: Point3d - The second pass-through point.
        """
        pass
    
    
    def AddFloatingSymmetricParabolaByThroughPointAndGrade(self):
        """
        AddFloatingSymmetricParabolaByThroughPointAndGrade(attachEntityId: System.UInt32, passPoint: Point2d, grade: System.Double, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileParabolaSymmetric
            Creates a floating Symmetric Parabola defined by an entity to attach to, a pass-through point and the grade value at the end point.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            attachEntityId: System.UInt32 - The entity to attach to.
            passPoint: Point2d - The pass-through point.
            grade: System.Double - The grade value at the end point.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        AddFloatingSymmetricParabolaByThroughPointAndGrade(attachEntityId: System.UInt32, passPoint: Point3d, grade: System.Double, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileParabolaSymmetric
            Creates a floating Symmetric Parabola defined by an entity to attach to, a pass-through point and the grade value at the end point.
            attachEntityId: System.UInt32 - The entity to attach to.
            passPoint: Point3d - The pass-through point.
            grade: System.Double - The grade value at the end point.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        """
        pass
    
    
    def AddFloatingSymmetricParabolaByThroughPointAndK(self):
        """
        AddFloatingSymmetricParabolaByThroughPointAndK(attachEntityId: System.UInt32, passPoint: Point2d, k: System.Double, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileParabolaSymmetric
            Creates a floating Symmetric Parabola defined by an entity to attach to, a pass-through point and the K value.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            attachEntityId: System.UInt32 - The entity to attach to.
            passPoint: Point2d - The pass-through point.
            k: System.Double - The K value.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        AddFloatingSymmetricParabolaByThroughPointAndK(attachEntityId: System.UInt32, passPoint: Point3d, k: System.Double, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileParabolaSymmetric
            Creates a floating Symmetric Parabola defined by an entity to attach to, a pass-through point and the K value.
            attachEntityId: System.UInt32 - The entity to attach to.
            passPoint: Point3d - The pass-through point.
            k: System.Double - The K value.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        """
        pass
    
    
    def AddFloatingSymmetricParabolaByThroughPointAndRadius(self):
        """
        AddFloatingSymmetricParabolaByThroughPointAndRadius(attachEntityId: System.UInt32, passPoint: Point2d, radius: System.Double, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileParabolaSymmetric
            Creates a floating Symmetric Parabola defined by an entity to attach to, a pass-through point and the radius value.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            attachEntityId: System.UInt32 - The entity to attach to.
            passPoint: Point2d - The pass-through point.
            radius: System.Double - The radius 
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        AddFloatingSymmetricParabolaByThroughPointAndRadius(attachEntityId: System.UInt32, passPoint: Point3d, radius: System.Double, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileParabolaSymmetric
            Creates a floating Symmetric Parabola defined by an entity to attach to, a pass-through point and the radius value.
            attachEntityId: System.UInt32 - The entity to attach to.
            passPoint: Point3d - The pass-through point.
            radius: System.Double - The radius 
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        """
        pass
    
    
    def AddFloatingTangent(self):
        """
        AddFloatingTangent(entityId: System.UInt32, passPoint: Point2d, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileTangent
            Creates a floating Tangent defined by an entity and a pass-through point, whether to append or prepend
            to the specified entity is determined by the closest point to the passPoint.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            entityId: System.UInt32 - Id of the entity to attach to.
            passPoint: Point2d - The pass-through point.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        AddFloatingTangent(entityId: System.UInt32, passPoint: Point3d, attachType: Autodesk.Civil.DatabaseServices.EntityAttachType) -> ProfileTangent
            Creates a floating Tangent defined by an entity and a pass-through point, whether to append or prepend
            to the specified entity is determined by the closest point to the passPoint.
            entityId: System.UInt32 - Id of the entity to attach to.
            passPoint: Point3d - The pass-through point.
            attachType: Autodesk.Civil.DatabaseServices.EntityAttachType - Specifies whether you want to append or prepend the new entity.
        """
        pass
    
    
    def AddFreeAsymmetricParabolaByPVIAndLengths(self):
        """
        AddFreeAsymmetricParabolaByPVIAndLengths(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, length1: System.Double, length2: System.Double) -> ProfileParabolaAsymmetric
            Creates a free Asymmetric Parabola constrained by a PVI and 2 parabola lengths.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            length1: System.Double - The length of the parabola in.
            length2: System.Double - The length of the parabola out.
        """
        pass
    
    
    def AddFreeCircularCurveByPVIAndLength(self):
        """
        AddFreeCircularCurveByPVIAndLength(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, length: System.Double) -> ProfileCircular
            Creates a free Circular Curve constrained by a PVI and length.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to
            length: System.Double - The length value.
        """
        pass
    
    
    def AddFreeCircularCurveByPVIAndRadius(self):
        """
        AddFreeCircularCurveByPVIAndRadius(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, radius: System.Double) -> ProfileCircular
            Creates a free Circular Curve constrained by a PVI and radius.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            radius: System.Double - The radius value.
        """
        pass
    
    
    def AddFreeCircularCurveByPVIAndThroughPoint(self):
        """
        AddFreeCircularCurveByPVIAndThroughPoint(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, passPoint: Point2d) -> ProfileCircular
            Creates a free Circular Curve constrained by a PVI and a pass-through point.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            passPoint: Point2d - The pass-through point.
        AddFreeCircularCurveByPVIAndThroughPoint(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, passPoint: Point3d) -> ProfileCircular
            Creates a free Circular Curve constrained by a PVI and a pass-through point.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            passPoint: Point3d - The pass-through point.
        """
        pass
    
    
    def AddFreeSymmetricParabolaByK(self):
        """
        AddFreeSymmetricParabolaByK(previousEntityId: System.UInt32, nextEntityId: System.UInt32, curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType, k: System.Double) -> ProfileParabolaSymmetric
            Creates a free Symmetric Parabola between two entities and the K value.
            Remarks: The parameter curveType is only applicable when the parabola is added between two ProfileParabolaSymmetric entities.
            previousEntityId: System.UInt32 - The previous entity to attach to.
            nextEntityId: System.UInt32 - The next entity to attach to.
            curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType - The vertical curve type, crest or sag.
            k: System.Double - The K value.
        """
        pass
    
    
    def AddFreeSymmetricParabolaByLength(self):
        """
        AddFreeSymmetricParabolaByLength(previousEntityId: System.UInt32, nextEntityId: System.UInt32, curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType, length: System.Double, preferFlat: System.Boolean) -> ProfileParabolaSymmetric
            Creates a free Symmetric Parabola between two entities with the specified curve length.
            Remarks: The parameter curveType is applicable when the parabola is added between two ProfileParabolaSymmetric entities.
            The parameter preferFlat is applicable when the parabola is added between a ProfileTangent and ProfileparabolaSymmetric entity.
            previousEntityId: System.UInt32 - The previous entity to attach to.
            nextEntityId: System.UInt32 - The next entity to attach to.
            curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType - The vertical curve type, crest or sag.
            length: System.Double - The curve length.
            preferFlat: System.Boolean - Specifies whether to choose the flat curve if two solutions are available. Steep curve is preferred if preferFlat is false.
        """
        pass
    
    
    def AddFreeSymmetricParabolaByPVIAndCurveLength(self):
        """
        AddFreeSymmetricParabolaByPVIAndCurveLength(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, curveLength: System.Double) -> ProfileParabolaSymmetric
            Creates a free Symmetric Parabola constrained by a PVI and curve length.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            curveLength: System.Double - The curve length.
        """
        pass
    
    
    def AddFreeSymmetricParabolaByPVIAndK(self):
        """
        AddFreeSymmetricParabolaByPVIAndK(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, k: System.Double) -> ProfileParabolaSymmetric
            Creates a free Symmetric Parabola constrained by a PVI and K value.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            k: System.Double - The K value.
        """
        pass
    
    
    def AddFreeSymmetricParabolaByPVIAndThroughPoint(self):
        """
        AddFreeSymmetricParabolaByPVIAndThroughPoint(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, passPoint: Point2d) -> ProfileParabolaSymmetric
            Creates a free Symmetric Parabola constrained by a PVI and a pass-through point.
            Remarks: Point2d.X and Point2d.Y are the profile's station and elevation respectively.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            passPoint: Point2d - The pass-through point.
        AddFreeSymmetricParabolaByPVIAndThroughPoint(attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI, passPoint: Point3d) -> ProfileParabolaSymmetric
            Creates a free Symmetric Parabola constrained by a PVI and a pass-through point.
            attachProfilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI - The PVI to attach to.
            passPoint: Point3d - The pass-through point.
        """
        pass
    
    
    def AddFreeSymmetricParabolaByRadius(self):
        """
        AddFreeSymmetricParabolaByRadius(previousEntityId: System.UInt32, nextEntityId: System.UInt32, curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType, radius: System.Double) -> ProfileParabolaSymmetric
            Creates a free Symmetric Parabola between two entities and the radius value.
            Remarks: The parameter curveType is applicable when the parabola is added between two ProfileParabolaSymmetric entities.
            previousEntityId: System.UInt32 - The previous entity to attach to.
            nextEntityId: System.UInt32 - The next entity to attach to.
            curveType: Autodesk.Civil.DatabaseServices.VerticalCurveType - The vertical curve type, crest or sag.
            radius: System.Double - The radius value.
        """
        pass
    
    
    def AddFreeTangent(self):
        """
        AddFreeTangent(previousEntityId: System.UInt32, nextEntityId: System.UInt32) -> ProfileTangent
            Creates a free Tangent between two entities.
            previousEntityId: System.UInt32 - Id of the previous entity to attach to.
            nextEntityId: System.UInt32 - Id of the next entity to attach to.
        """
        pass
    
    
    def Clear(self):
        """
        Clear()
            Removes all Profile entities from the collection.
        """
        pass
    
    
    def EntityAtId(self):
        """
        EntityAtId(id: System.UInt32) -> ProfileEntity
            Returns the ProfileEntity specified by ID.
            id: System.UInt32 - 
            The integer ID for the ProfileEntity. Which is unique in a collection.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileEntity
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
        Remove(entity: Autodesk.Civil.DatabaseServices.ProfileEntity) -> ProfileEntity
            Removes from the collection by the specified entity object.
            entity: Autodesk.Civil.DatabaseServices.ProfileEntity - Specifies the entity of the ProfileEntity to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes from the collection by the specified index.
            index: System.Int32 - Specifies index in the collection to remove.
        """
        pass
    
    pass

class ProfileEntityConstraintType():
    """
    Specifies the connection constraint type of ProfileEntity, including fixed(attached to none entity), float(attached to one entity) and free(attached to two entities).
    """
    pass

class ProfileEntityType():
    """
    Specifies the underlying ProfileEntity type, including tangent, circular, symmetric parabola and asymmetric parabola.
    """
    pass

class ProfileHatchArea(object):
    """
    Manages how areas of cut or fill are highlighted in a ProfileView.
    """
    Criteria = None
    Name = None
    ShapeStyleId = None
    ShapeStyleName = None
    pass

class ProfileHatchAreaCollection(object):
    """
    The ProfileHatchAreaCollection class represents the collection of all hatch area definitions in the ProfileView.  A ProfileHatchArea defines the appearance of cut or fill areas in a ProfileView.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(hatchAreaName: System.String, upperProfileId: ObjectId, lowerProfileId: ObjectId, shapeStyleId: ObjectId)
            Adds an Autodesk.Civil.DatabaseServices.ProfileHatchArea to the collection.
            hatchAreaName: System.String - Profile hatch area name.
            upperProfileId: ObjectId - Profile hatch area criteria's upper boundary object id.
            lowerProfileId: ObjectId - Profile hatch area criteria's lower boundary object id.
            shapeStyleId: ObjectId - Profile hatch area's shape style id.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileHatchArea
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
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
        Remove(hatchAreaName: System.String)
            Removes an Autodesk.Civil.DatabaseServices.ProfileHatchArea by the hatch area name from the collection.
            hatchAreaName: System.String - Profile hatch area name to remove.
        """
        pass
    
    pass

class ProfileHorizontalGeometryPointLabelGroup(Entity):
    """
    This class represents a profile horizontal geometry point label group.
    """
    StaggerLineHeight1 = None
    StaggerLineHeight2 = None
    def Create(self):
        """
        Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId
            Creates a new instance of ProfileHorizontalGeometryPointLabelGroup on the profile in the specified with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label group is located.
            profileId: ObjectId - The ObjectId of profile in which the label group is located.
            styleId: ObjectId - The ObjectId of ProfileHorizontalGeometryPointLabelGroup style.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileHorizontalGeometryPointLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileHorizontalGeometryPointLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileHorizontalGeometryPointLabelGroup.
        """
        pass
    
    
    def GetGeometryPointsOptions(self):
        """
        GetGeometryPointsOptions() -> GeometryPointSelector
            Gets a GeometryPointSelector containing the state of all ProfilePointTypes for the current label.
        """
        pass
    
    
    def SetGeometryPointsOptions(self):
        """
        SetGeometryPointsOptions(profileGeometryPoints: Autodesk.Civil.GeometryPointSelector) -> GeometryPointSelector
            Sets the state of all ProfilePointTypes for the current label.
            profileGeometryPoints: Autodesk.Civil.GeometryPointSelector
        """
        pass
    
    pass

class ProfileLabelGroup(Entity):
    """
    This class represents an profile label group.
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(runtimeClass: RXClass, profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of labels on the Profile of a specified type.
            runtimeClass: RXClass - The type of the label group class.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of the specified type.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(runtimeClass: RXClass, profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns the ObjectId collection of labels on the profile of a specified type.
            runtimeClass: RXClass - The type of the label group class.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of the specified type.
        """
        pass
    
    pass

class ProfileLineLabelGroup(Entity):
    """
    This class represents a profile line label group.
    """
    Weeding = None
    def Create(self):
        """
        Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId
            Creates a new instance of ProfileLineLabelGroup on the profile in the specified with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label group is located.
            profileId: ObjectId - The ObjectId of profile in which the label group is located.
            styleId: ObjectId - The ObjectId of ProfileLineLabelGroup style.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileLineLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all ProfileLineLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileLineLabelGroup.
        """
        pass
    
    pass

class ProfileMinorStationLabelGroup(Entity):
    """
    This class represents a profile minor station label group.
    """
    MajorStationLabelGroup = None
    def Create(self):
        """
        Create(styleId: ObjectId, majorStationLabelGroupId: ObjectId, increment: System.Double) -> ObjectId
            Creates a new instance of ProfileMinorStationLabelGroup on the profile in the specified with the specified label style.
            styleId: ObjectId - The style ID of the new ProfileMinorStationLabelGroup.
            majorStationLabelGroupId: ObjectId - The object ID of major station label group.
            increment: System.Double - The increment value at which to insert major and minor station labels.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfileMinorStationLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfileMinorStationLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileMinorStationLabelGroup.
        """
        pass
    
    pass

class ProfileOverride(GraphOverride):
    """
    Object used to change the style or label set for a profile.
    """
    OverrideStyleId = None
    OverrideStyleName = None
    ProfileId = None
    ProfileName = None
    def GetLabelGroupIds(self):
        """
        GetLabelGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the Profile's label group.
        """
        pass
    
    
    def GetProfileLabelGroupIds(self):
        """
        GetProfileLabelGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the Profile's label group.
        """
        pass
    
    pass

class ProfileOverrideCollection(GraphOverrideCollection):
    """
    The ProfileOverride collection class represents the collection of all profiles listed in the ProfileView.
    """
    SplitAt = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileOverride
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class ProfilePVI(object):
    """
    In a profile, the point where the lines formed by two tangent entities meet, whether the entities meet or not (the "Point of Vertical Intersection").
    """
    Elevation = None
    EntityAfter = None
    EntityBefore = None
    GradeIn = None
    GradeOut = None
    HeadlightSightDistance = None
    PassingSightDistance = None
    PVIType = None
    Station = None
    StoppingSightDistance = None
    VerticalCurve = None
    pass

class ProfilePVICollection(object):
    """
    The ProfilePVI collection class represents the collection of all ProfilePVI objects that belong to a Profile.
    """
    Count = None
    Item = None
    def AddPVI(self):
        """
        AddPVI(station: System.Double, elevation: System.Double) -> ProfilePVI
            Adds an Autodesk.Civil.DatabaseServices.ProfilePVI with a type of ProfileEntityType.Tangent to the collection.
            Remarks: The value of station is limited by the profile view in the UI, but it's not limited in the API.
            station: System.Double - Station value for the new PVI.
            elevation: System.Double - Elevation value for the new PVI.
        """
        pass
    
    
    def AddPVIArc(self):
        """
        AddPVIArc(station: System.Double, elevation: System.Double, radius: System.Double) -> ProfilePVI
            Adds an Autodesk.Civil.DatabaseServices.ProfilePVI with a type of ProfileEntityType.Circular to the collection.
            station: System.Double - The station value for the new PVI.
            elevation: System.Double - The elevation value for the new PVI.
            radius: System.Double - The radius value of the Arc for the new PVI.
        """
        pass
    
    
    def AddPVIAsymParabola(self):
        """
        AddPVIAsymParabola(station: System.Double, elevation: System.Double, tangentLen1: System.Double, tangentLen2: System.Double) -> ProfilePVI
            Adds an Autodesk.Civil.DatabaseServices.ProfilePVI with a type of ProfileEntityType.ParabolaAsymmetric to the collection.
            station: System.Double - The station value for the new PVI.
            elevation: System.Double - The elevation value for the new PVI.
            tangentLen1: System.Double - The lentgh value of the first tangent for the new PVI.
            tangentLen2: System.Double - The lentgh value of the second tangent for the new PVI.
        """
        pass
    
    
    def AddPVISymParabola(self):
        """
        AddPVISymParabola(station: System.Double, elevation: System.Double, curveLength: System.Double) -> ProfilePVI
            Adds an Autodesk.Civil.DatabaseServices.ProfilePVI with a type of ProfileEntityType.ParabolaSymmetric to the collection.
            station: System.Double - The station value for the new PVI.
            elevation: System.Double - The elevation value for the new PVI.
            curveLength: System.Double - The lentgh value of the Arc for the new PVI.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfilePVI
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetPVIAt(self):
        """
        GetPVIAt(station: System.Double, elevation: System.Double) -> ProfilePVI
            Gets the PVI in the collection closest to the given station and elevation.
            station: System.Double - Station value.
            elevation: System.Double - Elevation value.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(profilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI) -> ProfilePVI
            Removes a specific profile PVI from the collection.
            profilePVI: Autodesk.Civil.DatabaseServices.ProfilePVI
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes the specified PVI from this profile.
            Remarks: The the first and the last PVI cannot be removed.
            index: System.Int32 - The index of the PVI in the ProfilePVICollection.
        RemoveAt(station: System.Double, elevation: System.Double)
            Removes the profile PVI from the collection closest to the given station and elevation.
            Remarks: The first and the last PVI cannot be removed.
            station: System.Double - Station value.
            elevation: System.Double - Elevation value.
        """
        pass
    
    pass

class ProfilePVILabelGroup(Entity):
    """
    This class represents a profile PVI label group.
    """
    StaggerLineHeight1 = None
    StaggerLineHeight2 = None
    Weeding = None
    def Create(self):
        """
        Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId
            Creates a new instance of ProfilePVILabelGroup on the profile in the specified with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label group is located.
            profileId: ObjectId - The ObjectId of profile in which the label group is located.
            styleId: ObjectId - The ObjectId of ProfilePVILabelGroup style.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfilePVILabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfilePVILabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfilePVILabelGroup.
        """
        pass
    
    pass

class ProfileParabolaAsymmetric(ProfileEntity):
    """
    The ProfileParabolaAsymmetric class.  
    This class represents an ProfileEntity made up of a asymmetric parabola.
    """
    AsymmetricLength1 = None
    AsymmetricLength2 = None
    CurveType = None
    EntityType = None
    GradeChange = None
    GradeIn = None
    GradeOut = None
    HighLowPointElevation = None
    HighLowPointStation = None
    K = None
    PVIElevation = None
    PVIStation = None
    TangentOffsetAtPVI = None

    pass

class ProfileParabolaSymmetric(ProfileEntity):
    """
    This class represents an ProfileEntity made up of a symmetric parabola.
    """
    CurveType = None
    EntityType = None
    GradeAtThroughPoint1 = None
    GradeAtThroughPoint2 = None
    GradeChange = None
    GradeIn = None
    GradeOut = None
    HighLowPointElevation = None
    HighLowPointStation = None
    K = None
    M = None
    PVIElevation = None
    PVIStation = None
    Radius = None
    TangentOffsetAtPVI = None
    ThroughPoint1Elevation = None
    ThroughPoint1Station = None
    ThroughPoint2Elevation = None
    ThroughPoint2Station = None
    ThroughPoint3Elevation = None
    ThroughPoint3Station = None
    def GetHeadlightSightDistance(self):
        """
        GetHeadlightSightDistance(maxAngle: System.Double, headlightHeight: System.Double) -> double
            Gets the headlight sight distance with the given headlight angle and headlight height.
            Remarks: Only valid for sag curve.
            This design method for sag curves provides a minimum curve length. The curve must be long 
            enough so that in dark driving conditions, the headlights of a standard vehicle illuminate 
            the road a safe distance beyond the stopping distance for the designed speed of travel.
            maxAngle: System.Double - Headlight Angle. 
            headlightHeight: System.Double - Headlight Height. 
        """
        pass
    
    
    def GetPassingSightDistance(self):
        """
        GetPassingSightDistance(eyeHeight: System.Double, objectHeight: System.Double) -> double
            Gets the passing sight distance with the given eye height and object height.
            Remarks: Only valid for crest curve.
            This design method for crest curves provides a minimum curve length. The curve must be long enough so that
            the driver of a standard vehicle can always see an oncoming vehicle within a safe distance for the designed speed of travel.
            eyeHeight: System.Double - Eye Height. 
            objectHeight: System.Double - Object Height. 
        """
        pass
    
    
    def GetStoppingSightDistance(self):
        """
        GetStoppingSightDistance(eyeHeight: System.Double, objectHeight: System.Double) -> double
            Gets the stopping sight distance with the given eye height and object height.
            Remarks: Only valid for crest curve.
            This design method for crest curves provides a minimum curve length. The curve must be long enough so that the driver 
            of a standard vehicle can always see an object before it gets within the maximum stopping distance for the designed speed of travel.
            eyeHeight: System.Double - Eye Height. 
            objectHeight: System.Double - Object Height. 
        """
        pass
    
    
    def SetHeadlightSightDistance(self):
        """
        SetHeadlightSightDistance(maxAngle: System.Double, headlightHeight: System.Double, distance: System.Double)
            Sets the headlight sight distance with the given headlight angle and headlight height.
            Remarks: Only valid for sag curve.
            This design method for sag curves provides a minimum curve length. The curve must be long 
            enough so that in dark driving conditions, the headlights of a standard vehicle illuminate 
            the road a safe distance beyond the stopping distance for the designed speed of travel.
            maxAngle: System.Double - Headlight Angle. 
            headlightHeight: System.Double - Headlight Height. 
            distance: System.Double - New Headlight Sight Distance value. 
        """
        pass
    
    
    def SetPassingSightDistance(self):
        """
        SetPassingSightDistance(eyeHeight: System.Double, objectHeight: System.Double, distance: System.Double)
            Sets the passing sight distance with the given eye height and object height.
            Remarks: Only valid for crest curve.
            This design method for crest curves provides a minimum curve length. The curve must be long enough so that
            the driver of a standard vehicle can always see an oncoming vehicle within a safe distance for the designed speed of travel.
            eyeHeight: System.Double - Eye Height. 
            objectHeight: System.Double - Object Height. 
            distance: System.Double - New Passing Sight Distance value. 
        """
        pass
    
    
    def SetStoppingSightDistance(self):
        """
        SetStoppingSightDistance(eyeHeight: System.Double, objectHeight: System.Double, distance: System.Double)
            Sets the stopping sight distance with the given eye height and object height.
            Remarks: Only valid for crest curve.
            This design method for crest curves provides a minimum curve length. The curve must be long enough so that the driver 
            of a standard vehicle can always see an object before it gets within the maximum stopping distance for the designed speed of travel.
            eyeHeight: System.Double - Eye Height. 
            objectHeight: System.Double - Object Height. 
            distance: System.Double - New Stopping Sight Distance value. 
        """
        pass
    
    pass

class ProfileProjection(Entity):
    """
    The AeccDbProfileProjection class.
    """


    pass

class ProfileProjectionLabel(Entity):
    """
    This class represents an profile projection label.
    """
    ProjectionSourceId = None
    def Create(self):
        """
        Create(profileViewId: ObjectId, profileProjectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of ProfileProjectionLabel on the profileview with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label is located.
            profileProjectionId: ObjectId - The ObjectId of ProfileProjectionLabel's feature object.
            labelStyleId: ObjectId - The ObjectId of ProfileProjectionLabel style.
        """
        pass
    
    pass

class ProfileSagCurveLabelGroup(Entity):
    """
    This class represents a profile sag curve label group.
    """

    def Create(self):
        """
        Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId
            Creates a new instance of ProfileSagCurveLabelGroup on the profile in the specified with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label group is located.
            profileId: ObjectId - The ObjectId of profile in which the label group is located.
            styleId: ObjectId - The ObjectId of ProfileSagCurveLabelGroup style.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfileSagCurveLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfileSagCurveLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileSagCurveLabelGroup.
        """
        pass
    
    pass

class ProfileStationLabelGroup(Entity):
    """
    This class represents a profile station label group.
    """
    Increment = None
    StaggerLineHeight1 = None
    StaggerLineHeight2 = None
    def Create(self):
        """
        Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId, increment: System.Double) -> Autodesk.Civil.DatabaseServices.ProfileStationLabelGroup.
            Creates a new instance of a ProfileStationLabelGroup on the profile in the specified ProfileView with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label group is located.
            profileId: ObjectId - The ObjectId of profile in which the label group is located.
            styleId: ObjectId - The ObjectId of ProfileStationLabelGroup style.
            increment: System.Double - The increment value at which to insert major and minor station labels.
        """
        pass
    
    
    def CreateMajor(self):
        """
        CreateMajor(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId, increment: System.Double) -> ObjectId
            Creates a new instance of a ProfileStationLabelGroup on the Profile in the specified ProfileView with the specified label style.
            profileViewId: ObjectId - The ObjectId of the ProfileView in which the label group is located.
            profileId: ObjectId - The ObjectId of the Profile in which the label group is located.
            styleId: ObjectId - The ObjectId of the ProfileStationLabelGroup style to use.
            increment: System.Double - The increment value at which to insert major and minor station labels.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfileStationLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
            profileId: ObjectId - The ObjectId of the Profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileStationLabelGroup.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ProfileStationLabelGroup objects on the Profile in the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            profileId: ObjectId - The objectId of the profile where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of ProfileStationLabelGroup.
        """
        pass
    
    pass

class ProfileTangent(ProfileEntity):
    """
    This class represents an ProfileEntity made up of a single tangent.
    """
    EntityType = None
    Grade = None
    ThroughPoint1Elevation = None
    ThroughPoint1Station = None
    ThroughPoint2Elevation = None
    ThroughPoint2Station = None

    pass

class ProfileType():
    """
    Defines the profile type.
    """
    pass

class ProfileUpdateType():
    """
    Defines the profile's update mode.
    """
    pass

class ProfileView(Entity):
    """
    Manages the graphic display of profile data objects within a drawing. 
    A ProfileView is used to display one or more profiles for a horizontal alignment. 
    You can configure data bands and profile annotations in a ProfileView to make it clearer or more informative for the user.
    """
    AlignmentId = None
    AlignmentName = None
    Bands = None
    ElevationMax = None
    ElevationMin = None
    ElevationRangeMode = None
    GraphOverrides = None
    HatchAreas = None
    PipeOverrides = None
    SplitDataLines = None
    SplitDatumRounding = None
    SplitHeight = None
    SplitProfileView = None
    SplitStationMode = None
    SplitStationRounding = None
    StationEnd = None
    StationRangeMode = None
    StationStart = None
    StructureOverrides = None
    StyleId = None
    StyleName = None
    def Create(self):
        """
        Create(alignmentId: ObjectId, insertPosition: Point3d) -> ObjectId
            Creates a ProfileView from the specified alignment with the default ProfileView name and BandSetStyle.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
        Create(alignmentId: ObjectId, insertPosition: Point3d, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions) -> SplitProfileViewCreationOptions
            Creates a split ProfileView from the specified alignment with the default ProfileView name and BandSetStyle.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - The class including datas for split profileView options.
        Create(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions) -> StackedProfileViewsCreationOptions
            Creates stacked ProfileViews from the specified alignment with the default ProfileView name and BandSetStyle.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating the stacked profileViews.
        Create(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions) -> StackedProfileViewsCreationOptions
            Creates stacked split ProfileViews from the specified alignment with the default ProfileView name and BandSetStyle.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating the stacked profileViews.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - An object containing additional options for creating the split profileViews.
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId) -> ObjectId
            Creates a ProfileView from the specified alignment.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name of the stacked ProfileViews.
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet to import to the ProfileView.
            profileViewStyleId: ObjectId - The ObjectId of the ProfileView style.
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions) -> StackedProfileViewsCreationOptions
            Creates stacked ProfileViews from the specified alignment.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name of the stacked ProfileViews. 
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet to import to stacked ProfileViews. 
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating the stacked profileViews.
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, profileViewName: System.String, profileViewBandSetId: ObjectId, alignmentId: ObjectId, insertPosition: Point3d) -> CivilDocument
            Creates a profile view from the specified alignment.
            Remarks: The ProfileView feature settings are used to get the profileView style, profile labelset and other information, and the profile view is created on the Layer "0" by default.
            document: Autodesk.Civil.ApplicationServices.CivilDocument -  Document object in which the ProfileView is created.
            profileViewName: System.String -  Name of the created ProfileView. 
            profileViewBandSetId: ObjectId -  Object id of the profile view band set to import to profile view. 
            alignmentId: ObjectId -  Object id of the alignment. 
            insertPosition: Point3d -  Position at which the ProfileView is inserted. 
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, profileViewName: System.String, profileViewBandSetName: System.String, alignmentName: System.String, insertPosition: Point3d) -> CivilDocument
            Creates a profile view from the specified alignment.
            Remarks: We use the ProfileView feature settings to get the profileView style, profile labelset and other information, and put the profile view on the Layer "0" by default.
            document: Autodesk.Civil.ApplicationServices.CivilDocument -  Document object in which the ProfileView is created.
            profileViewName: System.String -  Name of the created ProfileView. 
            profileViewBandSetName: System.String -  Name of the profile view band set to import to profile view. 
            alignmentName: System.String -  Name of the alignment. 
            insertPosition: Point3d -  Position at which the ProfileView is inserted. 
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions) -> SplitProfileViewCreationOptions
            Creates a split ProfileView from the specified alignment.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name of the split ProfileView.
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet to import to the ProfileView.
            profileViewStyleId: ObjectId - The ObjectId of the ProfileView style.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - An object containing additional options for creating the split profileView.
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions) -> StackedProfileViewsCreationOptions
            Creates stacked split ProfileViews from the specified alignment.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name of the stacked split ProfileViews. 
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet to import to stacked ProfileViews. 
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating the stacked profileViews.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - An object containing additional options for creating the split profileViews.
        """
        pass
    
    
    def CreateMultiple(self):
        """
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions) -> MultipleProfileViewsCreationOptions
            Creates multiple ProfileViews from the alignment with the default ProfileViewStyle and ProfileViewBandSet.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions) -> StackedProfileViewsCreationOptions
            Creates multiple stacked ProfileViews for an alignment with the default ProfileViewBandSet.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating stacked ProfileViews.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions, datumType: Autodesk.Civil.ProfileViewDatumType) -> MultipleProfileViewsCreationOptions
            Creates multiple split ProfileViews from the alignment with the default ProfileViewStyle and ProfileViewBandSet.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - An object containing additional options for creating split ProfileViews.
            datumType: Autodesk.Civil.ProfileViewDatumType - Specifies profile view datum (location of profile lines).
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions, datumType: Autodesk.Civil.ProfileViewDatumType) -> StackedProfileViewsCreationOptions
            Creates multiple stacked split ProfileViews for an alignment with the default ProfileViewBandSet.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating stacked ProfileViews.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - An object containing additional options for creating split ProfileViews.
            datumType: Autodesk.Civil.ProfileViewDatumType - Specifies profile view datum (location of profile lines).
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions) -> MultipleProfileViewsCreationOptions
            Creates multiple ProfileViews from the alignment with the specified ProfileViewStyle and ProfileViewBandSet.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name template of the ProfileViews.
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet.
            profileViewStyleId: ObjectId - The ObjectId of the ProfileViewStyle.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions) -> StackedProfileViewsCreationOptions
            Creates multiple stacked ProfileViews for an alignment.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name template for the ProfileViews.
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet to import to the stacked ProfileViews. 
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating stacked ProfileViews.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions, datumType: Autodesk.Civil.ProfileViewDatumType) -> MultipleProfileViewsCreationOptions
            Creates multiple split ProfileViews from an alignment with the specified ProfileViewStyle and ProfileViewBandSet.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name template of the ProfileViews.
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet.
            profileViewStyleId: ObjectId - The ObjectId of the ProfileViewStyle.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - An object containing additional options for creating split ProfileViews.
            datumType: Autodesk.Civil.ProfileViewDatumType - Specifies profile view datum (location of profile lines).
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: System.String, profileViewBandSetId: ObjectId, stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions, multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions, splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions, datumType: Autodesk.Civil.ProfileViewDatumType) -> StackedProfileViewsCreationOptions
            Creates multiple stacked split ProfileViews for an alignment.
            alignmentId: ObjectId - The ObjectId of the alignment.
            insertPosition: Point3d - The position at which the ProfileView is inserted.
            profileViewName: System.String - The name template for the ProfileViews.
            profileViewBandSetId: ObjectId - The ObjectId of the ProfileViewBandSet to import to the stacked ProfileViews. 
            stackedOptions: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions - An object containing additional options for creating stacked ProfileViews.
            multipleOptions: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions - An object containing additional options for creating multiple ProfileViews.
            splitOptions: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions - An object containing additional options for creating split ProfileViews.
            datumType: Autodesk.Civil.ProfileViewDatumType - Specifies profile view datum (location of profile lines).
        """
        pass
    
    
    def FindStationAndElevationAtXY(self):
        """
        FindStationAndElevationAtXY(x: System.Double, y: System.Double, station: System.Double, elevation: System.Double) -> bool
            Finds the station and elevation values at the given X,Y coordinate.
            x: System.Double - The X coordinate in the profile view's coordinate system. 
            y: System.Double - The  Y coordinate in the profile view's coordinate system. 
            station: System.Double -  Returns the corresponding station. 
            elevation: System.Double -  Returns the corresponding elevation. 
        """
        pass
    
    
    def FindXYAtStationAndElevation(self):
        """
        FindXYAtStationAndElevation(station: System.Double, elevation: System.Double, x: System.Double, y: System.Double) -> bool
            Finds the X,Y coordinate for the given station and elevation.
            station: System.Double -  Station value along the parent alignment. 
            elevation: System.Double -  Elevation value along the parent alignment. 
            x: System.Double -  Returns the x value in the profile view's coordinate system. 
            y: System.Double -  Returns the y value in the profile view's coordinate system. 
        """
        pass
    
    
    def GetAvailablePipeProfileLabelIds(self):
        """
        GetAvailablePipeProfileLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the PipeProfileLabels.
        """
        pass
    
    
    def GetAvailableSpanningPipeProfileLabelIds(self):
        """
        GetAvailableSpanningPipeProfileLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the SpanningPipeProfileLabels.
        """
        pass
    
    
    def GetAvailableStructureProfileLabelIds(self):
        """
        GetAvailableStructureProfileLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the StructureProfileLabels.
        """
        pass
    
    
    def GetLabelIds(self):
        """
        GetLabelIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the ProfileView's labels.
        """
        pass
    
    
    def GetProfileViewLabelIds(self):
        """
        GetProfileViewLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the ProfileView's labels.
        """
        pass
    
    pass

class ProfileViewBandItem(BandSetItem):
    """
    This class represents a single profile view data band.
    """
    AlignmentId = None
    DataSourceId = None
    MaterialName = None
    Profile1Id = None
    Profile2Id = None

    pass

class ProfileViewBandItemCollection(BandSetItemCollection):
    """
    This class represents a collection that stores all the band items for a ProfileView object.
    """
    Item = None
    def Add(self):
        """
        Add(bandType: Autodesk.Civil.BandType, profileBandStyleName: System.String) -> BandType
            Creates a new profile view band item with the given band type and name, adds it to the collection.
            bandType: Autodesk.Civil.BandType - The profile band type, only ProfileData, HorizontalGeometry, VerticalGeometry, Superelevation, ProfileViewPipeNetwork and ProfileViewSectionalData are valid here.
            profileBandStyleName: System.String - The profile band name.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileViewBandItem
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

class ProfileViewBandSet(GraphBandSet):
    """
    This class represents the band collection in a ProfileView.
    """

    def GetBottomBandItems(self):
        """
        GetBottomBandItems() -> ProfileViewBandItemCollection
            Gets the bottom band items collection from the ProfileView.
        """
        pass
    
    
    def GetTopBandItems(self):
        """
        GetTopBandItems() -> ProfileViewBandItemCollection
            Gets the top band items collection from the ProfileView.
        """
        pass
    
    
    def SetBottomBandItems(self):
        """
        SetBottomBandItems(bandItems: Autodesk.Civil.DatabaseServices.ProfileViewBandItemCollection) -> ProfileViewBandItemCollection
            Sets the bottom band items to the ProfileView.
            bandItems: Autodesk.Civil.DatabaseServices.ProfileViewBandItemCollection
        """
        pass
    
    
    def SetTopBandItems(self):
        """
        SetTopBandItems(bandItems: Autodesk.Civil.DatabaseServices.ProfileViewBandItemCollection) -> ProfileViewBandItemCollection
            Sets the top band items to the ProfileView.
            bandItems: Autodesk.Civil.DatabaseServices.ProfileViewBandItemCollection
        """
        pass
    
    pass

class ProfileViewDepthLabel(Entity):
    """
    This class represents a profile view depth label.
    """
    EndPoint = None
    StartPoint = None
    def Create(self):
        """
        Create(profileViewId: ObjectId, labelStyleId: ObjectId, startPoint: Point2d, endPoint: Point2d) -> ObjectId
            Creates a new instance of ProfileViewDepthLabel on the profile view with the specified label style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label is located.
            labelStyleId: ObjectId - The ObjectId of ProfileViewDepthLabel style.
            startPoint: Point2d - The start point at which to insert ProfileViewDepthLabel.
            endPoint: Point2d - The end point at which to insert ProfileViewDepthLabel.
        """
        pass
    
    pass

class ProfileViewPart(Entity):
    """
    Manages the graphic display of pipe network parts in profile view.
    """
    ModelPartId = None
    def GetLabelIds(self):
        """
        GetLabelIds() -> ObjectIdCollection
            Gets the object ids of the labels attached to this profile network part
            Remarks: TODO: OBJECTID TYPE: Autodesk.Civil.DatabaseServices.Styles.LabelStyle
        """
        pass
    
    
    def GetPartProfileLabelIds(self):
        """
        GetPartProfileLabelIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the labels attached to this profile network part
        """
        pass
    
    pass

class ProfileViewSplitData(object):
    """
    This class represents a split location.
    """
    AdjustedDatum = None
    ProfileViewStyleId = None
    ProfileViewStyleName = None
    SplitStation = None
    pass

class ProfileViewSplitDataCollection(object):
    """
    The class provides a collection for the profile view split data.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(rawStation: System.Double, datum: System.Double) -> ProfileViewSplitData
            Adds a new split location.
            rawStation: System.Double -  Specifies the station of the split location. 
            datum: System.Double -  Specifies the elevation of the split location.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> ProfileViewSplitData
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
            Removes the split location from the collection.
            index: System.Int32 -  Specifies the item index to remove. 
        """
        pass
    
    pass

class QTOCriteriaNameMapping(object):
    """
    This class defines a utility class for mapping surface and shape when import criteria to QTOMaterialListCollection.
    """
    isMappingCompleted = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOCriteriaNameMapping
        """
        pass
    
    
    def GetMappedCorridorShape(self):
        """
        GetMappedCorridorShape(materialName: System.String, shapeName: System.String, mappedCorridorId: ObjectId, mappedShapeName: System.String)
            Get corridor shape which was mapped to the shape name of a material in the criteria.
            materialName: System.String - Specifies the material name that is referenced by the corresponding corridor shape in the list.
            shapeName: System.String - Specifies the shape name that is used in the criteria.
            mappedCorridorId: ObjectId - The ObjectId of mapped corridor.
            mappedShapeName: System.String - The mapped shape name.
        """
        pass
    
    
    def GetMappedSurfaceId(self):
        """
        GetMappedSurfaceId(materialName: System.String, surfaceName: System.String) -> ObjectId
            Get an ObjectId of Surface which is mapped to the surface name of a material in the criteria.
            materialName: System.String - Specifies the material name that is referenced by the corresponding surface in the list.
            surfaceName: System.String - Specifies the surface name that is used in the criteria.
        """
        pass
    
    
    def MapCorridorShape(self):
        """
        MapCorridorShape(shapeName: System.String, mappedCorridorId: ObjectId, mappedShapeName: System.String)
            Specifies an actual corridor shape to map to all shape with specified name in the criteria.
            shapeName: System.String - Specifies the shape name that is used in the criteria.
            mappedCorridorId: ObjectId - Specifies the ObjectId of an actual corridor.
            mappedShapeName: System.String - Specifies the shape name of mapped corridor to map to the shape name in the criteria.
        MapCorridorShape(materialName: System.String, shapeName: System.String, mappedCorridorId: ObjectId, mappedShapeName: System.String)
            Specifies an actual corridor shape to map to the shape name of a material in the criteria.
            materialName: System.String - Specifies the material name that is referenced by the corresponding corridor shape in the list.
            shapeName: System.String - Specifies the shape name that is used in the criteria.
            mappedCorridorId: ObjectId - Specifies the ObjectId of an actual corridor.
            mappedShapeName: System.String - Specifies the shape name of mapped corridor to map to the shape name in the criteria.
        """
        pass
    
    
    def MapSurface(self):
        """
        MapSurface(surfaceName: System.String, mappedSurfaceId: ObjectId)
            Specifies an actual surface to map to all surface with specified name in the criteria.
            surfaceName: System.String - Specifies the surface name that is used in the criteria.
            mappedSurfaceId: ObjectId - Specifies the ObjectId of an actual surface to map to the surface name in the criteria.
        MapSurface(materialName: System.String, surfaceName: System.String, mappedSurfaceId: ObjectId)
            Specifies an actual surface to map to the surface name of a material in the criteria.
            materialName: System.String - Specifies the material name that is referenced by the corresponding surface in the list.
            surfaceName: System.String - Specifies the surface name that is used in the criteria.
            mappedSurfaceId: ObjectId - Specifies the ObjectId of an actual surface to map to the surface name in the criteria.
        """
        pass
    
    pass

class QTOMaterial(object):
    """
    This class defines the QTO material of sample line group
    """
    Count = None
    Guid = None
    IsSubcriteriaSupported = None
    Item = None
    MaterialGaps = None
    MaterialListGuid = None
    Name = None
    QuantityType = None
    SampleLineGroupId = None
    ShapeStyleId = None
    Subcriteria = None
    def Add(self):
        """
        Add(surfaceId: ObjectId) -> QTOMaterialItem
            Adds a material item with the sampled surface to the material.
            Remarks: The sampled surface should be Autodesk.Civil.DatabaseServices.TinSurface or Autodesk.Civil.DatabaseServices.GridSurface.A new material item is added to the first sub criteria if it exists.
            surfaceId: ObjectId - The ObjectId of the sampled surface added as material item.
        Add(corridorId: ObjectId, shapeCode: System.String) -> QTOMaterialItem
            Adds a material item with the sampled corridor shape to the material.
            Remarks: The sampled corridor should be Autodesk.Civil.DatabaseServices.Corridor.
            corridorId: ObjectId - The ObjectId of the sampled corridor.
            shapeCode: System.String - A shape code of the sampled corridor.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOMaterial
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> QTOMaterialItem
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetFactor(self):
        """
        GetFactor(type: Autodesk.Civil.DatabaseServices.MaterialFactorType) -> MaterialFactorType
            Gets the factor value.
            type: Autodesk.Civil.DatabaseServices.MaterialFactorType
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def IsFactorApplicable(self):
        """
        IsFactorApplicable(type: Autodesk.Civil.DatabaseServices.MaterialFactorType) -> MaterialFactorType
            Gets a boolean value indicating whether the specified factor is applicable.
            Remarks: Cut factor is not applicable when MaterialQuantityType is Fill or Structure.Fill factor is not applicable when MaterialQuantityType is Cut.Refill factor is not applicable when MaterialQuantityType is Fill or Structure.
            type: Autodesk.Civil.DatabaseServices.MaterialFactorType
        """
        pass
    
    
    def Remove(self):
        """
        Remove(name: System.String) -> bool
            Removes a material item specified by name from the material.
            Remarks: The first material item with the specified name is removed when sub criteria exist.
            name: System.String - The name of the material item to be removed.
        Remove(materialItem: Autodesk.Civil.DatabaseServices.QTOMaterialItem) -> QTOMaterialItem
            Removes a material item from the material.
            materialItem: Autodesk.Civil.DatabaseServices.QTOMaterialItem - The material item to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a material item specified by index from the material.
            index: System.Int32 - The index of the material item to be removed.
        """
        pass
    
    
    def SetFactor(self):
        """
        SetFactor(type: Autodesk.Civil.DatabaseServices.MaterialFactorType, newValue: System.Double) -> MaterialFactorType
            Sets the factor value.
            type: Autodesk.Civil.DatabaseServices.MaterialFactorType
            newValue: System.Double
        """
        pass
    
    pass

class QTOMaterialGap(object):
    """
    This class defines QTO material gap.
    """
    Applied = None
    Description = None
    EndStation = None
    RunInDistance = None
    RunOutDistance = None
    StartStation = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOMaterialGap
        """
        pass
    
    pass

class QTOMaterialGapCollection(object):
    """
    This class defines the collection of QTO material gap.
    """
    Count = None
    Item = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOMaterialGapCollection
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> QTOMaterialGap
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    pass

class QTOMaterialItem(object):
    """
    This class defines material data used to define material of sample line group.
    """
    Condition = None
    MaterialGuid = None
    MaterialListGuid = None
    Name = None
    SampleLineGroupId = None
    Type = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOMaterialItem
        """
        pass
    
    
    def IsConditionApplicable(self):
        """
        IsConditionApplicable(conditionType: Autodesk.Civil.DatabaseServices.MaterialConditionType) -> MaterialConditionType
            Gets a boolean value indicating whether the specified condition type is applicable.
            Remarks: Above and Below is applicable when MaterialItemType is Surface and MaterialQuantityType is Cut, Fill, CutFill or Structure.Base and Compare is applicable when MaterialItemType is Surface and MaterialQuantityType is Earthwork.Include is applicable when MaterialItemType is CorridorShape and MaterialQuantityType is Structure.
            conditionType: Autodesk.Civil.DatabaseServices.MaterialConditionType
        """
        pass
    
    pass

class QTOMaterialList(object):
    """
    This class defines the QTO material list of sample line group
    """
    Count = None
    CurveCorrectionTolerance = None
    Guid = None
    IsCurveCorrectionEnabled = None
    Item = None
    MaterialListGaps = None
    Name = None
    SampleLineGroupId = None
    def Add(self):
        """
        Add(materialName: System.String) -> QTOMaterial
            Adds an empty material with the specified name to the material list.
            materialName: System.String - The name of the material to be created.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOMaterialList
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> QTOMaterial
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(guid: System.Guid) -> bool
            Removes a material specified by GUID from the material list.
            guid: System.Guid - The GUID of the material to be removed.
        Remove(name: System.String) -> bool
            Removes a material specified by name from the material list.
            name: System.String - The name of the material to be removed.
        Remove(material: Autodesk.Civil.DatabaseServices.QTOMaterial) -> QTOMaterial
            Removes a material from the material list.
            material: Autodesk.Civil.DatabaseServices.QTOMaterial - The material object to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a material specified by index from the material list.
            index: System.Int32 - Index of the material to be removed.
        """
        pass
    
    pass

class QTOMaterialListCollection(object):
    """
    This class defines the collection of QTO material lists of sample line group.
    """
    Count = None
    Item = None
    VolumeCalculationMethodType = None
    def Add(self):
        """
        Add(materialListName: System.String) -> QTOMaterialList
            Add an empty material list with the specified name.
            materialListName: System.String - The name of the material list to be created.
        """
        pass
    
    
    def Fix(self):
        """
        Fix(methodType: Autodesk.Civil.DatabaseServices.MaterialVolumeCalculationMethodType) -> MaterialVolumeCalculationMethodType
            Fixes material lists for the specified volume calculation method.
            methodType: Autodesk.Civil.DatabaseServices.MaterialVolumeCalculationMethodType - The volume calculation method.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> QTOMaterialList
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def ImportCriteria(self):
        """
        ImportCriteria(criteriaNameMapping: Autodesk.Civil.DatabaseServices.QTOCriteriaNameMapping) -> QTOMaterialList
            Imports a new QTOMaterialList based on a QuantityTakeoffCriteria.
            Remarks: An instance of QTOCreiteriaNameMapping class should be created with ObjectId of QuantityTakeoffCriteria and be mapped with all the names.
            criteriaNameMapping: Autodesk.Civil.DatabaseServices.QTOCriteriaNameMapping - An instance of QTOCriteriaNameMapping which has been set to map all name on a QuantityTakeoffCriteria.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(guid: System.Guid) -> bool
            Removes a material list specified by GUID from the collection.
            guid: System.Guid - The GUID of the material list to be removed.
        Remove(name: System.String) -> bool
            Removes a material list specified by name from the collection.
            name: System.String - The name of the material list to be removed.
        Remove(materialList: Autodesk.Civil.DatabaseServices.QTOMaterialList) -> QTOMaterialList
            Removes a material list from the collection.
            materialList: Autodesk.Civil.DatabaseServices.QTOMaterialList - The material list to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a material list specified by index from the collection.
            index: System.Int32 - Index of material list to be removed.
        """
        pass
    
    
    def Validate(self):
        """
        Validate(methodType: Autodesk.Civil.DatabaseServices.MaterialVolumeCalculationMethodType) -> MaterialVolumeCalculationMethodType
            Validates material lists for the specified volume calculation method.
            methodType: Autodesk.Civil.DatabaseServices.MaterialVolumeCalculationMethodType - The volume calculation method.
        """
        pass
    
    pass

class QTOMaterialListGap(object):
    """
    This class defines the QTO material list gap.
    """
    Description = None
    EndStation = None
    StartStation = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOMaterialListGap
        """
        pass
    
    pass

class QTOMaterialListGapCollection(object):
    """
    This class defines the collection of QTO material list gap.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(startStation: System.Double, endStation: System.Double) -> QTOMaterialListGap
            Add a material list gap.
            startStation: System.Double
            endStation: System.Double
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOMaterialListGapCollection
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> QTOMaterialListGap
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(materialListGap: Autodesk.Civil.DatabaseServices.QTOMaterialListGap) -> QTOMaterialListGap
            Removes a material list gap from the collection.
            materialListGap: Autodesk.Civil.DatabaseServices.QTOMaterialListGap
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a material list gap specified by index from the collection.
            index: System.Int32
        """
        pass
    
    pass

class QTOSubcriteria(object):
    """
    This class defines sub criteria used to define QTO material.
    """
    Count = None
    Item = None
    MaterialGuid = None
    MaterialListGuid = None
    Name = None
    SampleLineGroupId = None
    def Add(self):
        """
        Add(surfaceId: ObjectId) -> QTOMaterialItem
            Adds a material item with the sampled surface to the sub criteria.
            Remarks: The sampled surface should be Autodesk.Civil.DatabaseServices.TinSurface or Autodesk.Civil.DatabaseServices.GridSurface.
            surfaceId: ObjectId - The ObjectId of the sampled surface added as material item.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOSubcriteria
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> QTOMaterialItem
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(name: System.String) -> bool
            Removes a material item specified by name from the sub criteria.
            name: System.String - The name of the material item to be removed.
        Remove(materialItem: Autodesk.Civil.DatabaseServices.QTOMaterialItem) -> QTOMaterialItem
            Removes a material item from the sub criteria.
            materialItem: Autodesk.Civil.DatabaseServices.QTOMaterialItem - The material item to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a material item specified by index from the sub criteria.
            index: System.Int32 - The index of the material item to be removed.
        """
        pass
    
    pass

class QTOSubcriteriaCollection(object):
    """
    This class defines collection of sub criteria.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(subcriteriaName: System.String) -> QTOSubcriteria
            Adds an empty sub criteria with the specified name to the collection.
            subcriteriaName: System.String - The name of the sub criteria to be created.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the QTOSubcriteriaCollection
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> QTOSubcriteria
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(subcriteria: Autodesk.Civil.DatabaseServices.QTOSubcriteria) -> QTOSubcriteria
            Removes a sub criteria from the collection.
            subcriteria: Autodesk.Civil.DatabaseServices.QTOSubcriteria - The sub criteria to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a sub criteria specified by index from the collection.
            index: System.Int32 - Index of the material to be removed.
        """
        pass
    
    pass

class QTOUtility(object):
    """
    
    """
    def AddPayItemId(self):
        """
        AddPayItemId(oid: ObjectId, payItemID: System.String)
            Adds a pay item id.
            oid: ObjectId - Object id of the object to which add the pay item.
            payItemID: System.String - Pay item id to add.
        """
        pass
    
    
    def DeleteAllPayItemsIds(self):
        """
        DeleteAllPayItemsIds(oid: ObjectId)
            Deletes all pay item information from the specified object.
            oid: ObjectId - Object id of the object from which delete all the pay item information.
        """
        pass
    
    
    def DeletePayItemIds(self):
        """
        DeletePayItemIds(oid: ObjectId, payItemIDs: System.Collections.Specialized.StringCollection)
            Deletes the pay item ids in the collection from the specified object.
            oid: ObjectId - Object id of the object from which to delete the pay items.
            payItemIDs: System.Collections.Specialized.StringCollection - StringCollection containing the pay item ids to delete.
        """
        pass
    
    
    def GetPayItemIds(self):
        """
        GetPayItemIds(oid: ObjectId) -> StringCollection
            Gets a string collection of pay items ids for the specified object.
            oid: ObjectId - Object id for the object from which retrieve the pay item ids.
        """
        pass
    
    
    def OpenPayItemFile(self):
        """
        OpenPayItemFile(fileFormat: Autodesk.Civil.DatabaseServices.PayItemFileFormat, strPayItemFilePath: System.String, strPayItemCategorizationFilePath: System.String) -> PayItemFileFormat
            Open pay item files with specified format and file path.
            fileFormat: Autodesk.Civil.DatabaseServices.PayItemFileFormat - Pay item file format.
            strPayItemFilePath: System.String - Pay item file path.
            strPayItemCategorizationFilePath: System.String - Pay item categorization file path.
        """
        pass
    
    pass

class RailAlignmentInfo(object):
    """
    This class encapsulates the properties and operations of a rail alignment object.
    """
    TrackWidth = None
    def GetCantInfoAtStation(self):
        """
        GetCantInfoAtStation(station: System.Double) -> RailCANTInfo
            Gets the cant information at a specified station.
            station: System.Double - The station on the alignment at which to get rail cant information.
        """
        pass
    
    pass

class RailCANTInfo():
    """
    This class encapuslates cant (superelevation) informations for rail alignments.
    """
    AppliedCANT = None
    LeftRailElevationDifference = None
    Pivot = None
    RightRailElevationDifference = None
    pass

class RegionMatchType():
    """
    Specifies the way to match between two BaselineRegion.
    """
    pass

class SCSCSConstraints(object):
    """
    The SCSCSConstraints class.  This class defines contraints for creating
    Spiral-Curve-Spiral-Curve-Spiral (AlignmentSCSCS) compound Alignment entities.
    """
    def CreateByArc1Angle(self):
        """
        CreateByArc1Angle(arc1Angle: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by the angle of the first arc.
            arc1Angle: System.Double - The angle of the first arc.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc1Length(self):
        """
        CreateByArc1Length(arc1Len: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by the length of the first arc.
            arc1Len: System.Double - The length of the first arc.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc1PassPt(self):
        """
        CreateByArc1PassPt(ptArc1PassThru: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by a pass-through point for the first arc.
            ptArc1PassThru: Point2d - The pass-through point for the first arc.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc2Angle(self):
        """
        CreateByArc2Angle(arc2Angle: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by an end point.
            arc2Angle: System.Double - The angle of arc2.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc2Length(self):
        """
        CreateByArc2Length(arc2Len: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by the second arc length.
            arc2Len: System.Double - The second arc length.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc2PassPt(self):
        """
        CreateByArc2PassPt(ptArc2PassThru: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by the second arc pass through point.
            ptArc2PassThru: Point2d - The second arc pass through point.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByEndPoint(self):
        """
        CreateByEndPoint(endPoint: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by an end point.
            endPoint: Point2d - The end point.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByStartPoint(self):
        """
        CreateByStartPoint(startPoint: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by the start point.
            startPoint: Point2d - The start point.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByTan1Length(self):
        """
        CreateByTan1Length(extTan1Len: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by the first tangent length.
            extTan1Len: System.Double - The first tangent length.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByTan2Length(self):
        """
        CreateByTan2Length(extTan2Len: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, arc2Radius: System.Double, sp3Param: System.Double, isParamAValue: System.Boolean) -> SCSCSConstraints
            Creates an SCSCSConstraints object that constrains the SCSCS group by the length of the second tangent.
            extTan2Len: System.Double - The length of the second tangent.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    pass

class SCSSCSConstraints(object):
    """
    The SCSSCSConstraints class. This class defines contraints
    for creating Spiral-Curve-Spiral-Spiral-Curve-Spiral
    (AlignmentSCSSCS) compound Alignment entities.
    """
    def CreateByArc1Angle(self):
        """
        CreateByArc1Angle(arc1Angle: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the angle of the first arc.
            arc1Angle: System.Double - The angle of the first arc.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc1Length(self):
        """
        CreateByArc1Length(arc1Len: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the length of the first arc.
            arc1Len: System.Double - The length of the first arc.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc1PassPt(self):
        """
        CreateByArc1PassPt(ptArc1PassThru: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the pass-through point of the first arc.
            ptArc1PassThru: Point2d - The pass-through point of the first arc.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc2Angle(self):
        """
        CreateByArc2Angle(arc2Angle: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the second arc angle.
            arc2Angle: System.Double - The second arc angle.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc2Length(self):
        """
        CreateByArc2Length(arc2Len: System.Double, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the second arc length.
            arc2Len: System.Double - The second arc length.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByArc2PassPt(self):
        """
        CreateByArc2PassPt(ptArc2PassThru: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the pass-through point for the second arc.
            ptArc2PassThru: Point2d - The pass-through point for the second arc.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByEndPoint(self):
        """
        CreateByEndPoint(endPoint: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the end point.
            endPoint: Point2d - The end point.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    
    def CreateByStartPoint(self):
        """
        CreateByStartPoint(startPoint: Point2d, sp1Param: System.Double, arc1Radius: System.Double, sp2Param: System.Double, sp3Param: System.Double, arc2Radius: System.Double, sp4Param: System.Double, isParamAValue: System.Boolean) -> SCSSCSConstraints
            Creates an SCSSCSConstraints object that constrains the SCSSCS group by the start point.
            startPoint: Point2d - The start point.
            sp1Param: System.Double - The first spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc1Radius: System.Double - The radius of the first arc.
            sp2Param: System.Double - The second spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            sp3Param: System.Double - The third spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            arc2Radius: System.Double - The radius of the second arc.
            sp4Param: System.Double - The fourth spiral value.  If isParamAValue is true, this is the spiral A value. If isParamAValue is false, this is the spiral length.
            isParamAValue: System.Boolean - Indicates whether the sp_Param parameters are A values (true) or lengths (false).
        """
        pass
    
    pass

class SECurve(CANTCurve):
    """
    This class represents a super elevation curve object and contains a collection of critical stations for that curve.
    """
    CANTCriticalStations = None
    CriticalStations = None
    EndStation = None
    Name = None
    ParentAlignmentId = None
    StartStation = None
    pass

class SampleLine(Entity):
    """
    Lines used for obtaining elevational information from an existing terrain model or surface for creating profiles and cross sections.
    """
    GroupId = None
    LockToStation = None
    Number = None
    Station = None
    StyleId = None
    StyleName = None
    Vertices = None
    def Create(self):
        """
        Create(sampleLineName: System.String, sampleLineGroupId: ObjectId, points: Point2dCollection) -> ObjectId
            Creates a new sample line with specified vertex points.
            Remarks: Besides the specified vertex points, the created sample line has one more vertex, which is the intersection point with the alignment.
            sampleLineName: System.String - The name of the newly created sample line.
            sampleLineGroupId: ObjectId - The ObjectId of the sample line group to which the newly created sample line is added.
            points: Point2dCollection - The points used as the vertex of the newly created sample line.
        Create(sampleLineName: System.String, sampleLineGroupId: ObjectId, station: System.Double) -> ObjectId
            Creates a new sample line at a specified station.
            sampleLineName: System.String - The name of the newly created sample line.
            sampleLineGroupId: ObjectId - The ObjectId of the sample line group to which the newly created sample line is added.
            station: System.Double - The station at which the sample line is created.
        """
        pass
    
    
    def GetMaterialSectionId(self):
        """
        GetMaterialSectionId(materialListGuid: System.Guid, materialGuid: System.Guid) -> ObjectId
            Gets MaterialSection objectId by MaterialList GUID and Material GUID.
            Remarks: The method will return ObjectId.Null if the specified MaterialSection does not exist.
            materialListGuid: System.Guid - The GUID of materialList.
            materialGuid: System.Guid - The GUID of material.
        """
        pass
    
    
    def GetSectionId(self):
        """
        GetSectionId(sampledSourceId: ObjectId) -> ObjectId
            Gets section objectId generated from the specified source.
            sampledSourceId: ObjectId
        """
        pass
    
    
    def GetSectionIds(self):
        """
        GetSectionIds() -> ObjectIdCollection
            Gets the objectId collection of all sections attached on this sample line.
        """
        pass
    
    
    def GetSectionViewIds(self):
        """
        GetSectionViewIds() -> ObjectIdCollection
            Gets the objectId collection of all section views attached on this sample line.
        """
        pass
    
    pass

class SampleLineGroup(Entity):
    """
    Controls a set of related sample lines, the surfaces they sample, and methods for creating cross sections.
    """
    DefaultSamplineLabelStyleId = None
    DefaultSamplineStyleId = None
    IndividualSectionViewGroup = None
    MaterialLists = None
    SectionViewGroups = None
    def Create(self):
        """
        Create(groupName: System.String, alignmentId: ObjectId) -> ObjectId
            Creates a sample line group.
            groupName: System.String - The name of sample line group to be created.
            alignmentId: ObjectId - The ObjectId of alignment.
        """
        pass
    
    
    def GetAvailableSampleLineLabelGroupIds(self):
        """
        GetAvailableSampleLineLabelGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the SampleLineLabelGroup.
        """
        pass
    
    
    def GetMappingGuid(self):
        """
        GetMappingGuid(mappingName: System.String) -> Guid
            mappingName: System.String
        """
        pass
    
    
    def GetMassHaulViewIds(self):
        """
        GetMassHaulViewIds() -> ObjectIdCollection
            Gets the objectId collection of mass haul views.
        """
        pass
    
    
    def GetMaterialGuid(self):
        """
        GetMaterialGuid(mappingGuid: System.Guid, materialName: System.String) -> Guid
            mappingGuid: System.Guid
            materialName: System.String
        """
        pass
    
    
    def GetMaterialNamesInMapping(self):
        """
        GetMaterialNamesInMapping(mappingGuid: System.Guid) -> string[]
            mappingGuid: System.Guid
        """
        pass
    
    
    def GetMaterialSectionSources(self):
        """
        GetMaterialSectionSources() -> MaterialSectionSourceCollection
            Gets the collection of material sources.
        """
        pass
    
    
    def GetQTOMappingNames(self):
        """
        GetQTOMappingNames() -> string[]
        """
        pass
    
    
    def GetSampleLineIds(self):
        """
        GetSampleLineIds() -> ObjectIdCollection
            Gets the objectId collection of all sample lines in the sample line group.
        GetSampleLineIds(station: System.Double, tolerance: System.Double) -> ObjectIdCollection
            Gets the ObjectId collection of sample lines at a specified station in the sample line group.
            station: System.Double - The station at which sample lines are got.
            tolerance: System.Double - The tolerance for the station value.
        """
        pass
    
    
    def GetSectionSources(self):
        """
        GetSectionSources() -> SectionSourceCollection
            Gets the collection of sources which could be sampled.
            Remarks: This method should be called on SampleLineGroup which is opened for write, because the collection of sources of SampleLineGroup will be updated and written into the SampleLineGroup before return to user.
        """
        pass
    
    
    def GetTotalVolumeResultDataForMaterialList(self):
        """
        GetTotalVolumeResultDataForMaterialList(mappingGuid: System.Guid) -> QuantityTakeoffResult
            mappingGuid: System.Guid
        """
        pass
    
    pass

class SampleLineLabelGroup(Entity):
    """
    This class represents a SampleLine label group.
    """

    def Create(self):
        """
        Create(sampleLineGroupId: ObjectId) -> ObjectId
            Creates a new instance of a SampleLineLabelGroup on the specified SampleLineGroup with the default label style.
            sampleLineGroupId: ObjectId - The ObjectId of the SampleLineGroup in which the label group is located.
        Create(sampleLineGroupId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SampleLineLabelGroup on the specified SampleLineGroup with the specified label style.
            sampleLineGroupId: ObjectId - The ObjectId of the SampleLineGroup where the label group is located.
            labelStyleId: ObjectId - The ObjectId of the SampleLineLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(sampleLineGroupId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all the available SampleLineLabelGroup objects in the specified SampleLineGroup.
            sampleLineGroupId: ObjectId - The ObjectId of the SampleLineGroup where the labelGroups are located.
        """
        pass
    
    pass

class SampleLineVertex(object):
    """
    Represents an SampleLineVertex object. An SampleLineVertex is a vertext point of an sample line.
    """
    Location = None
    OffsetIndex = None
    Side = None
    pass

class SampleLineVertexCollection(object):
    """
    The collection of vertex point of the sample line object.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SampleLineVertex
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    pass

class SampleLineVertexSideType():
    """
    Defines the sample line vertex side relative to the alignment.
    """
    pass

class SampledSectionLink(object):
    """
    Defines a single line segment of sample surface cross-section data.
    """
    EndPointElevation = None
    EndPointOffset = None
    EndPointStation = None
    StartPointElevation = None
    StartPointOffset = None
    StartPointStation = None
    pass

class SampledSectionLinkCollection(object):
    """
    Collection of sampled elevation data.
    """
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SampledSectionLink
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class Section(Entity):
    """
    Provides views created at a 90 degree angle to a surface or an alignment.
    """
    LeftOffset = None
    LeftSwathWidth = None
    MaximumElevation = None
    MinmumElevation = None
    ParentId = None
    RightOffset = None
    RightSwathWidth = None
    SampleLineId = None
    SectionPoints = None
    SourceType = None
    Station = None
    StyleId = None
    StyleName = None
    UpdateMode = None

    pass

class SectionBandLabelGroup(Entity):
    """
    This class is the base class for all section band-related group labels.
    """
    StyleId = None
    StyleName = None
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(bandLabelGroupClassType: System.Type, sectionViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of band label groups on the SectionView with a specified type.
            bandLabelGroupClassType: System.Type - The type of the band label group class.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the band label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of bandLabelGroupClassType.
        """
        pass
    
    pass

class SectionDataBandLabelGroup(Entity):
    """
    This class represents a section data band label group.
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(sectionViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of SectionDataBandLabelGroup objects on the specified SectionView.
            sectionViewId: ObjectId - The objectId of the SectionView where the label groups are located.
        """
        pass
    
    pass

class SectionGradeBreakLabelGroup(Entity):
    """
    This class represents a section grade break label group.
    """
    StaggerLineHeight1 = None
    StaggerLineHeight2 = None
    Weeding = None
    def Create(self):
        """
        Create(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectId
            Creates a new instance of a SectionGradeBreakLabelGroup on the Section in the specified SectionView with the default label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label group is located.
            sectionId: ObjectId - The ObjectId of the Section where the label group is labeling.
        Create(sectionViewId: ObjectId, sectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SectionGradeBreakLabelGroup on the Section in the specified SectionView with the specified label style.
            sectionViewId: ObjectId - The ObjectId of SectionView where the label group is located.
            sectionId: ObjectId - The ObjectId of Section where the label group is labeling.
            labelStyleId: ObjectId - The ObjectId of a section gradebreak label style to use.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all available SectionGradeBreakLabelGroup objects on the specified Section and SectionView.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label groups are located.
            sectionId: ObjectId - The ObjectId of the Section where the label groups are labeling.
        """
        pass
    
    pass

class SectionLabelGroup(Entity):
    """
    This class is the a base class for all section-related group labels.
    """
    RangeEnd = None
    RangeEndFromFeature = None
    RangeStart = None
    RangeStartFromFeature = None
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(labelGroupClassType: System.Type, sectionViewId: ObjectId, sectionId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of labels on the profile of a specified type.
            labelGroupClassType: System.Type - The type of the label group class.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label groups are located.
            sectionId: ObjectId - The ObjectId of the Section where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of the specified type.
        """
        pass
    
    pass

class SectionMinorOffsetLabelGroup(Entity):
    """
    This class represents a section minor offset label group.
    """
    MajorOffsetLabelGroupId = None
    RangeEnd = None
    RangeEndFromFeature = None
    RangeStart = None
    RangeStartFromFeature = None
    def Create(self):
        """
        Create(majorOffsetLabelGroupId: ObjectId, increment: System.Double) -> ObjectId
            Creates a new instance of SectionMinorOffsetLabelGroup on the specified SectionOffsetLabelGroup with the default label style.
            majorOffsetLabelGroupId: ObjectId - The ObjectId of the SectionOffsetLabelGroup.
            increment: System.Double - The increment value at which to insert minor offset labels.
        Create(majorOffsetLabelGroupId: ObjectId, increment: System.Double, labelGroupStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SectionMinorOffsetLabelGroup on the specified SectionOffsetLabelGroup with the specified label style.
            majorOffsetLabelGroupId: ObjectId - The ObjectId of the SectionOffsetLabelGroup.
            increment: System.Double - The increment value at which to insert minor offset labels.
            labelGroupStyleId: ObjectId - The ObjectId of the minor offset label style to use (object type LabelStyle).
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all the available SectionOffsetMinorLabelGroup objects on the Section in the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label groups are located.
            sectionId: ObjectId - The ObjectId of the Section where the label groups are labeling.
        """
        pass
    
    pass

class SectionOffsetLabelGroup(Entity):
    """
    This class represents a section offset label group.
    """
    Increment = None
    StaggerLineHeight1 = None
    StaggerLineHeight2 = None
    def CreateMajor(self):
        """
        CreateMajor(sectionViewId: ObjectId, sectionId: ObjectId, increment: System.Double) -> ObjectId
            Creates a new instance of a SectionOffsetLabelGroup on the Section in the specified SectionView with the default label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView in which the label group is located.
            sectionId: ObjectId - The ObjectId of the Section in which the label group is labeling.
            increment: System.Double - The increment value at which to insert major offset labels.
        CreateMajor(sectionViewId: ObjectId, sectionId: ObjectId, increment: System.Double, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SectionOffsetLabelGroup on the Section in the specified SectionView with the specified label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView in which the label group is located.
            sectionId: ObjectId - The ObjectId of the Section in which the label group is labeling.
            increment: System.Double - The increment value at which to insert major offset labels.
            labelStyleId: ObjectId - The ObjectId of the SectionOffsetLabelStyle to use.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all the available SectionOffsetLabelGroup objects on the Section in the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label groups are located.
            sectionId: ObjectId - The ObjectId of the Section where the label groups are labeling.
            includeDerived: System.Boolean - Indicates whether to include the derived types of SectionOffsetLabelGroup.
        """
        pass
    
    pass

class SectionOverride(GraphOverride):
    """
    Object used to change the style or label set for a section.
    """
    OverrideStyleId = None
    OverrideStyleName = None
    SectionId = None
    SectionName = None
    def GetSectionLabelGroupIds(self):
        """
        GetSectionLabelGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of the section's label group.
        """
        pass
    
    pass

class SectionOverrideCollection(GraphOverrideCollection):
    """
    The SectionOverride collection class represents the collection of all Sections listed in the SectionView.
    """

    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionOverride
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class SectionPipeNetwork(Entity):
    """
    Section view of a pipe network.
    """
    StyleId = None
    StyleName = None

    pass

class SectionPoint(object):
    """
    Represents an SectionPoint object. An SectionPoint is a geometry point of a section.
    """
    Location = None
    pass

class SectionPointCollection(object):
    """
    The collection of geometry point of the section object.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionPoint
            Implement the method declare in IEnumerable<T> interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumertor which can be use to enumerate this collection.
        """
        pass
    
    pass

class SectionProjection(Entity):
    """
    AutoCAD or Autodesk Civil 3D objects projected from plan view into a section view.
    """
    StyleId = None
    StyleName = None

    pass

class SectionProjectionLabel(Entity):
    """
    This class represents a section projection label, a label on an object from plan view project into a section view.  
    Projected objects can be SectionProjection, CogoPoint, FeatureLine or SurveyFigure objects.
    """
    ProjectionSourceId = None
    def Create(self):
        """
        Create(sectionViewId: ObjectId, sectionProjectionId: ObjectId) -> ObjectId
            Creates a new instance of a SectionProjectLabel on the specified SectionView with the default label style.
            Remarks: sectionProjectionId must be the ObjectId of a SectionProjection, CogoPoint, FeatureLine or SurveyFigure.
            sectionViewId: ObjectId - The ObjectId of a SectionView in which the label is located.
            sectionProjectionId: ObjectId - The ObjectId of a feature object projected into the SectionView to label 
            (object type SectionProjection, CogoPoint, FeatureLine or SurveyFigure).
        Create(sectionViewId: ObjectId, sectionProjectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SectionProjectLabel on the specified SectionView with the specified label style.
            Remarks: sectionProjectionId must be the ObjectId of a SectionProjection, CogoPoint, FeatureLine or SurveyFigure.
            sectionViewId: ObjectId - The ObjectId of a SectionView in which the label is located.
            sectionProjectionId: ObjectId - The ObjectId of a feature object projected into the SectionView to label 
            (object type SectionProjection, CogoPoint, FeatureLine or SurveyFigure).
            labelStyleId: ObjectId - The ObjectId of a SectionProjectionLabel style to use (object type LabelStyle).
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the SectionProjectionLabels for the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of a SectionView to get the SectionProjectionLabels for.
        """
        pass
    
    pass

class SectionSegmentBandLabelGroup(Entity):
    """
    This class represents a section data band label group.
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(sectionViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of SectionSegmentBandLabelGroup objects on the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label groups are located.
        """
        pass
    
    pass

class SectionSegmentLabelGroup(Entity):
    """
    This class represents a section grade break label group.
    """

    def Create(self):
        """
        Create(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectId
            Creates a new instance of a SectionOffsetLabelGroup on the Section in the specified SectionView with the default label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label group is located.
            sectionId: ObjectId - The ObjectId of the Section where the label group is labeling.
        Create(sectionViewId: ObjectId, sectionId: ObjectId, labelGroupStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SectionSegmentLabelGroup on the Section in the specified SectionView with the specified label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label group is located.
            sectionId: ObjectId - The ObjectId of the Section where the label group is labeling.
            labelGroupStyleId: ObjectId - The ObjectId of the SectionSegmentLabelGroup style to use.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all the available SectionSegmentLabelGroup objects on the Section in the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of the SectionView where the label groups are located.
            sectionId: ObjectId - The ObjectId of the Section where the label groups are labeling.
        """
        pass
    
    pass

class SectionSource(object):
    """
    The available section source in SampleLineGroup.
    """
    IsSampled = None
    SourceId = None
    SourceType = None
    StyleId = None
    UpdateMode = None
    def GetSectionIds(self):
        """
        GetSectionIds() -> ObjectIdCollection
            Gets the objectId collection of sections on the section source.
        """
        pass
    
    pass

class SectionSourceCollection(object):
    """
    The collection of SectionSource in SampleLineGroup.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionSource
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    pass

class SectionSourceType():
    """
    Defines the type of data source from which the section data was extracted.
    """
    pass

class SectionUpdateType():
    """
    Defines the section's update mode.
    """
    pass

class SectionView(Entity):
    """
    Used to display cross sectional data for both existing and finished ground along a sampled cross section line at any given station along a horizontal alignment.
    """
    Bands = None
    ElevationMax = None
    ElevationMin = None
    GraphOverrides = None
    IsElevationRangeAutomatic = None
    IsOffsetRangeAutomatic = None
    OffsetLeft = None
    OffsetRight = None
    ParentEntityId = None
    ProfileGradePoints = None
    VolumeTables = None
    def Create(self):
        """
        Create(sectionViewName: System.String, sampleLineId: ObjectId, location: Point3d) -> ObjectId
            Creates a new section view from a specified sample line.
            sectionViewName: System.String - The name of the newly created section view.
            sampleLineId: ObjectId - The ObjectId of the sample line from which a new section view is created.
            location: Point3d - Location of the newly created section view.
        """
        pass
    
    
    def FindOffsetAndElevationAtXY(self):
        """
        FindOffsetAndElevationAtXY(x: System.Double, y: System.Double, offset: System.Double, elevation: System.Double) -> bool
            Finds the offset and elevation values at the given X,Y coordinate.
            x: System.Double - The X coordinate in the section view's coordinate system. 
            y: System.Double - The  Y coordinate in the section view's coordinate system. 
            offset: System.Double -  Returns the corresponding offset. 
            elevation: System.Double -  Returns the corresponding elevation. 
        """
        pass
    
    
    def FindXYAtOffsetAndElevation(self):
        """
        FindXYAtOffsetAndElevation(offset: System.Double, elevation: System.Double, x: System.Double, y: System.Double) -> bool
            Finds the X,Y coordinate for the given section and elevation.
            offset: System.Double -  Offset value. 
            elevation: System.Double -  Elevation value. 
            x: System.Double -  Returns the x value in the section view's coordinate system. 
            y: System.Double -  Returns the y value in the section view's coordinate system. 
        """
        pass
    
    
    def GetPipeSectionLabelIds(self):
        """
        GetPipeSectionLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all the PipeSectionLabel objects in the SectionView.
        """
        pass
    
    
    def GetSectionGradeBreakLabelGroupIds(self):
        """
        GetSectionGradeBreakLabelGroupIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of all the SectionGradeBreakLabelGroup objects in the SectionView.
        """
        pass
    
    
    def GetSectionMinorOffsetLabelGroupIds(self):
        """
        GetSectionMinorOffsetLabelGroupIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all the SectionMinorOffsetLabelGroup objects in the SectionView.
        """
        pass
    
    
    def GetSectionOffsetLabelGroupIds(self):
        """
        GetSectionOffsetLabelGroupIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all the SectionOffsetLabelGroup objects in the SectionView.
        """
        pass
    
    
    def GetSectionProjectionLabelIds(self):
        """
        GetSectionProjectionLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the SectionProjectionLabels in the SectionView.
        """
        pass
    
    
    def GetSectionSegmentLabelGroupIds(self):
        """
        GetSectionSegmentLabelGroupIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all the SectionSegmentLabelGroup objects in the SectionView.
        """
        pass
    
    
    def GetSectionViewDepthLabelIds(self):
        """
        GetSectionViewDepthLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of the SectionViewDepthLabels in the SectionView.
        """
        pass
    
    
    def GetSectionViewOffsetElevationLabelIds(self):
        """
        GetSectionViewOffsetElevationLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all the SectionViewOffsetElevationLabels in the SectionView.
        """
        pass
    
    
    def GetStructureSectionLabelIds(self):
        """
        GetStructureSectionLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all the StructureSectionLabel objects in the SectionView.
        """
        pass
    
    pass

class SectionViewBandItem(BandSetItem):
    """
    This class represents a single SectionView data band.
    """
    SampleLineId = None
    Section1Id = None
    Section2Id = None
    pass

class SectionViewBandItemCollection(BandSetItemCollection):
    """
    This class represents a collection of band items for a SectionView object.
    """
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionViewBandItem
            Implements the method declared in the IEnumerable(of T) interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class SectionViewBandSet(GraphBandSet):
    """
    This class represents the band collection in a SectionView.
    """

    def GetBottomBandItems(self):
        """
        GetBottomBandItems() -> SectionViewBandItemCollection
            Gets the bottom band items collection from the SectionView.
        """
        pass
    
    
    def GetTopBandItems(self):
        """
        GetTopBandItems() -> SectionViewBandItemCollection
            Gets the top band items collection from the SectionView.
        """
        pass
    
    
    def SetBottomBandItems(self):
        """
        SetBottomBandItems(bandItems: Autodesk.Civil.DatabaseServices.SectionViewBandItemCollection) -> SectionViewBandItemCollection
            Sets the bottom band items to the SectionView.
            bandItems: Autodesk.Civil.DatabaseServices.SectionViewBandItemCollection
        """
        pass
    
    
    def SetTopBandItems(self):
        """
        SetTopBandItems(bandItems: Autodesk.Civil.DatabaseServices.SectionViewBandItemCollection) -> SectionViewBandItemCollection
            Sets the top band items to the SectionView.
            bandItems: Autodesk.Civil.DatabaseServices.SectionViewBandItemCollection
        """
        pass
    
    pass

class SectionViewDepthLabel(Entity):
    """
    This class represents a section view depth (grade) label.
    """
    EndPoint = None
    StartPoint = None
    def Create(self):
        """
        Create(sectionViewId: ObjectId, startPoint: Point2d, endPoint: Point2d) -> ObjectId
            Creates a new instance of a SectionViewDepthLabel on the specified SectionView with the default label style.
            sectionViewId: ObjectId - The ObjectId of section view in which the label is located (object type SectionView).
            startPoint: Point2d - The startPoint (station and elevation) at which to insert SectionViewDepthLabel.
            This is a Point2d object, where startPoint.X is the station value, and startPoint.Y is the elevation.
            endPoint: Point2d - The endPoint (station and elevation) at which to insert SectionViewDepthLabel.
            This is a Point2d object, where endPoint.X is the station value, and endPoint.Y is the elevation.
        Create(sectionViewId: ObjectId, startPoint: Point2d, endPoint: Point2d, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of SectionViewDepthLabel on the specified SectionView with the specified label style.
            sectionViewId: ObjectId - The ObjectId of a section view in which the label is located (object type SectionView).
            startPoint: Point2d - The startPoint (station and elevation) at which to insert SectionViewDepthLabel.  
            This is a Point2d object, where startPoint.X is the station value, and startPoint.Y is the elevation.
            endPoint: Point2d - The endPoint (station and elevation) at which to insert SectionViewDepthLabel.
            This is a Point2d object, where endPoint.X is the station value, and endPoint.Y is the elevation.
            labelStyleId: ObjectId - The ObjectId of the SectionViewDepthLabel style to use (object type LabelStyle).
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of all SectionViewDepthLabel objects in the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of the SectionView for which to get the SectionViewDepthLabels.
        """
        pass
    
    pass

class SectionViewGroup(object):
    """
    
    """
    IsIndividual = None
    LayoutName = None
    Name = None
    PlotStyleId = None
    SampleLineGroupId = None
    TemplateFilePath = None
    def GetSectionViewIds(self):
        """
        GetSectionViewIds() -> ObjectIdCollection
            Gets the objectId collection of all section views attached on SampleLineGroup.
        """
        pass
    
    pass

class SectionViewGroupCollection(object):
    """
    The collection of SectionViewGroup in SampleLineGroup.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(insertPosition: Point3d) -> SectionViewGroup
            Add a SectionViewGroup which will create multiple SectionViews for each SampleLine in SampleLineGroup.
            insertPosition: Point3d - The position at which the SectionView is inserted.
        Add(insertPosition: Point3d, startStation: System.Double, endStation: System.Double, rangeOptions: Autodesk.Civil.DatabaseServices.SectionViewGroupCreationRangeOptions, placementOptions: Autodesk.Civil.DatabaseServices.SectionViewGroupCreationPlacementOptions) -> SectionViewGroup
            Add a SectionViewGroup which will create multiple SectionViews within specified station range in Alignment.
            insertPosition: Point3d - The position at which the SectionView is inserted.
            startStation: System.Double - The user specified start station on Alignment.
            endStation: System.Double - The user specified end station on Alignment.
            rangeOptions: Autodesk.Civil.DatabaseServices.SectionViewGroupCreationRangeOptions - The user specified range options to determine the offset and elevation.
            placementOptions: Autodesk.Civil.DatabaseServices.SectionViewGroupCreationPlacementOptions - The options to control the placement of the SectionViews in model space.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionViewGroup
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(sectionViewGroup: Autodesk.Civil.DatabaseServices.SectionViewGroup) -> SectionViewGroup
            Removes a SectionViewGroup from the collection.
            sectionViewGroup: Autodesk.Civil.DatabaseServices.SectionViewGroup - The SectionViewGroup to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a SectionViewGroup specified by index from the collection.
            index: System.Int32 - Index of SectionViewGroup to be removed.
        """
        pass
    
    pass

class SectionViewGroupCreationPlacementOptions(object):
    """
    This class encapsulates the placement options for creating SectionViewGroup.
    """
    LayoutName = None
    PlacementOption = None
    TemplateFilePath = None
    def GetAvailableLayoutNames(self):
        """
        GetAvailableLayoutNames(templateFilePath: System.String) -> string[]
            Gets a string array that contains all the layouts of drawing in templateFilePath.
            templateFilePath: System.String - Specifies the drawing template file path and name.
        """
        pass
    
    
    def UseDraftPlacement(self):
        """
        UseDraftPlacement()
            Make the section views in SectionViewGroup be created in a grid in model space without using a template.
        """
        pass
    
    
    def UseProductionPlacement(self):
        """
        UseProductionPlacement(templateFilePath: System.String, layoutName: System.String)
            Specifies a drawing template with layout name for new SectionViewGroup which can be used for creating production-ready section sheets.
            templateFilePath: System.String - Specifies the drawing template file path and name.
            layoutName: System.String - Specifies the layout name in the drawing template file.
        """
        pass
    
    pass

class SectionViewGroupCreationRangeOptions(object):
    """
    This class encapsulates the range options for creating SectionViewGroup.
    """
    Elevation = None
    ElevationRangeType = None
    LeftOffset = None
    RightOffset = None
    UseUserSpecifiedElevation = None
    UseUserSpecifiedOffset = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the SectionViewGroupCreationRangeOptions
        """
        pass
    
    
    def FollowSection(self):
        """
        FollowSection(sectionSource: Autodesk.Civil.DatabaseServices.SectionSource) -> SectionSource
            Sets the SectionSource to be followed to determine the elevation.
            sectionSource: Autodesk.Civil.DatabaseServices.SectionSource
        """
        pass
    
    
    def SetOffsetRange(self):
        """
        SetOffsetRange(leftOffset: System.Double, rightOffset: System.Double)
            sets the left offset and right offset for each SectionView to be created in SectionViewGroup.
            leftOffset: System.Double - The user specified left offset of each SectionView.
            rightOffset: System.Double - The user specified right offset of each SectionView.
        """
        pass
    
    pass

class SectionViewOffsetElevationLabel(Entity):
    """
    This class represents a section view offset elevation label.
    """
    Elevation = None
    Offset = None
    Section1Id = None
    Section2Id = None
    def Create(self):
        """
        Create(sectionViewId: ObjectId, offset: System.Double, elevation: System.Double) -> ObjectId
            Creates a new instance of a SectionViewOffsetElevationLabel on the specified section view with the default label style and marker style.
            sectionViewId: ObjectId - The ObjectId of the section view in which the label is located.
            offset: System.Double - The offset value on the section view at which to insert the SectionViewOffsetElevationLabel.
            elevation: System.Double - The elevation value at which insert SectionViewOffsetElevationLabel.
        Create(sectionViewId: ObjectId, offset: System.Double, elevation: System.Double, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SectionViewOffsetElevationLabel on the specified section view with the specified label style and marker style.
            sectionViewId: ObjectId - The ObjectId of the section view in which the label is located.
            offset: System.Double - The offset value on the section view at which to insert the SectionViewOffsetElevationLabel.
            elevation: System.Double - The elevation value at which insert SectionViewOffsetElevationLabel.
            labelStyleId: ObjectId - The ObjectId of the SectionViewOffsetElevationLabel style to use (object type LabelStyle).
            markerStyleId: ObjectId - The ObjectId of the marker display style (object type MarkerStyle).
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection
            Gets a ObjectIdCollection of all SectionViewOffsetElevationLabels for the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of the section view to get the SectionViewOffsetElevationLabels for.
        """
        pass
    
    pass

class SectionViewProfileGradePoint(object):
    """
    This class represents the profile grade point in a SectionView.
    """
    AlignmentId = None
    IsShow = None
    MarkerStyleId = None
    ProfileId = None
    pass

class SectionViewProfileGradePointCollection(object):
    """
    This class represents the collection of profile grade points in a SectionView.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(alignmentId: ObjectId) -> SectionViewProfileGradePoint
            Adds a profile grade point into profile grade point collection.
            alignmentId: ObjectId
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> SectionViewProfileGradePoint
            Implements the method declared in the IEnumerable(of T) interface. This method returns an enumerator for this collection.
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
        Remove(pgPoint: Autodesk.Civil.DatabaseServices.SectionViewProfileGradePoint) -> SectionViewProfileGradePoint
            Removes the given profile grade point.
            pgPoint: Autodesk.Civil.DatabaseServices.SectionViewProfileGradePoint
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a profile grade point by index.
            index: System.Int32
        """
        pass
    
    pass

class SectionViewQuantityTakeoffTable(Entity):
    """
    The AeccDbSectionViewQuantityTakeoffTable wrapper.
    """
    MaterialListGuid = None
    Type = None
    def AddSelectedMaterial(self):
        """
        AddSelectedMaterial(materialGuid: System.Guid) -> bool
            Adds a selected material for Material table.
            materialGuid: System.Guid
        """
        pass
    
    
    def GetSelectedMaterials(self):
        """
        GetSelectedMaterials() -> Guid[]
            Gets the selected materials when table type is Material.
        """
        pass
    
    
    def RemoveSelectedMaterial(self):
        """
        RemoveSelectedMaterial(materialGuid: System.Guid) -> bool
            Removes a selected material for Material table.
            materialGuid: System.Guid
        """
        pass
    
    pass

class SectionViewVolumeTableAnchorType():
    """
    Defines types of section view anchors and table anchors.
    """
    pass

class SectionViewVolumeTableGroup(object):
    """
    This class represents volume table group in a SectionView.
    """
    OffsetX = None
    OffsetY = None
    SectionViewAnchorType = None
    TableAnchorType = None
    TableLayoutType = None
    def CreateVolumeTable(self):
        """
        CreateVolumeTable(type: Autodesk.Civil.DatabaseServices.VolumeTableType, materialListGuid: System.Guid) -> VolumeTableType
            Creates a volume tables to the section view.
            Remarks: Tables with the same type and the same material list guid are duplicate.
            If no material list guid set to the tables, tables with the same type are duplicate.
            type: Autodesk.Civil.DatabaseServices.VolumeTableType
            materialListGuid: System.Guid
        """
        pass
    
    
    def GetVolumeTableIds(self):
        """
        GetVolumeTableIds() -> ObjectIdCollection
            Gets the ObjectIdCollection of all volume tables in the section view.
        """
        pass
    
    
    def Swap(self):
        """
        Swap(tableId1: ObjectId, tableId2: ObjectId)
            Swaps volume table positions in the group by ObjectId.
            tableId1: ObjectId - ObjectId of the first volume table to be swapped.
            tableId2: ObjectId - ObjectId of the second volume table to be swapped.
        """
        pass
    
    
    def SwapAt(self):
        """
        SwapAt(index1: System.Int32, index2: System.Int32)
            Swaps volume table positions in the group by index.
            index1: System.Int32 - Index (in volume table id collection) of the first volume table to be swapped.
            index2: System.Int32 - Index (in volume table id collection) of the second volume table to be swapped.
        """
        pass
    
    pass

class SectionViewVolumeTableLayoutType():
    """
    Defines table layout directions.
    """
    pass

class SectionalDataBandLabelGroup(Entity):
    """
    
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all SectionalDataBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all SectionalDataBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of SectionalDataBandLabelGroup.
        """
        pass
    
    pass

class Shape(object):
    """
    Roadway Shape object. Represents a series of roadway links which form a closed shape. Used in subassemblies.
    """
    Codes = None
    Index = None
    IsHidden = None
    Links = None
    def AddHole(self):
        """
        AddHole(links: Autodesk.Civil.DatabaseServices.Link) -> Link
            Add a hole into an existing shape.
            
            Links of the hole.
            links: Autodesk.Civil.DatabaseServices.Link
        """
        pass
    
    pass

class ShapeCollection(object):
    """
    A collection of Roadway Shape objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(links: Autodesk.Civil.DatabaseServices.Link, code: System.String) -> Shape
            Add a shape.
            links: Autodesk.Civil.DatabaseServices.Link - 
            Links of the shape.
            code: System.String - 
            The code of the shape.
        Add(links: Autodesk.Civil.DatabaseServices.Link, codes: System.String) -> Shape
            Add a shape.
            links: Autodesk.Civil.DatabaseServices.Link - 
            Links of the shape.
            codes: System.String - 
            The codes of the shape.
        Add(link1: Autodesk.Civil.DatabaseServices.Link, link2: Autodesk.Civil.DatabaseServices.Link, link3: Autodesk.Civil.DatabaseServices.Link, link4: Autodesk.Civil.DatabaseServices.Link, code: System.String) -> Shape
            Add a shape. In most cases, a shape is defined by 4 links.
            link1: Autodesk.Civil.DatabaseServices.Link - 
            First link of the shape.
            link2: Autodesk.Civil.DatabaseServices.Link - 
            Second link of the shape.
            link3: Autodesk.Civil.DatabaseServices.Link - 
            Third link of the shape.
            link4: Autodesk.Civil.DatabaseServices.Link - 
            Fourth link of the shape.
            code: System.String - 
            The code of the shape.
        Add(link1: Autodesk.Civil.DatabaseServices.Link, link2: Autodesk.Civil.DatabaseServices.Link, link3: Autodesk.Civil.DatabaseServices.Link, link4: Autodesk.Civil.DatabaseServices.Link, codes: System.String) -> Shape
            Add a shape. In most cases, a shape is defined by 4 links.
            link1: Autodesk.Civil.DatabaseServices.Link - 
            First link of the shape.
            link2: Autodesk.Civil.DatabaseServices.Link - 
            Second link of the shape.
            link3: Autodesk.Civil.DatabaseServices.Link - 
            Third link of the shape.
            link4: Autodesk.Civil.DatabaseServices.Link - 
            Fourth link of the shape.
            codes: System.String - 
            The codes of the shape.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> Shape
            Implements the method declared in the IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method return an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(index: System.Int32)
            Remove the Shape from collection.
            index: System.Int32 - 
            Index of the Shape.
        Remove(shape: Autodesk.Civil.DatabaseServices.Shape) -> Shape
            Remove the Shape from collection.
            shape: Autodesk.Civil.DatabaseServices.Shape - 
            The Shape need to be removed.
        """
        pass
    
    pass

class Sheet(Entity):
    """
    A sheet (construction document) object.
    """


    pass

class SideRoadProfileDistanceRuleType():
    """
    Specifies the method that is used to adjust the grade of the secondary road profile. 
    When To Intersection Extents is selected, the grade of the secondary road profile is adjusted to meet the extents of the intersection object. 
    When Specify Distance is used, the grade of the secondary road profile is adjusted by the value that is entered in the Distance Value.
    """
    pass

class Site(Entity):
    """
    The construction site abstraction containing parcels and alignments. 
    Note:
    Alignments are generally associated with a site.  An alignment interacts with objects on a site in two ways:
    If an alignment exists on a site with parcels, the alignment will subdivide any parcels it crosses over. If one or more alignments on a site form a closed region, a parcel will be created from the region.
    """

    def Create(self):
        """
        Create(document: Autodesk.Civil.ApplicationServices.CivilDocument, siteName: System.String) -> CivilDocument
            Creates a new site.
            document: Autodesk.Civil.ApplicationServices.CivilDocument - Document object in which the site is created.
            siteName: System.String - Name of the new site.
        """
        pass
    
    
    def GetAlignmentIds(self):
        """
        GetAlignmentIds() -> ObjectIdCollection
            Gets the objectId collection of all alignment objects in the site.
        """
        pass
    
    
    def GetFeatureLineIds(self):
        """
        GetFeatureLineIds() -> ObjectIdCollection
            Gets the objectId collection of all feature lines in the site.
        """
        pass
    
    
    def GetParcelIds(self):
        """
        GetParcelIds() -> ObjectIdCollection
            Gets the objectId collection of all parcels in the site.
        """
        pass
    
    pass

class SlopeElevationTarget(object):
    """
    The SlopeElevation class.
    """
    TargetId = None
    def GetElevation(self):
        """
        GetElevation(alignmentId: ObjectId, stationOnAlignment: System.Double) -> double
            alignmentId: ObjectId
            stationOnAlignment: System.Double
        GetElevation(alignmentId: ObjectId, stationOnAlignment: System.Double, side: Autodesk.Civil.DatabaseServices.AlignmentSide) -> AlignmentSide
            alignmentId: ObjectId
            stationOnAlignment: System.Double
            side: Autodesk.Civil.DatabaseServices.AlignmentSide
        """
        pass
    
    
    def GetNearestPipeOfNetworkToAlignment(self):
        """
        GetNearestPipeOfNetworkToAlignment(alignmentId: ObjectId, stationOnAlignment: System.Double, pipeId: ObjectId)
            alignmentId: ObjectId
            stationOnAlignment: System.Double
            pipeId: ObjectId
        GetNearestPipeOfNetworkToAlignment(alignmentId: ObjectId, stationOnAlignment: System.Double, side: Autodesk.Civil.DatabaseServices.AlignmentSide, pipeId: ObjectId) -> AlignmentSide
            alignmentId: ObjectId
            stationOnAlignment: System.Double
            side: Autodesk.Civil.DatabaseServices.AlignmentSide
            pipeId: ObjectId
        """
        pass
    
    pass

class SpanningPipeLabel(Entity):
    """
    This class represents a SpanningPipeLabel.
    """
    AnchorPipeId = None
    Length2DCenterToCenter = None
    Length2DEdgeToEdge = None
    Length3DCenterToCenter = None
    Length3DEdgeToEdge = None
    PipeIds = None
    Ratio = None
    ReferenceAlignmentId = None
    ShowSpannedPipes = None
    StructureIds = None
    def Create(self):
        """
        Create(partIds: ObjectIdCollection, anchorPipeId: ObjectId) -> ObjectId
            Creates a new instance of a SpanningPipeLabel that spans a collection of parts using the default label style.
            Remarks: If a path that crosses each item in partIds can be calculated, 
            each pipe on the path will be spanned.If the path that crosses two adjacent items in partIds crosses back on the starting part 
            to form a loop, the spanned part in the loop is abandoned.
            partIds: ObjectIdCollection - An ObjectIdCollection of Parts that need spanning.
            anchorPipeId: ObjectId - The ObjectId of the Pipe on which the label is located.
        Create(partIds: ObjectIdCollection, anchorPipeId: ObjectId, ratio: System.Double, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SpanningPipeLabel that spans a specified collection of parts with the specified label style.
            Remarks: If a path that crosses each item in partIds can be calculated, 
            each pipe on the path will be spanned.If the path that crosses two adjacent items in partIds crosses back on the starting part 
            to form a loop, the spanned part in the loop is abandoned.
            partIds: ObjectIdCollection - An ObjectIdCollection of the Parts which need spanning.
            anchorPipeId: ObjectId - The ObjectId of the Pipe in which the label is located.
            ratio: System.Double - The relative position of the label to the pipe.
            labelStyleId: ObjectId - The ObjectId of a SpanningPipeLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(pipeId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the SpanningPipeLabels for the specified Pipe.
            pipeId: ObjectId - The ObjectId of Pipe.
        """
        pass
    
    pass

class SpanningPipeProfileLabel(Entity):
    """
    This class represents a SpanningPipeProfileLabel.
    """
    AnchorProfileViewPartId = None
    Length2DCenterToCenter = None
    Length2DEdgeToEdge = None
    Length3DCenterToCenter = None
    Length3DEdgeToEdge = None
    ProfileViewPipeIds = None
    ProfileViewStructureIds = None
    Ratio = None
    ReferenceAlignmentId = None
    ShowSpannedProfileViewPipes = None
    def Create(self):
        """
        Create(profileViewPartIds: ObjectIdCollection, anchorProfileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectId
            Creates a new instance of a SpanningPipeProfileLabel that spans a collection of ProfileViewParts using the default label style.
            Remarks: The source of anchorProfileViewPartId should be a pipe.A path crossing each item in profileViewPartIds is calculated, and each profileViewPart on the path is spanned.If the path crossing two adjacent items in partIds crosses back to the start part to form a loop, the spanned part in the loop is abandoned.
            profileViewPartIds: ObjectIdCollection - An ObjectIdCollection of ProfileViewParts that need spanning.
            anchorProfileViewPartId: ObjectId - The ObjectId of the ProfileViewPart on which the label is located.
            profileViewId: ObjectId - The ObjectId of the ProfileView in which the label is located.
        Create(profileViewPartIds: ObjectIdCollection, anchorProfileViewPartId: ObjectId, profileViewId: ObjectId, ratio: System.Double, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a SpanningPipeProfileLabel that spans a collection of ProfileViewParts using the specified label style.
            Remarks: The ratio should be in the range [0, 1].The source of anchorProfileViewPartId should be a pipe.A path crossing each item in profileViewPartIds is calculated, and each profileViewPart on the path is spanned.If the path crossing two adjacent items in partIds crosses back to the start part to form a loop, the spanned part in the loop is abandoned.
            profileViewPartIds: ObjectIdCollection - An ObjectIdCollection of ProfileViewParts that need spanning.
            anchorProfileViewPartId: ObjectId - The ObjectId of a ProfileViewPart on which the label is located.
            profileViewId: ObjectId - The ObjectId of the ProfileView in which the label is located.
            ratio: System.Double - A ratio that determines the relative position of the label to the ProfileViewPart.
            labelStyleId: ObjectId - The ObjectId of SpanningPipeLabel style.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the SpanningPipeProfileLabels for the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of a ProfileView.
        """
        pass
    
    pass

class SpiralCurveType():
    """
    Defines the curve type for a spiral sub-entity.
    """
    pass

class SpiralDirectionType():
    """
    Defines the direction of a spiral sub-entity.
    """
    pass

class SpiralParamType():
    """
    Defines the type to attch the entity.
    """
    pass

class SplitProfileViewCreationOptions(object):
    """
    This class represents the options for creating SplitProfileViews.
    """
    FirstViewStyleId = None
    IntermediateViewStyleId = None
    LastViewStyleId = None
    SplitDatumOption = None
    SplitStationOption = None
    ViewHeight = None
    pass

class SplitStationType():
    """
    Defines the ways to split profile view.
    """
    pass

class StackedProfileViewsCreationOptions(object):
    """
    This class encapsulates the options for creating stacked ProfileViews.
    """
    BottomViewStyleId = None
    GapBetweenViews = None
    MiddleViewStyleId = None
    NumberOfViews = None
    TopViewStyleId = None
    pass

class StandardPointGroupQuery(PointGroupQuery):
    """
    This class encapsulates a standard point group query.
    """
    ExcludeElevations = None
    ExcludeFullDescriptions = None
    ExcludeNames = None
    ExcludeNumbers = None
    ExcludeRawDescriptions = None
    IncludeAllPoints = None
    IncludeElevations = None
    IncludeFullDescriptions = None
    IncludeNames = None
    IncludeNumbers = None
    IncludeRawDescriptions = None
    PointGroups = None
    pass

class Station(object):
    """
    The Alignment Station class.
    """
    GeometryStationType = None
    Location = None
    RawStation = None
    StationType = None
    pass

class StationElevationLabel(Entity):
    """
    This class represents a profile view station elevation label.
    """
    Elevation = None
    Profile1Id = None
    Profile2Id = None
    Station = None
    def Create(self):
        """
        Create(profileViewId: ObjectId, labelStyleId: ObjectId, markerStyleId: ObjectId, station: System.Double, elevation: System.Double) -> ObjectId
            Creates a new instance of StationElevationLabel on the profileview with the specified label style and marker style.
            profileViewId: ObjectId - The ObjectId of profile view in which the label is located.
            labelStyleId: ObjectId - The ObjectId of StationElevationLabel style.
            markerStyleId: ObjectId - The ObjectId of StationElevationLabel's marker style.
            station: System.Double - The station value at which to insert StationElevationLabel.
            elevation: System.Double - The elevation value at which to insert StationElevationLabel.
        """
        pass
    
    pass

class StationEquation(object):
    """
    Represents a particular system of renumbering or reordering stations within a portion of an alignment.
    """
    EquationType = None
    RawStationBack = None
    StationAhead = None
    StationBack = None
    pass

class StationEquationCollection(object):
    """
    A collection of StationEquation objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(rawStationBack: System.Double, stationAhead: System.Double, stationEquationType: Autodesk.Civil.DatabaseServices.StationEquationType) -> StationEquation
            Adds a station equation into the alignment.
            rawStationBack: System.Double - Raw station back value.
            stationAhead: System.Double - Station ahead value.
            stationEquationType: Autodesk.Civil.DatabaseServices.StationEquationType - Specifies the station equation type.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> StationEquation
            Implement the method declare in IEnumerable<T> interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implement the method declare in IEnumerable interface. This method return an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetStationEquation(self):
        """
        GetStationEquation(rawStationBack: System.Double) -> StationEquation
            Gets the StationEquation object in the collection by raw station back.
            rawStationBack: System.Double - Raw station back value.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(rawStationBack: System.Double)
            Removes a station equation from the collection by raw station back.
            rawStationBack: System.Double - Raw station back value.
        Remove(index: System.Int32)
            Removes a station equation from the collection at the given index.
            index: System.Int32 - Index of the StationEquation object to remove.
        """
        pass
    
    pass

class StationEquationType():
    """
    Specifies the kind of StationEquation.
    """
    pass

class StationOffsetLabel(Entity):
    """
    This class represents a station offset label.
    """
    AnchorAtXY = None
    Location = None
    def Create(self):
        """
        Create(alignmentId: ObjectId, labelStyleId: ObjectId, markerStyleId: ObjectId, location: Point2d) -> ObjectId
            Creates a new instance of an AlignmentCurveLabel and adds it to the specified database.
            alignmentId: ObjectId - The object id of alignment to which the label is attahed.
            labelStyleId: ObjectId - The object id of label style for the label.
            markerStyleId: ObjectId - The object id of marker style for the label.
            location: Point2d - The place in which the label is located.
        """
        pass
    
    pass

class StationRangeType():
    """
    Defines the ways to specify the horizontal range of the profile view.
    """
    pass

class StationRoundingType():
    """
    Specifies where to round the horizontal split location.
    """
    pass

class StationTypes():
    """
    Defines the possible station types, used
    by Alignment::GetStationSet().
    """
    pass

class Structure(Entity):
    """
    The drawing shape used to represent items such as manholes, catch basins, and headwalls used in utility networks. A Structure connects pipes together to form a pipe network.
    """
    AutomaticRimSurfaceAdjustment = None
    BarrelPipeClearance = None
    BoundingShape = None
    ConeHeight = None
    ConnectedPipe = None
    ConnectedPipesCount = None
    ControlSumpBy = None
    Cover = None
    DiameterOrWidth = None
    Easting = None
    FloorThickness = None
    Frame = None
    FrameDiameter = None
    FrameHeight = None
    Grate = None
    HeadwallBaseThickness = None
    HeadwallBaseWidth = None
    Height = None
    InnerDiameterOrWidth = None
    InnerLength = None
    Length = None
    Location = None
    Northing = None
    Offset = None
    PipeCenterDepth = None
    PipeInnerDiameterOrWidth = None
    PipeInvertDepth = None
    PipeLowestBottomDepth = None
    PipeOuterBottomDepth = None
    PipeOuterTopDepth = None
    PipeUpperTopDepth = None
    PipeWallThickness = None
    RimElevation = None
    RimToSumpHeight = None
    Rotation = None
    Station = None
    StyleId = None
    SumpDepth = None
    SumpElevation = None
    SurfaceAdjustmentValue = None
    SurfaceElevationAtInsertionPoint = None
    VerticalPipeClearance = None
    def ConnectToPipe(self):
        """
        ConnectToPipe(pipeId: ObjectId, positionType: Autodesk.Civil.DatabaseServices.ConnectorPositionType) -> ConnectorPositionType
            Connect this structure to the specified pipe.
            pipeId: ObjectId - The pipe to connect to.
            positionType: Autodesk.Civil.DatabaseServices.ConnectorPositionType - The connector position, either start or end.
        """
        pass
    
    
    def Disconnect(self):
        """
        Disconnect(pipeId: ObjectId)
            Disconnect from a pipe.
            pipeId: ObjectId - The pipe to disconnect from.
        """
        pass
    
    
    def GetAvailableStructureLabelIds(self):
        """
        GetAvailableStructureLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of StructureLabels on the Structure.
        """
        pass
    
    
    def GetConnectedPipeNames(self):
        """
        GetConnectedPipeNames() -> string[]
            Gets all the connected pipe names.
        """
        pass
    
    
    def GetLabelIds(self):
        """
        GetLabelIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of labels on the Structure.
        """
        pass
    
    
    def IsConnectedPipeFlowingIn(self):
        """
        IsConnectedPipeFlowingIn(index: System.Int32) -> bool
            Determines if the connected pipe is flowing into the structure
            index: System.Int32 - The index of the pipe to check.
        """
        pass
    
    
    def IsConnectedPipeFlowingOut(self):
        """
        IsConnectedPipeFlowingOut(index: System.Int32) -> bool
            Determines if the connected pipe is flowing out of the structure
            index: System.Int32 - The index of the pipe to check.
        """
        pass
    
    
    def IsPointInsideStructureRegion(self):
        """
        IsPointInsideStructureRegion(point: Point3d) -> bool
            Returns true if the point is within the structure region.
            point: Point3d - The point to test.
        """
        pass
    
    
    def ResizeByPipeDepths(self):
        """
        ResizeByPipeDepths() -> bool
            Resize the structure by pipe depths.
        """
        pass
    
    
    def ResizeJunctionStructure(self):
        """
        ResizeJunctionStructure(partFamilyGuid: System.String, rimElevation: System.Double, sumpElevation: System.Double)
            Resize the Junction structure by rim and sump elevations.
            partFamilyGuid: System.String - Part family's globally unique identifier.
            rimElevation: System.Double - Rim elevation
            sumpElevation: System.Double - Sump elevation.
        """
        pass
    
    pass

class StructureControlSumpType():
    """
    Specifies how a sump should be adjusted.
    """
    pass

class StructureLabel(Entity):
    """
    This class represents a StructureLabel.
    """
    ReferenceAlignmentId = None
    def Create(self):
        """
        Create(structureId: ObjectId) -> ObjectId
            Creates a new instance of a StructureLabel on a Structure using the default label style.
            Remarks: The LabelLocation of the new label is on the center of the Structure.
            structureId: ObjectId - The ObjectId of the Structure on which the label is located.
        Create(structureId: ObjectId, labelStyleId: ObjectId, labelLocation: Point3d) -> ObjectId
            Creates a new instance of a StructureLabel on a Structure using the specified label style.
            structureId: ObjectId - The ObjectId of the Structure on which the label is located.
            labelStyleId: ObjectId - The ObjectId of the stucture label style to use.
            labelLocation: Point3d - The position of the label text.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(structureId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the StructureLabels on the specified Structure.
            structureId: ObjectId - The ObjectId of the Structure.
        """
        pass
    
    pass

class StructureOverride(GraphOverride):
    """
    Object used to change the style for a structure.
    """
    Draw = None
    OverrideStyleId = None
    OverrideStyleName = None
    StructId = None
    StructName = None
    pass

class StructureOverrideCollection(GraphOverrideCollection):
    """
    The StuctureOverrideCollection collection class represents the collection of all structures listed in the ProfileView.
    """
    SplitAt = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> StructureOverride
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    pass

class StructureProfileLabel(Entity):
    """
    This class represents a StructureProfileLabel.
    """

    def Create(self):
        """
        Create(profileViewId: ObjectId, profileViewPartId: ObjectId) -> ObjectId
            Creates a new instance of a StructureProfileLabel on the center of a ProfileViewPart using the default label style.
            profileViewId: ObjectId - The ObjectId of the ProfileView in which the label is located.
            profileViewPartId: ObjectId - The ObjectId of the ProfileViewPart in which the label is located.
        Create(profileViewId: ObjectId, profileViewPartId: ObjectId, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a StructureProfileLabel on a ProfileViewPart using the specified label style.
            profileViewId: ObjectId - The ObjectId of the ProfileView in which the label is located.
            profileViewPartId: ObjectId - The ObjectId of the ProfileViewPart in which the label is located.
            labelStyleId: ObjectId - The ObjectId of a StructureProfileLabel style to use.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the StructureProfileLabels in the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of a ProfileView.
        """
        pass
    
    pass

class StructureSectionLabel(Entity):
    """
    This class represents a StructureSectionLabel.
    """

    def Create(self):
        """
        Create(sectionViewId: ObjectId, structureId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: System.Int32) -> ObjectId
            Creates a new instance of a StructureSectionLabel on a SectionPipeNetwork using the default label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView in which the label is located.
            structureId: ObjectId - The ObjectId of the Structure that is one of the sources of the SectionPipeNetwork.
            sectionPipeNetworkId: ObjectId - The ObjectId of the SectionPipeNetwork.
            partIndex: System.Int32 - The zero-based index of the part in the SectionPipeNetwork with the specified Structure source.
        Create(sectionViewId: ObjectId, structureId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: System.Int32, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a StructureSectionLabel on a SectionPipeNetwork using the specified label style.
            sectionViewId: ObjectId - The ObjectId of the SectionView in which the label is located.
            structureId: ObjectId - The ObjectId of the Structure that is one of the sources of the SectionPipeNetwork.
            sectionPipeNetworkId: ObjectId - The ObjectId of the SectionPipeNetwork.
            partIndex: System.Int32 - The zero-based index of a part in the SectionPipeNetwork with the specified Structure source.
            labelStyleId: ObjectId - The ObjectId of a StructureSectionLabel style.
        """
        pass
    
    
    def GetAvailableLabelIds(self):
        """
        GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection
            Gets an ObjectIdCollection of the StructureSectionLabels in the specified SectionView.
            sectionViewId: ObjectId - The ObjectId of the SectionView.
        """
        pass
    
    pass

class Subassembly(Entity):
    """
    Pattern for part of a corridor cross section, representing a particular portion of a roadway.
    """
    AssemblyId = None
    AttachedToOffsetAssembly = None
    CodeSetStyleName = None
    DefaultLoopInLayoutMode = None
    DefaultLoopOffsetInLayoutMode = None
    GeometryGenerator = None
    HasParentAssembly = None
    HasSide = None
    HelpCommand = None
    HelpData = None
    HelpFile = None
    IsDynamic = None
    Links = None
    OffsetAssemblyName = None
    OffsetToAssembly = None
    OffsetToBaseline = None
    OffsetToParentAssembly = None
    Origin = None
    ParamsBool = None
    ParamsDouble = None
    ParamsLong = None
    ParamsString = None
    PointIndexHookTo = None
    Points = None
    ResourceModule = None
    Shapes = None
    Side = None
    StyleName = None
    SubassemblyHookTo = None
    UseEmbeddedProject = None
    def EraseAllParams(self):
        """
        EraseAllParams()
            Erases all the subassembly's script parameters.
        """
        pass
    
    
    def GetResourceString(self):
        """
        GetResourceString(resourceId: System.UInt32) -> string
            Converts a resource id (numeric) to a resource string from the current subassembly's resource module.
            resourceId: System.UInt32
        GetResourceString(resourceId: System.String) -> string
            Converts a resource id (string) to a resource string from the current subassembly's resource module.
            resourceId: System.String
        """
        pass
    
    
    def Run(self):
        """
        Run()
            Runs the callback function associated with the Subassembly.
        """
        pass
    
    
    def ShowHelp(self):
        """
        ShowHelp()
            Shows the help information associated with a subassembly.
        """
        pass
    
    pass

class SubassemblyCollection(object):
    """
    A collection of Subassembly objects.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(subassemblyName: System.String, entityId: ObjectId, midOrdinateDist: System.Double, linkCreationOption: Autodesk.Civil.LinkCreationType) -> LinkCreationType
            Adds a subassembly with the specified name, entity, mid-ordinate distance and link creation option.
            Remarks: The valid types for entity used to create subassembly are Polyline, Polyline3d, Polyline2d, Feature, Face, Line, Circle, Arc, Ellipse and Spline.
            subassemblyName: System.String - Subassembly Name used to create subassembly.
            entityId: ObjectId - Object id of the entity used to create subassembly.
            midOrdinateDist: System.Double - Mid-ordinate distance used to create subassembly.
            linkCreationOption: Autodesk.Civil.LinkCreationType - Link creation option used to create subassembly.
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
    
    
    def GetSubassemblyIdsByName(self):
        """
        GetSubassemblyIdsByName(subassemblyName: System.String) -> ObjectIdCollection
            Gets subassembly id collection by name.
            subassemblyName: System.String
        """
        pass
    
    
    def ImportStockSubassembly(self):
        """
        ImportStockSubassembly(subassemblyName: System.String, className: System.String, location: Point3d) -> ObjectId
            Imports a stock Subassembly object with its class name.
            Remarks: It will import the corresponding subassembly according to the drawing unit settings.
            subassemblyName: System.String - Subassembly Name used to create subassembly.
            className: System.String - Class name of the subassembly.
            location: Point3d - The location of the new created subassembly.
        """
        pass
    
    
    def ImportSubassembly(self):
        """
        ImportSubassembly(subassemblyName: System.String, atcFilePath: System.String, itemId: System.String, location: Point3d) -> ObjectId
            Imports a Subassembly object from an atc file specified by its itemId.
            subassemblyName: System.String - Subassembly Name used to create subassembly.
            atcFilePath: System.String - File path of the atc file.
            itemId: System.String - The itemId of the Subassembly in atc file. It should not include the brackets.
            location: Point3d - The location of the new created subassembly.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(subassemblyId: ObjectId) -> bool
            Removes a subassembly by given subassembly id.
            subassemblyId: ObjectId - The removed subassembly id.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes a subassembly by index.
            index: System.Int32 - Index of the removed subassembly.
        """
        pass
    
    pass

class SubassemblyGenerator(object):
    """
    Controls the way Subassembly geometry is generated.
    """
    GeometryGenerateMode = None
    MacroOrClassName = None
    ProjectOrAssemblyName = None
    pass

class SubassemblyGeometryGenerateMode():
    """
    Enumerates the way subassembly geometry can be generated.
    """
    pass

class SubassemblyLogicalNameType():
    """
    
    """
    pass

class SubassemblySideType():
    """
    An enumeration that specifies the material condition type.
    """
    pass

class SubassemblyTargetInfo(object):
    """
    Encapsulates a subassembly target information object.
    """
    AssemblyGroupName = None
    DisplayName = None
    LogicalName = None
    SubassemblyName = None
    TargetIds = None
    TargetToOption = None
    TargetType = None
    pass

class SubassemblyTargetInfoCollection(object):
    """
    This class encapsulates a collection of SubassemblyTargetInfo objects.
    """
    Count = None
    Item = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SubassemblyTargetInfo
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

class SubassemblyTargetToOption():
    """
    
    """
    pass

class SuperElevationBandLabelGroup(Entity):
    """
    
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all SuperElevationBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all SuperElevationBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of SuperElevationBandLabelGroup.
        """
        pass
    
    pass

class SuperelevationCriticalStation(object):
    """
    This class represents a super-elevation critical station on an Alignment object.
    """
    ParentAlignmentId = None
    Station = None
    StationType = None
    SuperelevationCurveName = None
    TransitionDescription = None
    TransitionRegionType = None
    def BreakSegment(self):
        """
        BreakSegment(crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType) -> SuperelevationCrossSegmentType
            Removes the super-elevation information from the specified segment type.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
        """
        pass
    
    
    def GetSlope(self):
        """
        GetSlope(crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType) -> SuperelevationCrossSegmentType
            Returns the slope at the specified segment type.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
        """
        pass
    
    
    def GetSmoothingLength(self):
        """
        GetSmoothingLength(crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType) -> SuperelevationCrossSegmentType
            Returns the smoothing length at the specified segment type.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
        """
        pass
    
    
    def IsGradeBreak(self):
        """
        IsGradeBreak(crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType) -> SuperelevationCrossSegmentType
            Returns whether there is a slope change from previous segment and next segment.
            Remarks: This value will always be true for the SuperelevationCrossSegmentType::BeginAlignment and SuperelevationCrossSegmentType::EndAlignment.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
        """
        pass
    
    
    def RemoveGradeBreak(self):
        """
        RemoveGradeBreak(crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType) -> SuperelevationCrossSegmentType
            Resets the slope value to its initialization value at the specified segment type.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
        """
        pass
    
    
    def SetSlope(self):
        """
        SetSlope(crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType, slope: System.Double) -> SuperelevationCrossSegmentType
            Sets the slope at the specified segment type.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
            slope: System.Double - The slope value of the current SuperelevationCriticalStation.
        """
        pass
    
    
    def SetSmoothingLength(self):
        """
        SetSmoothingLength(crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType, length: System.Double) -> SuperelevationCrossSegmentType
            Sets the smoothing length at the specified segment type.
            crossSegmentType: Autodesk.Civil.SuperelevationCrossSegmentType - The type of a Superelevation cross segment.
            length: System.Double - The smoothing length of the current SuperelevationCriticalStation.
        """
        pass
    
    pass

class SuperelevationCriticalStationCollection(object):
    """
    This class represents a collection of SuperelevationCriticalStation objects.
    """
    Count = None
    Item = None
    ParentAlignmentId = None
    def Add(self):
        """
        Add(station: System.Double, criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType) -> SuperelevationCriticalStationType
            Adds a SuperelevationCriticalStation of the specified transition type at the specified station.
            station: System.Double - The station value on the alignment object.
            criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType - The type of the critical station.
        Add(station: System.Double, criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType, attainmentRegionType: Autodesk.Civil.SuperelevationAttainmentRegionType) -> SuperelevationCriticalStationType
            Adds a SuperelevationCriticalStation of the specified transition type at the specified station.
            station: System.Double - The station value on the alignment object.
            criticalStationType: Autodesk.Civil.SuperelevationCriticalStationType - The type of the critical station.
            attainmentRegionType: Autodesk.Civil.SuperelevationAttainmentRegionType
        """
        pass
    
    
    def GetCriticalStationAt(self):
        """
        GetCriticalStationAt(station: System.Double, tolerance: System.Double) -> SuperelevationCriticalStation
            Returns the SuperelevationCriticalStation object at the specified station value.
            Remarks: If there is no SuperElevationCriticalStation at the specified station value, the method returns Null.If there more than one SuperElevationCriticalStation objects at the specified station, the method returns the first one in the collection, which is the previous curve bound station.
            station: System.Double - The station value on the alignment object.
            tolerance: System.Double - The tolerance value for the station value.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> SuperelevationCriticalStation
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def IsCriticalStation(self):
        """
        IsCriticalStation(station: System.Double, tolerance: System.Double) -> bool
            Returns whether there is a SuperelevationCriticalStation at the specified station value.
            station: System.Double - The station value on the alignment object.
            tolerance: System.Double - The tolerance value for the station value.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes the SuperelevationCriticalStation object from the collection at a specified index.
            index: System.Int32 - The index of critical station obejct in the current collection to be removed.
        """
        pass
    
    pass

class SuperelevationCurve(SECurve):
    """
    
    """

    pass

class SuperelevationCurveCollection(object):
    """
    
    """
    Count = None
    Item = None
    ParentAlignmentId = None
    def AddUserDefinedCurve(self):
        """
        AddUserDefinedCurve(startSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity, endSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity) -> SuperelevationCurve
            Adds user defined curve to this collection.
            startSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity - The start sub entity to create SuperelevationCurve.
            endSubEntity: Autodesk.Civil.DatabaseServices.AlignmentSubEntity - The end sub entity to create SuperelevationCurve.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> SuperelevationCurve
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def ImportSuperelevationDataFromFile(self):
        """
        ImportSuperelevationDataFromFile(fileName: System.String, alignmentId: ObjectId, acceptGarbage: System.Boolean)
            Imports superelevation data from specified file.
            fileName: System.String - The full path and name of the superelevation data file.
            alignmentId: ObjectId - The alignment which the superelevation data are imported to.
            acceptGarbage: System.Boolean - Accept or ignore if there is some garbage data in the file.
        """
        pass
    
    pass

class SuperelevationType():
    """
    
    """
    pass

class Surface(Entity):
    """
    The base class for TIN and grid surfaces and volume surfaces.  
    This class exposes the methods and properties common to TIN and grid surfaces,
    """
    Analysis = None
    BoundariesDefinition = None
    BuildOptions = None
    HasSnapshot = None
    IsOutOfDate = None
    IsSnapshotOutOfDate = None
    IsVolumeSurface = None
    Lock = None
    Masks = None
    Operations = None
    StyleId = None
    def CreateSnapshot(self):
        """
        CreateSnapshot()
            Creates a snapshot that contains the current state of points and triangles resulting from previous Surface operations. 
            A snapshot can improve the performance of Surface builds from subsequent operations.
            Remarks: You can create only one snapshot for each Surface.When a surface is built, previous surface operations are ignored and the surface build begins at the snapshot operation.
        """
        pass
    
    
    def ExportToDEM(self):
        """
        ExportToDEM(fileName: System.String, coordinateSystemCode: System.String, gridSpacing: System.Double, deteElevBy: Autodesk.Civil.ExportDetermineElevationType) -> ExportDetermineElevationType
            Exports the Surface to a DEM file.
            Remarks: If the target DEM file exists, its contents are deleted. If the method fails, the existing file will be empty.If the drawing has a coordinate system defined, the export uses that drawing coordinate system, and the coordinateSystemCode parameter is ignored.This version of ExportToDEM() does not specify a custom Null elevation.
            fileName: System.String - The full file path of the DEM file.
            coordinateSystemCode: System.String - The coordinate zone of the exported surface, using a Map Zone name.
            gridSpacing: System.Double - The horizontal spacing for DEM profile points.
            deteElevBy: Autodesk.Civil.ExportDetermineElevationType - Specifies how the elevations of the DEM file are determined from the exported surface.
        ExportToDEM(fileName: System.String, coordinateSystemCode: System.String, gridSpacing: System.Double, deteElevBy: Autodesk.Civil.ExportDetermineElevationType, useCustomNullElevationation: System.Boolean, customNullElevation: System.Single) -> ExportDetermineElevationType
            Exports the surface to a DEM file, with an optional custom value for null elevation.
            Remarks: If the target DEM file exists, its contents are deleted. If the method fails, the existing file will be empty.If the drawing has a coordinate system defined, the export uses that drawing coordinate system, and the coordinateSystemCode parameter is ignored.
            fileName: System.String - The full file path of the DEM file.
            coordinateSystemCode: System.String - The coordinate zone of the exported surface, using a Map Zone name.
            gridSpacing: System.Double - The horizontal spacing for the DEM profile points.
            deteElevBy: Autodesk.Civil.ExportDetermineElevationType - Specifies how the elevations of DEM file are determined from the exported surface.
            useCustomNullElevationation: System.Boolean - Specifies whether to use a custom value for null elevation.
            customNullElevation: System.Single - Specifies the default value for null elevation.
        """
        pass
    
    
    def FindDirectionAtXY(self):
        """
        FindDirectionAtXY(x: System.Double, y: System.Double) -> double
            Gets the direction of the Surface at the specified location (x, y).
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def FindElevationAtXY(self):
        """
        FindElevationAtXY(x: System.Double, y: System.Double) -> double
            Gets the elevation of the Surface at the specified location (x, y).
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def FindSlopeAtXY(self):
        """
        FindSlopeAtXY(x: System.Double, y: System.Double) -> double
            Gets the slope of the Surface at the specified location (x, y).
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def GetBoundedVolumes(self):
        """
        GetBoundedVolumes(polygon: Point3dCollection) -> SurfaceVolumeInfo
            Calculates the volume of an area defined by several points.
            Remarks: This method is equivalent to the overloadded method with datumElevation = 0.0.
            polygon: Point3dCollection - 
            The polygon specifies the area where the volumes are calculated.
            Since the polygon should be a closed one, the start point and the end point must be the same. 
            There must be more than 3 points in the Point3dCollection.
        GetBoundedVolumes(polygon: Point3dCollection, datumElevation: System.Double) -> SurfaceVolumeInfo
            Calculate the volume of an area defined by several points.
            polygon: Point3dCollection - 
            The polygon specifies the area where the volumes are calculated.
            Since the polygon should be a closed one, the start point and the end point must be the same. 
            There must be more than 3 points in the Point3dCollection.
            datumElevation: System.Double - 
            The volumes will be calculated from the specified datum elevation.
        """
        pass
    
    
    def GetGeneralProperties(self):
        """
        GetGeneralProperties() -> GeneralSurfaceProperties
            Gets the general properties of the surface.
            Remarks: The general properties of a surface include information about minimum and maximum x and y coordinates, elevation, and number of points.
        """
        pass
    
    
    def GetIntersectionPoint(self):
        """
        GetIntersectionPoint(startPoint: Point3d, dir: Vector3d) -> Point3d
            Gets the intersection point with surface by the specified point and vector.
            startPoint: Point3d
            dir: Vector3d
        """
        pass
    
    
    def Rebuild(self):
        """
        Rebuild()
            Rebuilds the surface by processing all the operations one by one in the list.
            Remarks: You can check whether the Surface needs to be rebuilt by checking the IsOutOfDate property.
        """
        pass
    
    
    def RebuildSnapshot(self):
        """
        RebuildSnapshot()
            Rebuilds the snapshot for the surface.
            Remarks: You can rebuild a snapshot if any of the operations that precede it in the surface operation list are changed or removed.
        """
        pass
    
    
    def RemoveSnapshot(self):
        """
        RemoveSnapshot()
            Removes the existing snapshot for the surface.
        """
        pass
    
    pass

class SurfaceAnalysis(object):
    """
    The SurfaceAnalysis class.
    This class encapsulates surface analysis data, and is accessed from the Surface.Analysis property.
    """
    def CreateWaterdrop(self):
        """
        CreateWaterdrop(location: Point2d, objectType: Autodesk.Civil.WaterdropObjectType) -> WaterdropObjectType
            Creates one or more polylines that represent a flow of water, and marks the start point of the path.  This method exposes the Water Drop command
            from the Civil 3D GUI.
            Remarks: If the location is on a peak, multiple Polyline2d or Polyline3d entities are created.
            If the location is on a flat area, no entity is created and the method returns an empty ObjectIdCollection object.
            Otherwise, only one Polyline2d or Polyline3d entity is created.
            The water drop polyline is created on the surface layer.
            location: Point2d - The location at which to create waterdrop object(s).
            objectType: Autodesk.Civil.WaterdropObjectType - WaterdropObjectType::Polyline2D creates polylines of type Autodesk.AutoCAD.Database.Polyline.WaterdropObjectType::Polyline3D creates polylines of type Autodesk.AutoCAD.Database.Polyline3d.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the SurfaceAnalysis
        """
        pass
    
    
    def GetContourData(self):
        """
        GetContourData() -> SurfaceAnalysisContourData
            Gets the surface contour analysis data for a Surface.
            Remarks: This method returns contour analysis data for a Surface.  Data only exists if it has been generated in the
            Surface Analysis tab.  Countours will appear in the GUI if the countour components of the surface style
            are set to visible, but the analysis data will be empty.  Data is generated from the Analysis tab on the
            Surface Properties dialog.
            Use SetContourData() to apply changes made to data returned by this method.
        """
        pass
    
    
    def GetDirectionData(self):
        """
        GetDirectionData() -> SurfaceAnalysisDirectionData
            Gets the surface direction analysis data for a Surface.
            Remarks: This method returns direction analysis data for a Surface.  Data only exists if it has been generated in the
            Surface Analysis tab.  Directions will appear in the GUI if the direction component of the surface style
            are set to visible, but the analysis data will be empty.  Data is generated from the Analysis tab on the
            Surface Properties dialog.
            Use SetDirectionData() to apply changes made to data returned by this method.
        """
        pass
    
    
    def GetElevationData(self):
        """
        GetElevationData() -> SurfaceAnalysisElevationData
            Gets the elevation analysis data for a Surface.
            Remarks: This method returns elevation analysis data for a Surface.  Data only exists if it has been generated in the
            Surface Analysis tab.  Elevations will appear in the GUI if the elevation component of the surface style
            are set to visible, but the analysis data will be empty.  Data is generated from the Analysis tab on the
            Surface Properties dialog.
            Use SetElevationData() to apply changes made to data returned by this method.
        """
        pass
    
    
    def GetSlopeArrowData(self):
        """
        GetSlopeArrowData() -> SurfaceAnalysisSlopeArrowData
            Gets the slope arrow analysis data for a Surface.
            Remarks: This method returns slope arrow analysis data for a Surface.  Data only exists if it has been generated in the
            Surface Analysis tab.  Slope arrows will appear in the GUI if the slope arrow component of the surface style
            are set to visible, but the analysis data will be empty.  Data is generated from the Analysis tab on the
            Surface Properties dialog.
            Use SetSlopeArrowData() to apply changes made to data returned by this method.
        """
        pass
    
    
    def GetSlopeData(self):
        """
        GetSlopeData() -> SurfaceAnalysisSlopeData
            Gets the slope analysis data for a Surface.
            Remarks: This method returns slope analysis data for a Surface.  Data only exists if it has been generated in the
            Surface Analysis tab.  Slopes will appear in the GUI if the slope component of the surface style
            are set to visible, but the analysis data will be empty.  Data is generated from the Analysis tab on the
            Surface Properties dialog.
            Use SetSlopeData() to apply changes made to data returned by this method.
        """
        pass
    
    
    def GetUserDefinedContourData(self):
        """
        GetUserDefinedContourData() -> SurfaceAnalysisUserDefinedContourData
            Gets an array which contains all the surface user-defined contour analysis data.
        """
        pass
    
    
    def GetWatershedData(self):
        """
        GetWatershedData() -> SurfaceAnalysisWatershedDataCollection
            Gets the watershed analysis data for a Surface.
            Remarks: This method returns watershed analysis data for a Surface.  Data only exists if it has been generated in the
            Surface Analysis tab.  Watersheds will appear in the GUI if the watershed component of the surface style
            are set to visible, but the analysis data will be empty.  Data is generated from the Analysis tab on the
            Surface Properties dialog.
            Use SetWatershedData() to apply changes made to data returned by this method.
        """
        pass
    
    
    def SetContourData(self):
        """
        SetContourData(analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisContourData) -> SurfaceAnalysisContourData
            Sets the surface contour analysis data for a Surface. Use this method to apply changes made to data returned by
            GetContourData().
            analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisContourData - An array that contains the contour analysis data for the Surface.
        """
        pass
    
    
    def SetDirectionData(self):
        """
        SetDirectionData(analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisDirectionData) -> SurfaceAnalysisDirectionData
            Sets the surface direction analysis data for a Surface. Use this method to apply changes made to data returned by
            GetDirectionData().
            analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisDirectionData - An array that contains the direction analysis data for the Surface.
        """
        pass
    
    
    def SetElevationData(self):
        """
        SetElevationData(analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisElevationData) -> SurfaceAnalysisElevationData
            Sets the surface elevation analysis data for a Surface. Use this method to apply changes made to data returned by
            GetElevationData().
            analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisElevationData - An array that contains the elevation analysis data for the Surface.
        """
        pass
    
    
    def SetSlopeArrowData(self):
        """
        SetSlopeArrowData(analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisSlopeArrowData) -> SurfaceAnalysisSlopeArrowData
            Sets the slope arrow analysis data for a Surface.  Use this method to apply changes made to data returned by
            GetSlopeArrowData().
            analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisSlopeArrowData - An array that contains the slope arrow analysis data for the Surface.
        """
        pass
    
    
    def SetSlopeData(self):
        """
        SetSlopeData(analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisSlopeData) -> SurfaceAnalysisSlopeData
            Sets the slope analysis data for a Surface. Use this method to apply changes made to data returned by
            GetSlopeData().
            analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisSlopeData - An array that contains the slope analysis data for the Surface.
        """
        pass
    
    
    def SetUserDefinedContourData(self):
        """
        SetUserDefinedContourData(analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisUserDefinedContourData) -> SurfaceAnalysisUserDefinedContourData
            Sets the user-defined contour analysis data for a Surface. Use this method to apply changes made to data returned by
            GetUserDefinedContourData().
            analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisUserDefinedContourData - An array that contains the user-defined contour analysis data for the Surface.
        """
        pass
    
    
    def SetWatershedData(self):
        """
        SetWatershedData(analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisWatershedDataCollection) -> SurfaceAnalysisWatershedDataCollection
            Sets the watershed analysis data for a Surface. Use this method to apply changes made to data returned by
            GetWatershedData().
            analysisData: Autodesk.Civil.DatabaseServices.SurfaceAnalysisWatershedDataCollection - A collection that contains the watershed analysis data for the Surface.
        """
        pass
    
    pass

class SurfaceAnalysisContourData(object):
    """
    This class encapsulates the properties of a single contour in a surface contour analysis.
    """
    ContourValue = None
    MaximumElevation = None
    MinimumElevation = None
    pass

class SurfaceAnalysisDirectionData(object):
    """
    This class encapsulates all the properties of a single direction in a direction analysis for a surface.
    """
    MaximumDirection = None
    MinimumDirection = None
    Scheme = None
    pass

class SurfaceAnalysisElevationData(object):
    """
    This class defines a single elevation region, specified by a minimum and maximum elevation.
    """
    MaximumElevation = None
    MinimumElevation = None
    Scheme = None
    pass

class SurfaceAnalysisSlopeArrowData(object):
    """
    This class encapsulates all the properties of the slope arrow surface analysis.
    Slope ranges are specified % grade, where 1.00 is 100%.  The color is an AutoCAD Color object.
    A Slope direction arrow analysis typically contains several slope arrow ranges.  The Surface.Analysis.GetSlopeArrowData() method
    returns an array of SurfaceAnalysisSlopeArrowData objects, one for each slope arrow range.
    """
    MaximumSlope = None
    MinimumSlope = None
    Scheme = None
    pass

class SurfaceAnalysisSlopeData(object):
    """
    This class encapsulates all the properties of a slope analysis of a Surface.
    """
    MaximumSlope = None
    MinimumSlope = None
    Scheme = None
    pass

class SurfaceAnalysisUserDefinedContourData(object):
    """
    This class encapsulates all the properties of a single user-defined contour in a Surface analysis.
    """
    Color = None
    Description = None
    Elevation = None
    LineTypeId = None
    LineWeight = None
    pass

class SurfaceAnalysisWatershedData(object):
    """
    This class encapsulates the properties of a watershed area in a surface watershed analysis.
    """
    AreaColor = None
    AreaHatchPatternName = None
    AreaID = None
    Description = None
    DrainsInto = None
    SegmentColor = None
    SegmentLineTypeId = None
    SegmentLineWeight = None
    Type = None
    Visible = None
    pass

class SurfaceAnalysisWatershedDataCollection(object):
    """
    This class represents a collection of SurfaceAnalysisWatershedData objects for a surface watershed analysis.
    """
    Count = None
    Item = None
    ParentSurfaceId = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SurfaceAnalysisWatershedData
            This method returns an enumerator which can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            This method returns an enumerator which can be use to enumerate this collection.
        """
        pass
    
    pass

class SurfaceBoundary(object):
    """
    This class defines a boundary object for a Surface.
    """
    BoundaryType = None
    Vertices = None
    pass

class SurfaceBreakline(object):
    """
    This class defines a TIN surface breakline.
    """
    BreaklineType = None
    Description = None
    Vertices = None
    def InsertIntoDrawing(self):
        """
        InsertIntoDrawing() -> ObjectId
            Inserts the breakline into the drawing as AutoCAD polylines.
        """
        pass
    
    pass

class SurfaceBuildOptions(object):
    """
    This class encapsulates options for Surface build operations.
    """
    CopyDeletedDependentObjects = None
    CrossingBreaklinesElevationOption = None
    ExecludeMaximumElevation = None
    ExecludeMinimumElevation = None
    MaximumAngleBetweenAdjacentTinLines = None
    MaximumElevation = None
    MaximumTriangleLength = None
    MinimumElevation = None
    NeedConvertBreaklines = None
    UseMaximumAngle = None
    UseMaximumTriangleLength = None
    pass

class SurfaceContourLabelGroup(Entity):
    """
    This class represents a surface countour label group.
    """
    IsLabelLineVisible = None
    IsMajorContourLabelVisible = None
    IsMinorContourLabelVisible = None
    IsUserContourLabelVisible = None
    LabelLinePoints = None
    MajorContourLabelStyleId = None
    MinorContourLabelStyleId = None
    RangeEnd = None
    RangeEndFromFeature = None
    RangeStart = None
    RangeStartFromFeature = None
    UserContourLabelStyleId = None
    def Create(self):
        """
        Create(surfaceId: ObjectId, labelLinePoints: Point2dCollection) -> ObjectId
            Creates a new instance of an SurfaceContourLabelGroup and adds it to the specified surface.
            Remarks: There are at least 2 points to compose the label line.
            surfaceId: ObjectId - The ObjectId of surface to which the label is attahed.
            labelLinePoints: Point2dCollection - The place in which the label is located.
        Create(surfaceId: ObjectId, labelLinePoints: Point2dCollection, majorContourlabelStyleId: ObjectId, minorContourlabelStyleId: ObjectId, userContourlabelStyleId: ObjectId) -> ObjectId
            Creates a new instance of an SurfaceContourLabelGroup and adds it to the specified surface.
            Remarks: There are at least 2 points to compose the label line.
            surfaceId: ObjectId - The ObjectId of surface to which the label is attached.
            labelLinePoints: Point2dCollection - The place where the label is located.
            majorContourlabelStyleId: ObjectId - The object id of label style for the major contour label.
            minorContourlabelStyleId: ObjectId - The object id of label style for the minor contour label.
            userContourlabelStyleId: ObjectId - The object id of label style for the user contour label.
        """
        pass
    
    
    def CreateMultipleAtInterval(self):
        """
        CreateMultipleAtInterval(surfaceId: ObjectId, labelLineStartPoint: Point2d, labelLineEndPoint: Point2d, interval: System.Double)
            Creates multiple SurfaceContourLabelGroup to a surface at a specified interval.
            surfaceId: ObjectId - The object id of surface to which the label is attached.
            labelLineStartPoint: Point2d - The start point of label line.
            labelLineEndPoint: Point2d - The end point of label line.
            interval: System.Double - The interval between the label groups along contours.
        CreateMultipleAtInterval(surfaceId: ObjectId, labelLineStartPoint: Point2d, labelLineEndPoint: Point2d, interval: System.Double, options: Autodesk.Civil.DatabaseServices.SurfaceContourLabelGroupCreateOption) -> SurfaceContourLabelGroupCreateOption
            Creates multiple SurfaceContourLabelGroup to a surface at a specified interval.
            surfaceId: ObjectId - The object id of surface to which the label is attached.
            labelLineStartPoint: Point2d - The start point of label line.
            labelLineEndPoint: Point2d - The end point of label line.
            interval: System.Double - The interval between the label groups along contours.
            options: Autodesk.Civil.DatabaseServices.SurfaceContourLabelGroupCreateOption - The other options for creation such as label style.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(surfaceId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection containing all the available contour label groups belonging to the specified surface.
            surfaceId: ObjectId - The ObjectId of surface to get the contour label groups for.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(surfaceId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection containing all the available contour label groups belonging to the specified surface.
            surfaceId: ObjectId - The ObjectId of surface.
        """
        pass
    
    
    def GetLabelLinePoint(self):
        """
        GetLabelLinePoint(index: System.Int32) -> Point2d
            Get one key point from label line by index
            index: System.Int32
        """
        pass
    
    
    def SetLabelLinePoint(self):
        """
        SetLabelLinePoint(index: System.Int32, __unnamed001: Point2d)
            Set one key point from label line by index
            index: System.Int32
            __unnamed001: Point2d
        """
        pass
    
    pass

class SurfaceContourLabelGroupCreateOption(object):
    """
    
    """
    MajorContourlabelStyleId = None
    MaskType = None
    MinorContourlabelStyleId = None
    ShowLabelLine = None
    ShowMajorContourlabelgroup = None
    ShowMinorContourlabelgroup = None
    ShowUserDefinedContourlabelgroup = None
    UserDefinedContourlabelStyleId = None
    pass

class SurfaceDefinitionAddFigureSurveyQueries(SurfaceOperationAddFigureSurveyQuery):
    """
    This class encapsulates the survey queries operation list on a surface.
    """
    def AddFigureSurveyQuery(self):
        """
        AddFigureSurveyQuery(surveyProjectGuid: System.Guid, surveyQueryGuid: System.Guid, queryChecksum: System.Int32, surfaceOpDescription: System.String, midOrdinateDis: System.Double) -> SurfaceOperationAddFigureSurveyQuery
            Adds a figure survey to a TinSurface object.
            surveyProjectGuid: System.Guid - The GUID of a survey project.
            surveyQueryGuid: System.Guid - The GUID of a point survey query.
            queryChecksum: System.Int32 - The checksum of a point survey query.
            surfaceOpDescription: System.String - The description of the operation.
            midOrdinateDis: System.Double - The mid-ordinate distance value to use.
        """
        pass
    
    pass

class SurfaceDefinitionAddPointSurveyQueries(SurfaceOperationAddPointSurveyQuery):
    """
    This class encapsulates the survey queries operation list on a surface
    """
    def AddPointSurveyQuery(self):
        """
        AddPointSurveyQuery(surveyProjectGuid: System.Guid, surveyQueryGuid: System.Guid, queryChecksum: System.Int32, surfaceOpDescription: System.String, midOrdinateDis: System.Double) -> SurfaceOperationAddPointSurveyQuery
            Adds a point survey to a TinSurface object.
            surveyProjectGuid: System.Guid - The GUID of a survey project.
            surveyQueryGuid: System.Guid - The GUID of a point survey query.
            queryChecksum: System.Int32 - The checksum of a point survey query.
            surfaceOpDescription: System.String - The description of the operation.
            midOrdinateDis: System.Double - The mid-ordinate distance value to use.
        """
        pass
    
    pass

class SurfaceDefinitionBoundaries(SurfaceOperationAddBoundary):
    """
    This class encapsulates the boundary operation list for a surface.
    """
    def AddBoundaries(self):
        """
        AddBoundaries(boundaryEntities: ObjectIdCollection, midOrdinateDistance: System.Double, boundaryType: Autodesk.Civil.SurfaceBoundaryType, useNonDestructiveBreakline: System.Boolean) -> SurfaceOperationAddBoundary
            Adds boundaries to the surface from a collection of entity ObjectIds.
            Remarks: The parameter useNonDestructiveBreakline is ignored for a GridVolumeSurface or TinSurface with a DataClip boundary type.When creating the DataClip/Outer boundary, the first ObjectId in boundaryEntities is used, and any other ObjectIds in the collection are ignored.The first boundary in the boundaryEntities should be closed when creating a DataClip boundary.
            boundaryEntities: ObjectIdCollection - A collection that contains the ObjectIds of entities used to define the surface boundaries.
            midOrdinateDistance: System.Double - When the boundary is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arc segments of the boundary.
            boundaryType: Autodesk.Civil.SurfaceBoundaryType - Specifies the surface boundary type.
            useNonDestructiveBreakline: System.Boolean - Spefifies whether to use non-destructive breaklines when the boundary is created.
        AddBoundaries(points: Point2dCollection, midOrdinateDistance: System.Double, boundaryType: Autodesk.Civil.SurfaceBoundaryType, useNonDestructiveBreakline: System.Boolean) -> SurfaceOperationAddBoundary
            Adds boundaries to the surface from a Point2dCollection.
            Remarks: The parameter useNonDestructiveBreakline is ignored for a GridVolumeSurface or TinSurface with a DataClip boundary type.For a DataClip boundary type, the order of points in the collection should define a closed polygon, and should not create edges that cross.  
            The first and last points must be the same.
            points: Point2dCollection - A collection that contains 2d points used to define surface boundaries.
            midOrdinateDistance: System.Double - When the boundary is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arc segments of the boundary.  This value must be greater than 0.
            boundaryType: Autodesk.Civil.SurfaceBoundaryType - Specifies the surface boundary type.
            useNonDestructiveBreakline: System.Boolean - Spefifies whether to use non-destructive breaklines when creating the boundary.
        AddBoundaries(points: Point3dCollection, midOrdinateDistance: System.Double, boundaryType: Autodesk.Civil.SurfaceBoundaryType, useNonDestructiveBreakline: System.Boolean) -> SurfaceOperationAddBoundary
            Adds boundaries to the surface from a Point3dCollection.
            Remarks: The parameter useNonDestructiveBreakline is ignored for a GridVolumeSurface or TinSurface with a DataClip boundary type.For a DataClip boundary type, the order of points in the collection should define a closed polygon, and should not create edges that cross.  
            The first and last points must be the same.
            points: Point3dCollection - A collection that contains 3d points used to define breaklines.
            midOrdinateDistance: System.Double - When the boundary is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arc segments of the boundary.
            boundaryType: Autodesk.Civil.SurfaceBoundaryType - Defines the surface boundary type.
            useNonDestructiveBreakline: System.Boolean - Spefifies whether use to non-destructive breaklines when creating the boundary.
        """
        pass
    
    pass

class SurfaceDefinitionBreaklines(SurfaceOperationAddBreakline):
    """
    This class encapsulates the breakline operation list for a surface.  Operations are held in the order they are performed on the surface.
    """
    def AddBreaklinesFromFile(self):
        """
        AddBreaklinesFromFile(filename: System.String) -> SurfaceOperationAddBreaklineFromFile
            Adds breaklines from a .flt file (ASCII file format), and maintains the link to the file.
            Remarks: This method maintains a link to the breakline file.  The FLT file will be re-read whenever the surface is rebuilt. 
            If you do not want to maintain a link, use ImportBreaklinesFromFile().
            filename: System.String - The path and name of the file used to create the breaklines.
        """
        pass
    
    
    def AddNonDestructiveBreaklines(self):
        """
        AddNonDestructiveBreaklines(breaklineEntities: ObjectIdCollection, midOrdinateDistance: System.Double) -> SurfaceOperationAddBreakline
            Adds non-destructive breaklines to a surface from a collection of entities.
            Remarks: When defining a non-destructive breakline, surface points are created at each vertex of the object and at each intersection of a surface triangle edge and the non-destructive breakline object.
            breaklineEntities: ObjectIdCollection - A collection of ObjectIds for entities used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
        AddNonDestructiveBreaklines(points: Point2dCollection, midOrdinateDistance: System.Double) -> SurfaceOperationAddBreakline
            Adds non-destructive breaklines to a surface from a collection of 2d points.
            Remarks: When defining a non-destructive breakline, surface points are created at each point and at each intersection of a surface triangle edge and the non-destructive breakline object.
            points: Point2dCollection - A collection that contains 2d points used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
        AddNonDestructiveBreaklines(points: Point3dCollection, midOrdinateDistance: System.Double) -> SurfaceOperationAddBreakline
            Adds non-destructive breaklines to a surface from a collection of 3d points.
            Remarks: When defining a non-destructive breakline, surface points are created at each point and at each intersection of a surface triangle edge and the non-destructive breakline object.
            points: Point3dCollection - A collection of 3d points used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
        """
        pass
    
    
    def AddProximityBreaklines(self):
        """
        AddProximityBreaklines(breaklineEntities: ObjectIdCollection, midOrdinateDistance: System.Double) -> SurfaceOperationAddBreakline
            Adds proximity breaklines to a surface from an ObjectId collection.
            Remarks: This method creates proximity breaklines that reference surface points in proximity to the vertices of the breaklineEntities as the breakline.
            breaklineEntities: ObjectIdCollection - A collection of entity ObjectIds used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
        AddProximityBreaklines(points: Point2dCollection, midOrdinateDistance: System.Double) -> SurfaceOperationAddBreakline
            Adds proximity breaklines to a surface from a collection of 2d points.
            points: Point2dCollection - A collection of 2d points used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
        AddProximityBreaklines(points: Point3dCollection, midOrdinateDistance: System.Double) -> SurfaceOperationAddBreakline
            Adds proximity breaklines to a surface from a collection of 3d points.
            points: Point3dCollection - A collection of 3d points used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
        """
        pass
    
    
    def AddStandardBreaklines(self):
        """
        AddStandardBreaklines(breaklineEntities: ObjectIdCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddBreakline
            Adds standard breaklines to the surface fromm a collection of entities.
            Remarks: When defining a standard, the X, Y, and Z coordinates of each vertex on the polyline that you select are converted into TIN vertices.The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.Set a parameter to  0 to ignore it.
            breaklineEntities: ObjectIdCollection - A collection of ObjectIds for entities used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a breakline is greater than the maximumDistance, then points are added along the breakline at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        AddStandardBreaklines(points: Point2dCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddBreakline
            Adds standard breaklines to the surface from a collection of 2d points.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.Set a parameter to  0 to ignore it.
            points: Point2dCollection - A collection of 2d points used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a breakline is greater than the maximumDistance, then points are added along the breakline at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        AddStandardBreaklines(points: Point3dCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddBreakline
            Adds standard breaklines to the surface from a collection of 3d points.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.Set a parameter to  0 to ignore it.
            points: Point3dCollection - A collection of 3d points used to create breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a breakline is greater than the maximumDistance, then points are added along the breakline at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        """
        pass
    
    
    def AddWallBreaklines(self):
        """
        AddWallBreaklines(creationData: Autodesk.Civil.DatabaseServices.WallBreaklineCreationData, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddBreakline
            Adds wall breaklines to a surface, specifying a single elevation for all vertices.
            Remarks: Set a parameter to  0 to ignore it.
            creationData: Autodesk.Civil.DatabaseServices.WallBreaklineCreationData - An array of WallBreaklineCreationData objects that define breakline entities, offset side and the elevation value for each vertex, used to create wall breaklines.
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a breakline is greater than the maximumDistance, then points are added along the breakline at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        AddWallBreaklines(creationData: Autodesk.Civil.DatabaseServices.WallBreaklineCreationDataEx, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddBreakline
            Adds wall breaklines to a surface, specifiying elevations for each vertex.
            Remarks: Set a parameter to  0 to ignore it.
            creationData: Autodesk.Civil.DatabaseServices.WallBreaklineCreationDataEx - An array of WallBreaklineCreationDataEx objects that define breakline entities, offset side and individual elevation for each vertex, used to create wall breaklines. 
            midOrdinateDistance: System.Double - When the breakline is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a breakline is greater than the maximumDistance, then points are added along the breakline at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        """
        pass
    
    
    def ImportBreaklinesFromFile(self):
        """
        ImportBreaklinesFromFile(filename: System.String) -> SurfaceOperationAddBreakline
            Adds breaklines from a .flt file (ASCII file format).
            Remarks: All breaklines in the FLT file are copied into the surface as Add SurfaceOperationAddBreakline operations.  After the import, the FLT file is no longer referenced. If you want to maintain the link, use AddBreaklinesFromFile().
            filename: System.String - The path and name of the file used to create the breaklines.
        """
        pass
    
    pass

class SurfaceDefinitionContours(SurfaceOperationAddContour):
    """
    This class encapsulates the contour operation list on the surface.
    """
    def AddContours(self):
        """
        AddContours(boundaryEntities: ObjectIdCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddContour
            Adds contours to a surface from entities in an ObjectIdCollection.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.
            boundaryEntities: ObjectIdCollection - A collection of ObjectIds used to create contours.
            midOrdinateDistance: System.Double - When the contour is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a contour is greater than the maximumDistance, then points are added along the contour at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        AddContours(points: Point2dCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddContour
            Adds contours to a surface from a collection of 2d points.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.
            points: Point2dCollection - A collection of 2d points used to create contours.
            midOrdinateDistance: System.Double - When the contour is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a contour is greater than the maximumDistance, then points are added along the contour at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        AddContours(points: Point3dCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double) -> SurfaceOperationAddContour
            Adds contours to a surface from a collection of 3d points.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.
            points: Point3dCollection - A collection of 3d points used to create contours.
            midOrdinateDistance: System.Double - When the contour is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a contour is greater than the maximumDistance, then points are added along the contour at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
        AddContours(boundaryEntities: ObjectIdCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double, options: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationAddContour
            Adds contours to a surface from entities in an ObjectIdCollection, and minimizes flat areas.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.If all the properties in options are false, the parameter is ignored.
            boundaryEntities: ObjectIdCollection - A collection of ObjectIds used to create contours.
            midOrdinateDistance: System.Double - When the contour is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a contour is greater than the maximumDistance, then points are added along the contour at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
            options: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions - Specifies the options for minimizing flat areas on a surface.
        AddContours(points: Point2dCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double, options: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationAddContour
            Adds contours to a surface from a 2d point collection, and minimizes flat areas.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.If all the properties in options are false, the parameter is ignored.
            points: Point2dCollection - A collection of 2d points used to create contours.
            midOrdinateDistance: System.Double - When the contour is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a contour is greater than the maximumDistance, then points are added along the contour at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
            options: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions - Specifies the options for minimizing flat areas on a surface.
        AddContours(points: Point3dCollection, midOrdinateDistance: System.Double, maximumDistance: System.Double, weedingDistance: System.Double, weedingAngle: System.Double, options: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationAddContour
            Adds contours to the surface from a 3d point collection, and minimizes flat areas.
            Remarks: The weeding factors ignore both vertices that are closer together than the distance factor and vertices that deflect less than the angle factor.If all the properties in options are false, the parameter is ignored.
            points: Point3dCollection - A collection contains the 3d points used to define contour boundaries.
            midOrdinateDistance: System.Double - When the contour is defined from a polyline with curves, the midOrdinateDistance value is used to tessellate the arcs in the polyline.
            maximumDistance: System.Double - Specifies the maximum distance between vertices. If the distance between vertices on a contour is greater than the maximumDistance, then points are added along the contour at equal intervals that are less than or equal to the maximumDistance.
            weedingDistance: System.Double - The distance value for the weeding factor.
            weedingAngle: System.Double - The angle value for the weeding factor.
            options: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions - Specifies the options for minimizing flat areas on a surface.
        """
        pass
    
    pass

class SurfaceDefinitionDEMFiles(SurfaceOperationAddDEMFile):
    """
    This class encapsulates the DEMfile operation list on a surface.
    """
    def AddDEMFile(self):
        """
        AddDEMFile(filename: System.String) -> SurfaceOperationAddDEMFile
            Adds DEM file data to a surface.
            filename: System.String - The name and path of an existing DEM file.
        AddDEMFile(filename: System.String, useCustomNullElevation: System.Boolean, customeNullElevation: System.Double) -> SurfaceOperationAddDEMFile
            Adds DEM file data to a surface with custom null elevation information.
            filename: System.String - The name and path of an existing DEM file.
            useCustomNullElevation: System.Boolean - Specifies whether use a custom null elevation.
            customeNullElevation: System.Double - The value to use for null elevation.
        AddDEMFile(filename: System.String, coordinateSystemCode: System.String, useCustomNullElevation: System.Boolean, customeNullElevation: System.Double) -> SurfaceOperationAddDEMFile
            Adds DEM file data to a surface with custom null elevation and coordinate system information.
            Remarks: If the DEM file coordinate system is different from the current coordinate system of the drawing, and you are adding it to a TIN surface, you can specify a coordinate system for the DEM file. The coordinate system you specify for the DEM file should match the data defined in the DEM file itself.DEM files cannot be transformed for grid surfaces.The coordinateSystemCode value "" means that no transformation is needed.
            filename: System.String - The name and path of an existing DEM file.
            coordinateSystemCode: System.String - The coordinate system code to transform the data in the DEM file.  For a GridSurface, this parameter must be an empty string "".
            useCustomNullElevation: System.Boolean - Specifies whether use custom null elevation.
            customeNullElevation: System.Double - The value to use for null elevation.
        """
        pass
    
    pass

class SurfaceDefinitionDrawingObjects(SurfaceOperationAddDrawingObject):
    """
    This class encapsulates drawing object addition operations on a surface.
    """
    def AddFrom3DFaces(self):
        """
        AddFrom3DFaces(face3DIds: ObjectIdCollection, needMaintainEdge: System.Boolean, description: System.String) -> SurfaceOperationAdd3DFaces
            Creates surface point data from AutoCAD 3DFace objects.
            Remarks: The XYZ coordinates of each object's endpoints are used to define surface points.
            face3DIds: ObjectIdCollection - An ObjectIdCollection of AutoCAD 3DFace objects from which the surface point data will be added.
            needMaintainEdge: System.Boolean - Specifies whether to define the Autodesk Civil 3D triangle edges based on the edges defined in the original AutoCAD object.
            description: System.String - Specifies the description for the point data to be created.
        AddFrom3DFaces(points: Point3dCollection, edges: System.Collections.Generic.IEnumerable, description: System.String) -> SurfaceOperationAdd3DFaces
            Creates point data from points and edge information.
            Remarks: The value of an edge is the index of an item in points.
            points: Point3dCollection - Specifies the point information.
            edges: System.Collections.Generic.IEnumerable - Specifies the edge information.
            description: System.String - Specifies the description for the point data to be created.
        """
        pass
    
    
    def AddFromBlocks(self):
        """
        AddFromBlocks(blockIds: ObjectIdCollection, description: System.String) -> SurfaceOperationAddDrawingObject
            Creates point data from AutoCAD Block Reference objects.
            Remarks: The XYZ coordinates of the insertion point for each block are used to define the surface point.
            blockIds: ObjectIdCollection - An ObjectIdCollection of AutoCAD block reference objects from which the surface point data will be added.
            description: System.String - Specifies the description for the point data to be created.
        """
        pass
    
    
    def AddFromLines(self):
        """
        AddFromLines(lineIds: ObjectIdCollection, needMaintainEdge: System.Boolean, description: System.String) -> SurfaceOperationAddDrawingObject
            Creates surface point data from AutoCAD Line objects.
            Remarks: The XYZ coordinates of each line's endpoints are used to define surface points.
            lineIds: ObjectIdCollection - An ObjectIdCollection of AutoCAD Line objects from which the surface point data will be added.
            needMaintainEdge: System.Boolean - Specifies whether to define the Autodesk Civil 3D triangle edges based on the edges defined in the original AutoCAD object.
            description: System.String - Specifies the description for the point data to be created.
        """
        pass
    
    
    def AddFromPoints(self):
        """
        AddFromPoints(pointIds: ObjectIdCollection, description: System.String) -> SurfaceOperationAddDrawingObject
            Creates surface point data from AutoCAD Point objects.
            Remarks: The XYZ coordinates of each Point3D are used to define the surface point.
            pointIds: ObjectIdCollection - An ObjectIdCollection of AutoCAD Point3d objects from which the surface point data will be added.
            description: System.String - Specifies the description for the point data to be created.
        """
        pass
    
    
    def AddFromPolyFaces(self):
        """
        AddFromPolyFaces(polyfaceIds: ObjectIdCollection, needMaintainEdge: System.Boolean, description: System.String) -> SurfaceOperationAddDrawingObject
            Creates surface point data from AutoCAD PolyFaceMesh objects.
            Remarks: The XYZ coordinates of each object's endpoints are used to define surface point.
            polyfaceIds: ObjectIdCollection - An ObjectIdCollection of AutoCAD PolyFaceMesh objects from which the surface point data will be added.
            needMaintainEdge: System.Boolean - Specifies whether to define the Autodesk Civil 3D triangle edges based on the edges defined in the original AutoCAD object.
            description: System.String - Specifies the description for the point data to be created.
        """
        pass
    
    
    def AddFromTexts(self):
        """
        AddFromTexts(textIds: ObjectIdCollection, description: System.String) -> SurfaceOperationAddDrawingObject
            Creates surface point data from AutoCAD Text objects.
            Remarks: The XYZ coordinates of each text insertion point are used to define the surface point.
            textIds: ObjectIdCollection - An ObjectIdCollection of AutoCAD Text objects from which the surface point data will be added.
            description: System.String - Specifies the description for the point data to be created.
        """
        pass
    
    pass

class SurfaceDefinitionPointFiles(SurfaceOperationAddPointFile):
    """
    This class encapsulates the point files operation list for a surface.
    """
    def AddPointFile(self):
        """
        AddPointFile(pointFilename: System.String, pointFileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat) -> SurfaceOperationAddPointFile
            Adds points from a point file to the surface.
            pointFilename: System.String - The full path and name of the point file.
            pointFileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat - The file format for the point file.  You can get a collection of supported point file formats by using PointFileFormatCollection.GetPointFileFormats().
        AddPointFile(pointFilename: System.String, pointFileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat, useAdjustedElevation: System.Boolean, shouldTransformPointCoordinate: System.Boolean, shouldExpandCoordinateData: System.Boolean) -> SurfaceOperationAddPointFile
            Adds the point file to the surface.
            Remarks: The shouldExpandCoordinateData and useAdjustedElevation value are ignored if they are not supported in the point file format.
            pointFilename: System.String - The full path of the point file.
            pointFileFormat: Autodesk.Civil.DatabaseServices.PointFileFormat - The file format for the point file.  You can get a collection of supported point file formats by using PointFileFormatCollection.GetPointFileFormats().
            useAdjustedElevation: System.Boolean - Specifies whether to adjust the point elevation values.
            shouldTransformPointCoordinate: System.Boolean - Specifies whether to transform the points in the file.
            shouldExpandCoordinateData: System.Boolean - Specifies whether to calculate the coordinate data properties of the points, such as degrees, minutes, seconds, and hemisphere for latitude and longitude.
        """
        pass
    
    pass

class SurfaceDefinitionPointGroups(SurfaceOperationAddPointGroup):
    """
    This class encapsulates the point group operation list on a surface.
    """
    def AddPointGroup(self):
        """
        AddPointGroup(pointGroupId: ObjectId) -> SurfaceOperationAddPointGroup
            Adds a point group to a surface.
            pointGroupId: ObjectId - The ObjectId of the point group to be added to the surface.
        """
        pass
    
    pass

class SurfaceElevationLabel(Entity):
    """
    This class represents a surface slope label.
    """
    Location = None
    def Create(self):
        """
        Create(surfaceId: ObjectId, location: Point2d) -> ObjectId
            Creates a new instance of an OnePoint SurfaceElevationLabel.
            surfaceId: ObjectId - The object id of surface to which the label is attahed.
            location: Point2d - The place in which the label is located.
        Create(surfaceId: ObjectId, location: Point2d, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId
            Creates a new instance of an OnePoint SurfaceElevationLabel.
            surfaceId: ObjectId - The object id of surface to which the label is attached.
            location: Point2d - The place in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
            markerStyleId: ObjectId - The object id of anchor marker style for the label.
        """
        pass
    
    
    def GetAvailableSurfaceElevationLabelIds(self):
        """
        GetAvailableSurfaceElevationLabelIds(surfaceId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of elevation labels for the specified surface.
            surfaceId: ObjectId - ObjectId of the surface where the labels are located.
        """
        pass
    
    
    def GetAvailableSurfaceElevationLabels(self):
        """
        GetAvailableSurfaceElevationLabels(surfaceId: ObjectId) -> ObjectIdCollection
            Returns the ObjectId collection of elevation labels on the specified surface.
            surfaceId: ObjectId - ObjectId of the surface where the labels are located.
        """
        pass
    
    pass

class SurfaceMask(object):
    """
    This class encapsulates a mask on a surface.
    """
    Description = None
    IsRenderOnly = None
    Linkages = None
    MaterialId = None
    MidOrdinateDistance = None
    Name = None
    ObjectId = None
    SurfaceId = None
    Type = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the SurfaceMask
        """
        pass
    
    pass

class SurfaceMaskCollection(object):
    """
    This class encapsulates a surface's masks list.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(creationData: Autodesk.Civil.DatabaseServices.SurfaceMaskCreationData) -> SurfaceMask
            Adds a SurfaceMask to the collection.
            creationData: Autodesk.Civil.DatabaseServices.SurfaceMaskCreationData
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> SurfaceMask
            Implements the method declared in the IEnumerable<T> interface. 
            This method return an enumertor which can be used to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. 
            This method return an enumertor which can be used to enumerate this collection.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf(mask: Autodesk.Civil.DatabaseServices.SurfaceMask) -> SurfaceMask
            Gets the index of the specified mask in the mask collection.
            mask: Autodesk.Civil.DatabaseServices.SurfaceMask
        """
        pass
    
    
    def MoveDown(self):
        """
        MoveDown(mask: Autodesk.Civil.DatabaseServices.SurfaceMask) -> SurfaceMask
            Moves the specfied mask to its next position in the mask collection.
            Remarks: The next mask will be moved to the position of mask.
            mask: Autodesk.Civil.DatabaseServices.SurfaceMask
        """
        pass
    
    
    def MoveUp(self):
        """
        MoveUp(mask: Autodesk.Civil.DatabaseServices.SurfaceMask) -> SurfaceMask
            Moves the specfied mask to its previous position in the mask collection.
            Remarks: The previous mask will be moved to the position of mask.
            mask: Autodesk.Civil.DatabaseServices.SurfaceMask
        """
        pass
    
    
    def Remove(self):
        """
        Remove(mask: Autodesk.Civil.DatabaseServices.SurfaceMask) -> SurfaceMask
            Removes the specified mask from the mask collection.
            mask: Autodesk.Civil.DatabaseServices.SurfaceMask
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes the mask at the specified index in the mask collection.
            index: System.Int32
        """
        pass
    
    
    def Swap(self):
        """
        Swap(mask1: Autodesk.Civil.DatabaseServices.SurfaceMask, mask2: Autodesk.Civil.DatabaseServices.SurfaceMask) -> SurfaceMask
            Swaps the indexs of two specified masks in the mask collection, changing their order.
            mask1: Autodesk.Civil.DatabaseServices.SurfaceMask
            mask2: Autodesk.Civil.DatabaseServices.SurfaceMask
        """
        pass
    
    pass

class SurfaceMaskCreationData(object):
    """
    This class specifies the informations required to create a surface mask.
    """
    Description = None
    IsRenderOnly = None
    Linkages = None
    MaterialId = None
    MidOrdinateDistance = None
    Name = None
    SurfaceId = None
    Type = None
    pass

class SurfaceMaskType():
    """
    Defines the surface mask type.
    """
    pass

class SurfaceMinimizeFlatAreaOptions():
    """
    
    """
    AddPointsToEdges = None
    AddPointsToTriangles = None
    FillGaps = None
    SwapEdges = None
    pass

class SurfaceOperation(SurfaceOperationAddBoundary):
    """
    The base class for all surface operations.  This class encapsulates the common methods such as moveup, movedown, etc. for surface operations.
    """
    Enabled = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the SurfaceOperation
        """
        pass
    
    
    def MoveDown(self):
        """
        MoveDown()
            Moves the operation one position down in the operation list.
        """
        pass
    
    
    def MoveToBottom(self):
        """
        MoveToBottom()
            Moves the operation to the bottom of the operation list.
        """
        pass
    
    
    def MoveToTop(self):
        """
        MoveToTop()
            Moves the operation to the top of the operation list.
        """
        pass
    
    
    def MoveUp(self):
        """
        MoveUp()
            Moves the operation one position up in the operation list.
        """
        pass
    
    pass

class SurfaceOperationAdd3DFaces(SurfaceOperation):
    """
    This class encapsulates the operation of adding 3D faces to surface.
    """


    pass

class SurfaceOperationAddBoundary(SurfaceOperation):
    """
    This class encapsulates boundary addition operations for a surface.
    """
    BoundaryType = None
    Count = None
    IsTrimmed = None
    Item = None
    MidOrdinateDistance = None
    Name = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SurfaceBoundary
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def InsertIntoDrawing(self):
        """
        InsertIntoDrawing() -> ObjectIdCollection
            Inserts boundaries in the current operation into the drawing as AutoCAD polylines.
        """
        pass
    
    pass

class SurfaceOperationAddBreakline(SurfaceOperation):
    """
    This class encapsulates the operation of adding breaklines to a surface.  Methods that import or create breaklines on a surface
    return this object, which contains all breaklines created in the operation.
    """
    BreaklineType = None
    Count = None
    Description = None
    Item = None
    MaximumDistance = None
    MidOrdinateDistance = None
    WeedingAngle = None
    WeedingDistance = None
    def GetEnumerator(self):
        """
        GetEnumerator() -> SurfaceBreakline
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator for this collection.
        """
        pass
    
    
    def InsertIntoDrawing(self):
        """
        InsertIntoDrawing() -> ObjectIdCollection
            Inserts breaklines in the current operation into the drawing as AutoCAD polylines.
        """
        pass
    
    pass

class SurfaceOperationAddBreaklineFromFile(SurfaceOperation):
    """
    This class encapsulates the operation of importing breaklines from file.
    """
    BreaklineFileName = None
    Description = None

    pass

class SurfaceOperationAddContour(SurfaceOperation):
    """
    This class encapsulates the operation of adding contours to a surface.
    """
    Description = None
    MaximumDistance = None
    MidOrdinateDistance = None
    Summary = None
    WeedingAngle = None
    WeedingDistance = None
    def InsertIntoDrawing(self):
        """
        InsertIntoDrawing() -> ObjectIdCollection
            Inserts contour data into the drawing as AutoCAD polylines.
        """
        pass
    
    pass

class SurfaceOperationAddDEMFile(SurfaceOperation):
    """
    This class encapsulates the operation of adding DEM file to a surface.
    """
    CoordinateSystemCode = None
    CustomeNullElevation = None
    DEMFileName = None
    FileSize = None
    UseCustomNullElevation = None

    pass

class SurfaceOperationAddDrawingObject(SurfaceOperation):
    """
    This class encapsulates the operation of adding point data to a surface from AutoCAD Drawing Objects.
    """
    Description = None
    MaintainEdge = None
    ObjectType = None

    pass

class SurfaceOperationAddFigureSurveyQuery(SurfaceOperation):
    """
    This class encapsulates the operation of adding a figure survey query to a TinSurface.
    """


    pass

class SurfaceOperationAddGridPoint(SurfaceOperation):
    """
    This class encapsulates the operation of adding a point to a GridSurface.
    """
    Elevation = None
    Location = None

    pass

class SurfaceOperationAddImxFile(SurfaceOperation):
    """
    This class encapsulates the operation of adding Imx file to a surface.
    """
    DoCoordinateConversion = None
    FileSize = None
    GitHash = None
    ImxFileName = None
    Query = None
    SurfaceName = None

    pass

class SurfaceOperationAddLine(SurfaceOperation):
    """
    This class encapsulates the operation of adding a line to a TinSurface.
    """
    EndLocation = None
    StartLocation = None

    pass

class SurfaceOperationAddPointFile(SurfaceOperation):
    """
    This class encapsulates the operation of adding a point file to a surface.
    """
    FileFormat = None
    PointFileName = None
    ShouldExpandCoordinateData = None
    ShouldTransformPointCoordinates = None
    UseAdjustedElevation = None

    pass

class SurfaceOperationAddPointGroup(SurfaceOperation):
    """
    This class encapsulates the operation of adding point groups to a surface.
    """
    PointGroupId = None

    pass

class SurfaceOperationAddPointSurveyQuery(SurfaceOperation):
    """
    This class encapsulates the operation of adding a point survey query to a TinSurface.
    """


    pass

class SurfaceOperationAddSurveyQuery(SurfaceOperation):
    """
    This class encapsulates the operation of adding a point/figure survey query to a TinSurface.
    """
    Description = None
    ProjectGuid = None
    ProjectName = None
    QueryGuid = None
    QueryName = None
    SurveyQueryType = None

    pass

class SurfaceOperationAddTinFile(SurfaceOperation):
    """
    This class encapsulates the operation of adding a TIN file to a surface.
    """
    FileSize = None
    TinFileName = None

    pass

class SurfaceOperationAddTinMultipleVertices(SurfaceOperation):
    """
    This class encapsulates the operation of adding multiple vertices to a TinSurface.
    """
    Locations = None

    pass

class SurfaceOperationAddTinVertex(SurfaceOperation):
    """
    This class encapsulates the operation of adding a vertex to a TinSurface.
    """
    Location = None

    pass

class SurfaceOperationAddXmlFile(SurfaceOperation):
    """
    This class encapsulates the operation of adding data from an XML file to a surface.
    """
    XmlFileName = None

    pass

class SurfaceOperationCollection(object):
    """
    This class encapsulates the operations' list on the surface in order.
    """
    Count = None
    Item = None
    def DisableOperations(self):
        """
        DisableOperations(operationClassType: System.Type)
            Disables all the operations with the specific type in the collection.
            Remarks: If there are any status changes for those operations, the surface will be out-of-date, user needs to rebuild the surface manually.
            operationClassType: System.Type - The type of the specific surface operation class which should derive from SurfaceOperation.
        """
        pass
    
    
    def EnableOperations(self):
        """
        EnableOperations(operationClassType: System.Type)
            Enables all the operations with the specific type in the collection.
            Remarks: If there are any status changes for those operations, the surface will be out-of-date, user needs to rebuild the surface manually.
            operationClassType: System.Type - The type of the specific surface operation class which should derive from SurfaceOperation.
        """
        pass
    
    
    def GetOperationStatus(self):
        """
        GetOperationStatus(operationClassType: System.Type) -> SurfaceOpeartionStatusType
            Gets the current status of the surface operation with specific type.
            Remarks: Returns Varies when the operations with specific type in current collection contain both active and inactive status.Returns None when there is no such opeartion in current collection.
            operationClassType: System.Type - The type of the specific surface operation class which should derive from SurfaceOperation.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(operation: Autodesk.Civil.DatabaseServices.SurfaceOperation) -> SurfaceOperation
            Removes an operation from the operation collection.
            operation: Autodesk.Civil.DatabaseServices.SurfaceOperation - The operation in the current collection that needs to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(index: System.Int32)
            Removes the operation at the specified position in the operation collection
            index: System.Int32 - The position of operation in the current collection that needs to be removed.
        """
        pass
    
    
    def Swap(self):
        """
        Swap(firstOperation: Autodesk.Civil.DatabaseServices.SurfaceOperation, secondOperation: Autodesk.Civil.DatabaseServices.SurfaceOperation) -> SurfaceOperation
            Swaps the order for two operations in the current collection.
            firstOperation: Autodesk.Civil.DatabaseServices.SurfaceOperation - The first operation in the current collection that needs to be swapped.
            secondOperation: Autodesk.Civil.DatabaseServices.SurfaceOperation - The second operation in the current collection that needs to be swapped.
        """
        pass
    
    
    def SwapAt(self):
        """
        SwapAt(firstIndex: System.Int32, secondIndex: System.Int32)
            Swaps the order for two operations at the specified position in the list.
            firstIndex: System.Int32 - The first position of operation in the current collection that needs to be swapped.
            secondIndex: System.Int32 - The second position of operation in the current collection that needs to be swapped.
        """
        pass
    
    pass

class SurfaceOperationCreateByCropping(SurfaceOperation):
    """
    This class encapsulates the operation of creating surface by cropping from another surface.
    """
    CroppedBoundary = None
    SourceFileName = None

    pass

class SurfaceOperationCreatedFromCorridor(SurfaceOperation):
    """
    This class encapsulates the operation of being created from a corridor.
    """
    CorridorId = None
    CorridorSurfaceName = None

    pass

class SurfaceOperationDeleteGridPoint(SurfaceOperation):
    """
    This class encapsulates the operation of deleting a GridSurface point.
    """
    Location = None

    pass

class SurfaceOperationDeleteLine(SurfaceOperation):
    """
    This class encapsulates the operation of deleting a line from a Surface.
    """
    MidLocation = None

    pass

class SurfaceOperationDeleteMultipleGridPoints(SurfaceOperation):
    """
    This class encapsulates the operation of deleting multiple points from a GridSurface.
    """
    Locations = None

    pass

class SurfaceOperationDeleteMultipleLines(SurfaceOperation):
    """
    This class encapsulates the operation of deleting multiple lines from a Surface.
    """
    MidLocations = None

    pass

class SurfaceOperationDeleteMultipleTinVertices(SurfaceOperation):
    """
    This class encapsulates the operation of deleting multiple TinSurface vertices.
    """
    Locations = None

    pass

class SurfaceOperationDeleteTinVertex(SurfaceOperation):
    """
    This class encapsulates the operation of deleting a TinSurface vertex.
    """
    Location = None

    pass

class SurfaceOperationMinimizeFlatAreas(SurfaceOperation):
    """
    This class encapsulates the operation of minimizing the flat areas for a TinSurface.
    """
    CountOfAddedPoints = None
    CountOfRemovedPoints = None
    MinimizeFlatAreaOptions = None

    pass

class SurfaceOperationModifyGridPointElevation(SurfaceOperation):
    """
    This class encapsulates the operation of changing the elevation of a GridSurface point.
    """
    Location = None
    NewElevation = None

    pass

class SurfaceOperationModifyMultipleGridPointsElevation(SurfaceOperation):
    """
    This class encapsulates the operation of changing the elevation of multiple GridSurface points.
    """
    Elevation = None
    IsDeltaElevation = None
    Locations = None

    pass

class SurfaceOperationModifyMultipleTinVerticesElevation(SurfaceOperation):
    """
    This class encapsulates the operation of changing the elevation of multiple TinSurface vertices.
    """
    Elevation = None
    IsDeltaElevation = None
    Locations = None

    pass

class SurfaceOperationModifyTinVertexElevation(SurfaceOperation):
    """
    This class encapsulates the operation of changing the elevation of a TinSurface vertex.
    """
    Location = None
    NewElevation = None

    pass

class SurfaceOperationMoveTinVertex(SurfaceOperation):
    """
    This class encapsulates the operation of moving a TinSurface vertex on the XY plane.
    """
    NewLocation = None
    OriginalLocation = None

    pass

class SurfaceOperationPasteSurface(SurfaceOperation):
    """
    This class encapsulates the operation of pasting a surface.
    """
    SurfaceId = None

    pass

class SurfaceOperationRaise(SurfaceOperation):
    """
    This class encapsulates the operation of raising or lowering a surface.
    """
    DeltaElevation = None

    pass

class SurfaceOperationSimplify(SurfaceOperation):
    """
    This class encapsulates the operation of simplifying a TinSurface object.
    """
    CountOfRemovedPoints = None
    SimplifyOptions = None

    pass

class SurfaceOperationSmooth(SurfaceOperation):
    """
    This class encapsulates the operation of smoothing a TinSurface object.
    """
    OutPutPoints = None
    SurfaceSmoothMethod = None

    pass

class SurfaceOperationSwapEdge(SurfaceOperation):
    """
    This class encapsulates the operation of swapping an edge of a TinSurface.
    """
    MidLocation = None

    pass

class SurfaceOperationTransformBy(SurfaceOperation):
    """
    This class encapsulates the operation of transforming a surface, such as rotate, scale and move transformations.
    """
    TransformMatrix = None
    TransformType = None

    pass

class SurfacePointOutputOptions(object):
    """
    The class encapsulates the information required for the interpolation and extrapolation of point output.
    """
    Edges = None
    GridOrientation = None
    GridSpacingX = None
    GridSpacingY = None
    OutputLocations = None
    OutputRegions = None
    RandomPointsNumber = None
    pass

class SurfaceSimplifyOptions(object):
    """
    This class represents the options for simplifing a TinSurface object.
    """
    MaximumChangeInElevation = None
    PercentageToRemove = None
    RegionOption = None
    SimplifyMethod = None
    UseMaximumChangeInElevation = None
    UsePercentageToRemove = None
    UserSpecifiedPolygonRegion = None
    def Equals(self):
        """
        Equals(right: System.Object) -> bool
            right: System.Object
        """
        pass
    
    
    def SetSurfaceBorderAsRegion(self):
        """
        SetSurfaceBorderAsRegion()
            Sets the surface border as region to apply the simplification.
        """
        pass
    
    
    def SetUserSpecifiedPolygonRegionByEntityId(self):
        """
        SetUserSpecifiedPolygonRegionByEntityId(entityId: ObjectId, midOrdinate: System.Double)
            Sets the region defined by an existing entity in the drawing.
            Remarks: A user specified region only takes effect when RegionOption is SurfaceSimplifyRegionType.UserSpecified.
            entityId: ObjectId - ObjectId of the entity acting as a region.
            midOrdinate: System.Double - 
            The default mid-ordinate length used to get region from the entity.
            If the selected object contains arc segments, each segment is tessellated into chord segments. The length of each chord segment is derived from the specified mid-ordinate distance.
        """
        pass
    
    pass

class SurfaceSimplifyRegionType():
    """
    Enum class which represents the region type to simplify the TinSurface object.
    """
    pass

class SurfaceSlopeLabel(Entity):
    """
    This class represents a surface slope label.
    """
    Location = None
    Location2 = None
    SlopeLabelType = None
    def Create(self):
        """
        Create(surfaceId: ObjectId, location: Point2d) -> ObjectId
            Creates a new instance of an OnePoint SurfaceSlopeLabel.
            surfaceId: ObjectId - The object id of surface to which the label is attahed.
            location: Point2d - The place in which the label is located.
        Create(surfaceId: ObjectId, location: Point2d, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of an OnePoint SurfaceSlopeLabel.
            surfaceId: ObjectId - The object id of surface to which the label is attahed.
            location: Point2d - The place in which the label is located.
            labelStyleId: ObjectId - The object id of label style for the label.
        Create(surfaceId: ObjectId, point1: Point2d, point2: Point2d) -> ObjectId
            Creates a new instance of a TwoPoint SurfaceSlopeLabel.
            surfaceId: ObjectId - The object id of surface to which the label is attahed.
            point1: Point2d - The first point of label.
            point2: Point2d - The second point of label.
        Create(surfaceId: ObjectId, point1: Point2d, point2: Point2d, labelStyleId: ObjectId) -> ObjectId
            Creates a new instance of a TwoPoint SurfaceSlopeLabel.
            surfaceId: ObjectId - The object id of surface to which the label is attahed.
            point1: Point2d - The first point of label.
            point2: Point2d - The second point of label.
            labelStyleId: ObjectId - The object id of label style for the label.
        """
        pass
    
    
    def GetAvailableSurfaceSlopeLabelIds(self):
        """
        GetAvailableSurfaceSlopeLabelIds(surfaceId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of slope labels on the specified surface.
            surfaceId: ObjectId - ObjectId of the surface where the labels are located.
        """
        pass
    
    
    def GetAvailableSurfaceSlopeLabels(self):
        """
        GetAvailableSurfaceSlopeLabels(surfaceId: ObjectId) -> ObjectIdCollection
            Returns the ObjectId collection of slope labels on the specified surface.
            surfaceId: ObjectId - ObjectId of the surface where the labels are located.
        """
        pass
    
    pass

class SurfaceSlopeLabelType():
    """
    This enum class represents the types of surface slope label.
    """
    pass

class SurfaceTransformOperationType():
    """
    Specifies the type of transform operation on a surface.
    """
    pass

class SurfaceVolumeInfo():
    """
    This class defines the volume information of a surface or part of a surface.
    """
    Cut = None
    Fill = None
    Net = None
    pass

class SurveyFigure(Entity):
    """
    Survey figure class. Figures are groups of connected lines and arcs where the figure vertexes can reference survey points.
    """


    pass

class SurveyNetworkEntity(Entity):
    """
    The drawing database version of a survey network object.
    """


    pass

class SweptShapeType():
    """
    Specifies the swept shape of a pipe.
    """
    pass

class Table(Entity):
    """
    Base class for table objects, such as LegendTable and AlignmentTable.
    """


    pass

class TerrainSurfaceProperties(object):
    """
    This class encapsulates Terrain surface statistics information.
    """

    pass

class TinSurface(Entity):
    """
    This class encapsulates a Triangle Irregular Network (TIN) surface.
    """
    BreaklinesDefinition = None
    ContoursDefinition = None
    DEMFilesDefinition = None
    DrawingObjectsDefinition = None
    PointFilesDefinition = None
    PointGroupsDefinition = None
    SurveyQueriesAddFigureDefinition = None
    SurveyQueriesAddPointDefinition = None
    Triangles = None
    Vertices = None
    def AddLine(self):
        """
        AddLine(vertex1: Autodesk.Civil.DatabaseServices.TinSurfaceVertex, vertex2: Autodesk.Civil.DatabaseServices.TinSurfaceVertex) -> SurfaceOperationAddLine
            Adds a line to the TinSurface object.
            vertex1: Autodesk.Civil.DatabaseServices.TinSurfaceVertex - The end point of the line.
            vertex2: Autodesk.Civil.DatabaseServices.TinSurfaceVertex - The other end point of the line.
        """
        pass
    
    
    def AddVertex(self):
        """
        AddVertex(location: Point2d) -> SurfaceOperationAddTinVertex
            Adds a vertex to the TinSurface object.
            Remarks: This overload method takes a point2d as parameter.
            If the location is on the surface, the elevation of the vertex to be added will be automatically calculated according to the current triangle.
            If the location is not on the surface, the elevation will be set as 0.0 by default.
            location: Point2d - The location where the vertex will be added.
        AddVertex(location: Point3d) -> SurfaceOperationAddTinVertex
            Adds a vertex to the TinSurface object.
            location: Point3d - The location where the vertex will be added.
        """
        pass
    
    
    def AddVertices(self):
        """
        AddVertices(locations: Point2dCollection) -> SurfaceOperationAddTinMultipleVertices
            Adds multiple vertices to the TinSurface object.
            Remarks: This overload method takes a point2d collection as a parameter.
            If the location is on the surface, the elevation of vertex to be added will be automatically calculated according to current the triangle.
            If the location is not on the surface, the elevation will be set as 0.0 by default.
            locations: Point2dCollection - Locations where vertices will be added.
        AddVertices(locations: Point3dCollection) -> SurfaceOperationAddTinMultipleVertices
            Adds multiple vertices to the TinSurface object.
            locations: Point3dCollection - Locations where vertices will be added.
        """
        pass
    
    
    def Create(self):
        """
        Create(database: Database, surfaceName: System.String) -> ObjectId
            Creates a new instance of a TinSurface and adds it to the specified database.
            Remarks: This method uses the default style for the surface.
            database: Database - The database where the new surface is created.
            surfaceName: System.String - The name of the surface.
        Create(surfaceName: System.String, styleId: ObjectId) -> ObjectId
            Creates a new instance of a TinSurface and adds it to the database that contains styleId.
            surfaceName: System.String - The name of the surface.
            styleId: ObjectId - The ObjectId of the style for the surface.
        """
        pass
    
    
    def CreateByCropping(self):
        """
        CreateByCropping(destDatabase: Database, surfaceName: System.String, srcSurfaceId: ObjectId, points: Point2dCollection) -> ObjectId
            Creates a new TinSurface by cropping from an existing source TinSurface, and then inserts the new surface into another drawing.
            You must specify the cropped area with at least 3 points.
            Remarks: You need to lock the destDatabase and then set it as the current document before you call this method.
            destDatabase: Database - The database to insert the new TinSurface into.
            surfaceName: System.String - The new surface name.
            srcSurfaceId: ObjectId - The ObjectId of the source surface.
            points: Point2dCollection - A collection of points that specifies the cropped area.
        CreateByCropping(destDatabase: Database, surfaceName: System.String, srcSurfaceId: ObjectId, points: Point3dCollection) -> ObjectId
            Creates a new TinSurface by cropping from an existing source TinSurface, and then inserts the new surface into another drawing.
            You must specify at least 3 points as the cropped area.
            Remarks: You need to lock the destDatabase and then set it as the current document before you call this method.
            destDatabase: Database - The database to insert the new TinSurface into.
            surfaceName: System.String - The new surface name.
            srcSurfaceId: ObjectId - The ObjectId of the source surface.
            points: Point3dCollection - The points that specify the cropped area.
        CreateByCropping(destDatabase: Database, surfaceName: System.String, srcSurfaceId: ObjectId, objects: ObjectIdCollection, location: Point2d) -> ObjectId
            Creates a new TinSurface by cropping from a source TinSurface, and then inserts the new surface into another drawing.
            You must specify a cropped area with at least one AutoCAD drawing object.
            Remarks: The supported object types are: Polyline, Polyline2d, Polyline3d, ParcelSegment, FeatureLine, Circle, Arc, Ellipse, and Line.
            destDatabase: Database - The database to insert the new TinSurface into.
            surfaceName: System.String - The new surface name.
            srcSurfaceId: ObjectId - The ObjectId of the source surface.
            objects: ObjectIdCollection - The objects that specify the cropped area.
            location: Point2d - A location to identify the direction of the cropped area.
        """
        pass
    
    
    def CreateFromCorridorSurface(self):
        """
        CreateFromCorridorSurface(surfaceName: System.String, corridorSurface: Autodesk.Civil.DatabaseServices.CorridorSurface) -> CorridorSurface
            Creates a new TinSurface from corridor surface.
            surfaceName: System.String - The new surface name.
            corridorSurface: Autodesk.Civil.DatabaseServices.CorridorSurface - The corridor surface created from.
        """
        pass
    
    
    def CreateFromIMX(self):
        """
        CreateFromIMX(database: Database, styleId: ObjectId, imxFileName: System.String, surfaceName: System.String, gitHash: System.String, query: System.String, doCoordSysConversion: System.Boolean) -> ObjectId
            Creates a new instance of a TinSurface from a specified IMX file to the specified database.
            database: Database - The database where the new surface should be created.
            styleId: ObjectId - The object id of the surface style.  Passing AcDbObjectId::kNull will create with the default style.
            imxFileName: System.String - The full file path of the IMX file.
            surfaceName: System.String - The name of the surface within the IMX file.
            gitHash: System.String - The git hash value.
            query: System.String - The query value.
            doCoordSysConversion: System.Boolean - true to perform coordinate system conversion if possible
        """
        pass
    
    
    def CreateFromTin(self):
        """
        CreateFromTin(database: Database, tinFileName: System.String) -> ObjectId
            Creates a new instance of a TinSurface from a specified TIN file, and adds it to the specified database.
            database: Database - The database where the new surface is created.
            tinFileName: System.String - The full file path of the TIN file.
        """
        pass
    
    
    def DeleteLine(self):
        """
        DeleteLine(tinTriangleEdge: Autodesk.Civil.DatabaseServices.TinSurfaceEdge) -> SurfaceOperationDeleteLine
            Deletes a line from the TinSurface object.
            tinTriangleEdge: Autodesk.Civil.DatabaseServices.TinSurfaceEdge - The TIN triangle edge to be deleted.
        """
        pass
    
    
    def DeleteLines(self):
        """
        DeleteLines(tinTriangleEdges: System.Collections.Generic.IEnumerable) -> SurfaceOperationDeleteMultipleLines
            Deletes multiple lines from the TinSurface object.
            tinTriangleEdges: System.Collections.Generic.IEnumerable - The TIN triangle edges to be deleted.
        """
        pass
    
    
    def DeleteVertex(self):
        """
        DeleteVertex(vertex: Autodesk.Civil.DatabaseServices.TinSurfaceVertex) -> SurfaceOperationDeleteTinVertex
            Deletes a vertex from the TinSurface object.
            vertex: Autodesk.Civil.DatabaseServices.TinSurfaceVertex - The vertex to be deleted.
        """
        pass
    
    
    def DeleteVertices(self):
        """
        DeleteVertices(vertices: System.Collections.Generic.IEnumerable) -> SurfaceOperationDeleteMultipleTinVertices
            Deletes multiple vertices from the TinSurface object.
            vertices: System.Collections.Generic.IEnumerable - The vertices to be deleted.
        """
        pass
    
    
    def ExtractBorder(self):
        """
        ExtractBorder(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface border information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the border information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def ExtractContours(self):
        """
        ExtractContours(interval: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation interval.
            interval: System.Double - 
            The specified elevation interval.
        ExtractContours(interval: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation interval with smoothing.
            interval: System.Double - 
            The specified elevation interval.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only.
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        ExtractContours(lowElev: System.Double, highElev: System.Double, interval: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation range and interval.
            lowElev: System.Double - 
            The specified lower elevation.
            highElev: System.Double - 
            The specified high elevation.
            interval: System.Double - 
            The specified elevation interval.
        ExtractContours(lowElev: System.Double, highElev: System.Double, interval: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation range and interval with smoothing.
            lowElev: System.Double - 
            The specified lower elevation.
            highElev: System.Double - 
            The specified high elevation.
            interval: System.Double - 
            The specified elevation interval.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractContoursAt(self):
        """
        ExtractContoursAt(elevation: System.Double) -> ObjectIdCollection
            Extracts the surface contour information from the terrain surface at a specified elevation.
            elevation: System.Double - 
            The specified elevation.
        ExtractContoursAt(elevation: System.Double, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> ContourSmoothingType
            Extracts the surface contour information from the terrain surface at a specified elevation with smoothing.
            elevation: System.Double - 
            The specified elevation.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, the smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractGridded(self):
        """
        ExtractGridded(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface grid information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the grid information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def ExtractMajorContours(self):
        """
        ExtractMajorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface major contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        ExtractMajorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> SurfaceExtractionSettingsType
            Extracts the surface major contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractMinorContours(self):
        """
        ExtractMinorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface minor contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        ExtractMinorContours(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType, smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType, smoothFactor: System.Int32) -> SurfaceExtractionSettingsType
            Extracts the surface minor contour information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the contour information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
            smoothType: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType - 
            Currently, smoothType can be AddVertices only. 
            smoothFactor: System.Int32 - 
            smoothFactor should be in the range [0, 10]. A value of 10 generates the smoothest contours.
        """
        pass
    
    
    def ExtractWatershed(self):
        """
        ExtractWatershed(settingsType: Autodesk.Civil.SurfaceExtractionSettingsType) -> SurfaceExtractionSettingsType
            Extracts the surface watershed information from the terrain surface.
            settingsType: Autodesk.Civil.SurfaceExtractionSettingsType - 
            Specify SurfaceExtractionSettingsType.Plan to extract the watershed information using the plan visual style settings, 
            or  SurfaceExtractionSettingsType.Model to use the model settings.
        """
        pass
    
    
    def FindEdgeAtXY(self):
        """
        FindEdgeAtXY(x: System.Double, y: System.Double) -> TinSurfaceEdge
            Finds the closest TinSurfaceEdge near location (x, y).
            Remarks: When the method can't find an edge at location (x, y), it means (x, y) is not on the surface. You can use the IdentifyFeatureTypeAtXY property to determine whether the location (x, y) is on surface.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def FindTriangleAtXY(self):
        """
        FindTriangleAtXY(x: System.Double, y: System.Double) -> TinSurfaceTriangle
            Finds the TinSurfaceTriangle which contains location (x, y).
            Remarks: When the method can't find a triangle at location (x, y), it means (x, y) is not on the surface. You can use the IdentifyFeatureTypeAtXY property to determine whether the location (x, y) is on surface.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def FindVertexAtXY(self):
        """
        FindVertexAtXY(x: System.Double, y: System.Double) -> TinSurfaceVertex
            Finds the closest TinSurfaceVertex near location (x, y).
            Remarks: When the method can't find a vertex at location (x, y), it means that (x, y) is not on the surface. You can use the IdentifyFeatureTypeAtXY property to determine whether the location (x, y) is on the surface.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def GetTerrainProperties(self):
        """
        GetTerrainProperties() -> TerrainSurfaceProperties
            Gets the Terrain properties of the surface.
        """
        pass
    
    
    def GetTinProperties(self):
        """
        GetTinProperties() -> TinSurfaceProperties
            Gets the TIN properties of the surface.
        """
        pass
    
    
    def GetTriangles(self):
        """
        GetTriangles(includeInvisible: System.Boolean) -> TinSurfaceTriangleCollection
            Gets all the vertices in the TinSurface.
            includeInvisible: System.Boolean - Indicates whether the method should return invisible triangles.
        """
        pass
    
    
    def GetVerticesInsideBorder(self):
        """
        GetVerticesInsideBorder(border: Point3dCollection) -> TinSurfaceVertex
            Gets an array that contains all the TinSurfaceVertex objects inside the border specified by a Point3d collection.
            Remarks: The points in the collection should be able to build a border.
            This method is used to prepare the KrigingMethodOptions object used to smooth a surface using the Kriging method.
            border: Point3dCollection - A collection that contains the Point3d objects used to specify the border.
        """
        pass
    
    
    def GetVerticesInsideBorderRandom(self):
        """
        GetVerticesInsideBorderRandom(border: Point3dCollection, randomNumber: System.Int32) -> TinSurfaceVertex
            Gets an array that contains a random selection of TinSurfaceVertex objects inside the border specified by a Point3d collection.
            Remarks: The points in the collection should be able to build a border.
            This method is used to prepare the KrigingMethodOptions object used to smooth a surface using the Kriging method.
            border: Point3dCollection - A collection that contains the Point3d objects used to specify the border.
            randomNumber: System.Int32 - The number of TinSurfaceVertices objects to get.
        """
        pass
    
    
    def GetVerticesInsidePolylines(self):
        """
        GetVerticesInsidePolylines(polylineIds: ObjectIdCollection) -> TinSurfaceVertex
            Gets an array that contains all the TinSurfaceVertex objects inside the polyline.
            Remarks: This method is used to prepare the KrigingMethodOptions object used to smooth a surface using the Kriging method.
            polylineIds: ObjectIdCollection - A collection that contains polyline ObjectIds.
        """
        pass
    
    
    def GetVerticesInsidePolylinesRandom(self):
        """
        GetVerticesInsidePolylinesRandom(polylineIds: ObjectIdCollection, randomNumber: System.Int32) -> TinSurfaceVertex
            Gets an array that contains a random sample of TinSurfaceVertex objects inside the polyline.
            Remarks: This method is used to prepare the KrigingMethodOptions object used to smooth a surface using the Kriging method.
            polylineIds: ObjectIdCollection - A collection that contains polyline ObjectIds.
            randomNumber: System.Int32 - The number of TinSurfaceVertices objects to get.
        """
        pass
    
    
    def IdentifyFeatureTypeAtXY(self):
        """
        IdentifyFeatureTypeAtXY(x: System.Double, y: System.Double) -> Type
            Identifies the specific surface feature (triangle, edge, vertex) at a specified point.
            x: System.Double
            y: System.Double
        """
        pass
    
    
    def MinimizeFlatAreas(self):
        """
        MinimizeFlatAreas(minimizeOptions: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationMinimizeFlatAreas
            Minimizes flat areas in a surface.
            minimizeOptions: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions - Options for minimizing.
        """
        pass
    
    
    def MoveVertex(self):
        """
        MoveVertex(vertex: Autodesk.Civil.DatabaseServices.TinSurfaceVertex, newLocation: Point2d) -> SurfaceOperationMoveTinVertex
            Moves a vertex in the TinSurface object on the XY plane.
            vertex: Autodesk.Civil.DatabaseServices.TinSurfaceVertex - The vertex to be moved.
            newLocation: Point2d - The new location where the vertex will be moved to.
        """
        pass
    
    
    def PasteSurface(self):
        """
        PasteSurface(surfaceId: ObjectId) -> SurfaceOperationPasteSurface
            Pastes a surface into the current surface.
            Remarks: This method can paste all kinds of surface, including TinSurface, GridSurface, TinVolumeSurface, GridVolumeSurface.
            surfaceId: ObjectId
        """
        pass
    
    
    def RaiseSurface(self):
        """
        RaiseSurface(deltaElevation: System.Double) -> SurfaceOperationRaise
            Raises or lowers the surface.
            deltaElevation: System.Double - 
            The elevation delta. A positive value raises the elevation while a negative value lowers the elevation.
        """
        pass
    
    
    def RaiseVertices(self):
        """
        RaiseVertices(vertices: System.Collections.Generic.IEnumerable, deltaElevation: System.Double) -> SurfaceOperationModifyMultipleTinVerticesElevation
            Raises or lowers multiple vertices in the TinSurface object.
            Remarks: Vertices are lowered if deltaElevation is negative, otherwise they are raised.
            vertices: System.Collections.Generic.IEnumerable - The vertices to be raised or lowered.
            deltaElevation: System.Double - The delta elevation for the vertices.
        """
        pass
    
    
    def SampleElevations(self):
        """
        SampleElevations(curveId: ObjectId) -> Point3dCollection
            Gets the sampled points along a curve entity.
            curveId: ObjectId - An ObjectId of Autodesk.AutoCAD.DatabaseServices.Curve. The curve can be a line, arc and so on.
        SampleElevations(pt1: Point3d, pt2: Point3d) -> Point3dCollection
            pt1: Point3d
            pt2: Point3d
        """
        pass
    
    
    def SetVertexElevation(self):
        """
        SetVertexElevation(vertex: Autodesk.Civil.DatabaseServices.TinSurfaceVertex, newElevation: System.Double) -> SurfaceOperationModifyTinVertexElevation
            Sets the elevation of a vertex in the TinSurface object.
            vertex: Autodesk.Civil.DatabaseServices.TinSurfaceVertex - The vertex to be set with new elevation.
            newElevation: System.Double - The new elevation for the vertex.
        """
        pass
    
    
    def SetVerticesElevation(self):
        """
        SetVerticesElevation(vertices: System.Collections.Generic.IEnumerable, newElevation: System.Double) -> SurfaceOperationModifyMultipleTinVerticesElevation
            Sets the elevation of multiple vertices in the TinSurface object.
            vertices: System.Collections.Generic.IEnumerable - The vertices to be set with new a elevation.
            newElevation: System.Double - The new elevation for the vertices.
        """
        pass
    
    
    def SimplifySurface(self):
        """
        SimplifySurface(simplifyOptions: Autodesk.Civil.DatabaseServices.SurfaceSimplifyOptions) -> SurfaceOperationSimplify
            Reduces the number of points on TIN surface, making the surface file smaller and easier to process.
            simplifyOptions: Autodesk.Civil.DatabaseServices.SurfaceSimplifyOptions - Options of simplification.
        """
        pass
    
    
    def SmoothSurfaceByKriging(self):
        """
        SmoothSurfaceByKriging(krigingOptions: Autodesk.Civil.DatabaseServices.KrigingMethodOptions, pointOutputOptions: Autodesk.Civil.DatabaseServices.SurfacePointOutputOptions) -> SurfaceOperationSmooth
            Smooths the surface using the Kriging method.
            Remarks: Surface smoothing can take a considerable amount of time proportional to the number of output points. For the Kriging method, it is recommended that you use a relatively small sample point set (no more than 100 to 200 points).
            krigingOptions: Autodesk.Civil.DatabaseServices.KrigingMethodOptions - The information about the sample data and semivariogram model to smooth a surface using the Kriging method.
            pointOutputOptions: Autodesk.Civil.DatabaseServices.SurfacePointOutputOptions - The information for interpolation and extrapolation of the point output.
        """
        pass
    
    
    def SmoothSurfaceByNNI(self):
        """
        SmoothSurfaceByNNI(pointOutputOptions: Autodesk.Civil.DatabaseServices.SurfacePointOutputOptions) -> SurfaceOperationSmooth
            Smooths the surface using the Natural Neighbor Interpolation (NNI) method.
            pointOutputOptions: Autodesk.Civil.DatabaseServices.SurfacePointOutputOptions - The information for the interpolation and extrapolation of the point output.
        """
        pass
    
    
    def SwapEdge(self):
        """
        SwapEdge(tinTriangleEdge: Autodesk.Civil.DatabaseServices.TinSurfaceEdge) -> SurfaceOperationSwapEdge
            Swaps edges in order to change the direction of two triangle faces in a surface model.
            tinTriangleEdge: Autodesk.Civil.DatabaseServices.TinSurfaceEdge - The TIN triangle edge to be swapped.
        """
        pass
    
    pass

class TinSurfaceEdge(TinSurfaceObject):
    """
    This class encapsulates a triangle edge in a TinSurface.
    """
    IsValid = None
    Triangle1 = None
    Triangle2 = None
    Vertex1 = None
    Vertex2 = None
    def Equals(self):
        """
        Equals(rhs: System.Object) -> bool
            rhs: System.Object
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode() -> int
        """
        pass
    
    pass

class TinSurfaceEdgeCollection(object):
    """
    This class encapsulates a collection of TinSurfaceEdge objects.
    """
    Count = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the TinSurfaceEdgeCollection
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> TinSurfaceEdge
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

class TinSurfaceEdgeEnumerator(object):
    """
    
    """
    Current = None
    CurrentObject = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the TinSurfaceEdgeEnumerator
        """
        pass
    
    
    def MoveNext(self):
        """
        MoveNext() -> bool
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
        """
        pass
    
    pass

class TinSurfaceObject(TinSurfaceEdge):
    """
    The base class for TinSurface data objects, such as TinSurfaceVertex and TinSurfaceTriangle.
    """
    IsValid = None
    Surface = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the TinSurfaceObject
        """
        pass
    
    pass

class TinSurfaceProperties(object):
    """
    This class encapsulates TIN surface statistics information.
    """

    pass

class TinSurfaceTriangle(TinSurfaceObject):
    """
    This class encapsulates a triangle in a TinSurface.
    """
    Edge1 = None
    Edge2 = None
    Edge3 = None
    Vertex1 = None
    Vertex2 = None
    Vertex3 = None
    def Equals(self):
        """
        Equals(rhs: System.Object) -> bool
            rhs: System.Object
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode() -> int
        """
        pass
    
    pass

class TinSurfaceTriangleCollection(object):
    """
    This class encapsulates a collection of TinSurfaceTriangle objects.
    """
    Count = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the TinSurfaceTriangleCollection
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> TinSurfaceTriangle
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

class TinSurfaceTriangleEnumerator(object):
    """
    
    """
    Current = None
    CurrentObject = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the TinSurfaceTriangleEnumerator
        """
        pass
    
    
    def MoveNext(self):
        """
        MoveNext() -> bool
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
        """
        pass
    
    pass

class TinSurfaceVertex(TinSurfaceObject):
    """
    This class encapsulates a triangle vertex in a TinSurface.
    """
    Edges = None
    Location = None
    Triangles = None
    Vertices = None
    def Equals(self):
        """
        Equals(rhs: System.Object) -> bool
            rhs: System.Object
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode() -> int
        """
        pass
    
    pass

class TinSurfaceVertexCollection(object):
    """
    This class encapsulates a collection of TinSurfaceVertex objects.
    """
    Count = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the TinSurfaceVertexCollection
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> TinSurfaceVertex
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

class TinSurfaceVertexEnumerator(object):
    """
    
    """
    Current = None
    CurrentObject = None
    def Dispose(self):
        """
        Dispose()
            Releases all resources used by the TinSurfaceVertexEnumerator
        """
        pass
    
    
    def MoveNext(self):
        """
        MoveNext() -> bool
        """
        pass
    
    
    def Reset(self):
        """
        Reset()
        """
        pass
    
    pass

class TinVolumeSurface(Entity):
    """
    The TinVolumeSurface class.
    This class encapsulates a TIN volume surface.
    """
    CutFactor = None
    FillFactor = None
    def Create(self):
        """
        Create(surfaceName: System.String, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId) -> ObjectId
            Creates a new instance of a TinVolumeSurface and adds it to the database where the surface specified by baseSurfaceId is located.
            Remarks: This method uses the default style for the surface so you don't need to provide a style ObjectId.
            surfaceName: System.String - The name of the new TinVolumeSurface.
            baseSurfaceId: ObjectId - The ObjectId of the base surface for the TinVolumeSurface.
            comparisonSurfaceId: ObjectId - The ObjectId of the comparison (top) surface for the TinVolumeSurface.
        Create(surfaceName: System.String, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, styleId: ObjectId) -> ObjectId
            Creates a new instance of a TinVolumeSurface and adds it to the database where the surface specified by baseSurfaceId is located.
            Remarks: This method takes a SurfaceStyle, specified by styleId, to apply to the newly created surface.
            surfaceName: System.String - The name of the new TinVolumeSurface.
            baseSurfaceId: ObjectId - The ObjectId of the base surface for the TinVolumeSurface.
            comparisonSurfaceId: ObjectId - The ObjectId of the comparison (top) surface for the TinVolumeSurface.
            styleId: ObjectId - The ObjectId of the SurfaceStyle for the TinVolumeSurface.
        """
        pass
    
    
    def GetTinProperties(self):
        """
        GetTinProperties() -> TinSurfaceProperties
            Gets the TIN properties of the surface.
        """
        pass
    
    
    def GetVolumeProperties(self):
        """
        GetVolumeProperties() -> VolumeSurfaceProperties
            Gets the Volume properties of the surface.
        """
        pass
    
    pass

class TransitionDescriptionBase(CurveCurveReverseCurveTransitionDescription):
    """
    Abstract base class for all transition description objects.
    """
    EndStation = None
    Length = None
    StartStation = None
    pass

class UDP(UDPBoolean):
    """
    The class represents the base class for all user-defined property classes.
    """
    ClassificationName = None
    DefaultValue = None
    Description = None
    Guid = None
    IsInUsed = None
    Name = None
    UseDefaultValue = None
    pass

class UDPBoolean(UDP):
    """
    This class represents a user-defined property with a Boolean data type.
    """
    DefaultValue = None
    def InternalGetAttributeTypeInfo(self):
        """
        InternalGetAttributeTypeInfo() -> AeccAttributeTypeInfoBool*
        """
        pass
    
    pass

class UDPClassification(object):
    """
    This class encapsulates a UDPClassification used to create and organize user-defined custom properties.
    """
    Name = None
    UDPs = None
    def ContainsUDP(self):
        """
        ContainsUDP(udp: Autodesk.Civil.DatabaseServices.UDP) -> UDP
            Gets whether the collection contains the given UDP.
            udp: Autodesk.Civil.DatabaseServices.UDP - The instance of a UDP to search for in the collection.
        """
        pass
    
    
    def CreateUDP(self):
        """
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoBool) -> UDPBoolean
            Creates a user-defined property with a boolean data type.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoBool - An AttributeTypeInfoBool that defines the parameters for the new user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoDouble) -> UDPDouble
            Creates a user-defined property with a double data type.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoDouble - An AttributeTypeInfoDouble that defines the parameters for the new user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoEnum) -> UDPEnumeration
            Creates a user-defined property with an enumeration data type.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoEnum - An AttributeTypeInfoEnum that defines the parameters for the new user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoInt) -> UDPInteger
            Creates a user-defined property with an integer data type.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoInt - An AttributeTypeInfoInteger instance that defines the parameters for the new user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoString) -> UDPString
            Creates a user-defined property with a string data type.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoString - An AttributeTypeInfoString instance that defines the parameters for the new user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoBool, guid: System.Guid) -> UDPBoolean
            Creates a user-defined property with a boolean data type.
            Remarks: When the guid parameter is Guid.Empty, a new GUID is automatically assigned to the user-defined property. 
            Multiple UDPs can share the same GUID, however, the combination of the UDP name + GUID must be unique.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoBool - An AttributeTypeInfoBool instance that defines the parameters for the new user-defined property.
            guid: System.Guid - the Guid for the user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoDouble, guid: System.Guid) -> UDPDouble
            Creates a user-defined property with a double data type.
            Remarks: When the guid parameter is Guid.Empty, a new GUID is automatically assigned to the user-defined property. 
            Multiple UDPs can share the same GUID, however, the combination of the UDP name + GUID must be unique.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoDouble - An AttributeTypeInfoDouble that defines the parameters for the new user-defined property.
            guid: System.Guid - the Guid for the user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoEnum, guid: System.Guid) -> UDPEnumeration
            Creates a user-defined property with an enumeration data type.
            Remarks: When the guid parameter is Guid.Empty, a new GUID is automatically assigned to the user-defined property. 
            Multiple UDPs can share the same GUID, however, the combination of the UDP name + GUID must be unique.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoEnum - An AttributeTypeInfoEnum that defines the parameters for the new user-defined property.
            guid: System.Guid - the Guid for the user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoInt, guid: System.Guid) -> UDPInteger
            Creates a user-defined property with an integer data type.
            Remarks: When the guid parameter is Guid.Empty, a new GUID is automatically assigned to the user-defined property.
            Multiple UDPs can share the same GUID, however, the combination of the UDP name + GUID must be unique.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoInt - An AttributeTypeInfoInteger instance that defines the parameters for the new user-defined property.
            guid: System.Guid - the Guid for the user-defined property.
        CreateUDP(udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoString, guid: System.Guid) -> UDPString
            Creates a user-defined property with a string data type.
            Remarks: When the guid parameter is Guid.Empty, a new GUID is automatically assigned to the user-defined property. 
            Multiple UDPs can share the same GUID, however, the combination of the UDP name + GUID must be unique.
            udpTypeInfo: Autodesk.Civil.DatabaseServices.AttributeTypeInfoString - An AttributeTypeInfoString instance that defines the parameters for the new user-defined property.
            guid: System.Guid - A GUID for the user-defined property.
        """
        pass
    
    
    def RemoveUDP(self):
        """
        RemoveUDP(udp: Autodesk.Civil.DatabaseServices.UDP) -> UDP
            Removes the specified UDP with the current classification.
            udp: Autodesk.Civil.DatabaseServices.UDP - The instance of the UDP to remove.
        """
        pass
    
    pass

class UDPClassificationApplyType():
    """
    An enumeration that specifies how User-Defined Property classifications 
    are applied to a point group or parcel properties.
    """
    pass

class UDPClassificationCollection(object):
    """
    This class encapsulates the collection of all UDPClassification objects in the current drawing.
    """
    Count = None
    Item = None
    def Add(self):
        """
        Add(name: System.String) -> UDPClassification
            Creates a new UDPClassification with the given name and adds it to the collection.
            name: System.String - The name of the UDPClassification to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(name: System.String) -> bool
            Gets whether the collection contains the given UDPClassification by its name.
            name: System.String
        Contains(udpClassification: Autodesk.Civil.DatabaseServices.UDPClassification) -> UDPClassification
            Gets whether the collection contains the given UDPClassification.
            udpClassification: Autodesk.Civil.DatabaseServices.UDPClassification
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> UDPClassification
            Implement the method declared in the IEnumerable<T> interface. This method returns an enumerator that can be use to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declaredd in the IEnumerable interface. This method returns an enumerator that can be used to enumerate this collection.
        """
        pass
    
    
    def GetPointUDPClassifications(self):
        """
        GetPointUDPClassifications(pDatabase: Database) -> UDPClassificationCollection
            pDatabase: Database
        """
        pass
    
    
    def Remove(self):
        """
        Remove(name: System.String) -> bool
            Removes a UDPClassification from the collection by name.
            name: System.String - The name of the UDPClassification object to remove.
        Remove(udpClassification: Autodesk.Civil.DatabaseServices.UDPClassification) -> UDPClassification
            Removes the specified UDPClassification from the collection.
            udpClassification: Autodesk.Civil.DatabaseServices.UDPClassification - The instance of the UDPClassification object to remove from the collection.
        """
        pass
    
    pass

class UDPCollection(object):
    """
    This class encapsulates a collection of UDP objects.
    """
    Count = None
    Item = None
    def Contains(self):
        """
        Contains(udp: Autodesk.Civil.DatabaseServices.UDP) -> UDP
            Gets whether the collection contains a given UDP.
            udp: Autodesk.Civil.DatabaseServices.UDP - The instance of the UDP.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> UDP
            Implements the method declared in the IEnumerable<T> interface. This method returns an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def GetObjectEnumerator(self):
        """
        GetObjectEnumerator() -> IEnumerator
            Implements the method declared in the IEnumerable interface. This method returns an enumerator which can be used to enumerate this collection.
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray() -> UDP
            Copies the UDP objects in the collection to a new array.
        """
        pass
    
    pass

class UDPDouble(UDP):
    """
    This class represents a user-defined property with a double-precision data type.
    """
    DataType = None
    DefaultValue = None
    LowerBoundInclusive = None
    LowerBoundValue = None
    UpperBoundInclusive = None
    UpperBoundValue = None
    pass

class UDPEnumeration(UDP):
    """
    This class represents a user-defined property with an enumeration data type.
    """
    DefaultValue = None
    def GetEnumValues(self):
        """
        GetEnumValues() -> string[]
            Gets an array that contains all defined enumeration values for the UDP.
        """
        pass
    
    pass

class UDPInteger(UDP):
    """
    This class represents a user-defined property with an integer data type.
    """
    DefaultValue = None
    LowerBoundInclusive = None
    LowerBoundValue = None
    UpperBoundInclusive = None
    UpperBoundValue = None
    pass

class UDPString(UDP):
    """
    This class represents a user-defined property with a string data type.
    """
    DefaultValue = None
    pass

class VerticalCurveType():
    """
    Specifies the geometry type of a ProfileEntity curve, used for three types of parabolic entities.
    """
    pass

class VerticalGeometryBandLabelGroup(Entity):
    """
    
    """

    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all VerticalGeometryBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The ObjectId of the ProfileView where the label groups are located.
        """
        pass
    
    
    def GetAvailableLabelGroups(self):
        """
        GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: System.Boolean) -> ObjectIdCollection
            Returns an ObjectIdCollection of all VerticalGeometryBandLabelGroup objects on the specified ProfileView.
            profileViewId: ObjectId - The objectId of the profile view where the label groups are located.
            includeDerived: System.Boolean - Indicates whether to include the derived types of VerticalGeometryBandLabelGroup.
        """
        pass
    
    pass

class ViewFrame(Entity):
    """
    View frames are rectangular-shaped regions along an alignment that define an area that will be displayed in a sheet.
    """
    AlignmentId = None
    EndStation = None
    GroupId = None
    IsLabelVisible = None
    LabelAnchorPosition = None
    LabelStyleId = None
    Sheet = None
    SheetSet = None
    StartStation = None

    pass

class ViewFrameGroup(Entity):
    """
    Manages a single group of view frames that are displaying consecutive station ranges along the same alignment.
    """
    DefaultLeftMatchLineLabelAnchorPosition = None
    DefaultLeftMatchLineLabelStyleId = None
    DefaultRightMatchLineLabelAnchorPosition = None
    DefaultRightMatchLineLabelStyleId = None
    DefaultViewFrameLabelAnchorPosition = None
    DefaultViewFrameLabelStyleId = None
    def GetAvailableMatchLineLabelGroupIds(self):
        """
        GetAvailableMatchLineLabelGroupIds() -> ObjectIdCollection
            Returns an ObjectIdCollection of all available MatchLineLabelGroups.
        """
        pass
    
    
    def GetAvailableViewFrameLabelGroupIds(self):
        """
        GetAvailableViewFrameLabelGroupIds() -> ObjectIdCollection
            Returns an ObjectIdCollection of all available ViewFrameLabelGroups.
        """
        pass
    
    
    def GetMatchLineIds(self):
        """
        GetMatchLineIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all MatchLines.
        """
        pass
    
    
    def GetMatchLineLabelGroupIdBySide(self):
        """
        GetMatchLineLabelGroupIdBySide(side: Autodesk.Civil.EntitySideType) -> EntitySideType
            Returns the ObjectId of the MatchLineLabelGroup on the specified side.
            side: Autodesk.Civil.EntitySideType
        """
        pass
    
    
    def GetViewFrameIds(self):
        """
        GetViewFrameIds() -> ObjectIdCollection
            Gets an ObjectIdCollection of all ViewFrames.
        """
        pass
    
    pass

class ViewFrameLabelGroup(Entity):
    """
    This class represents a ViewFrame label group.
    """

    def Create(self):
        """
        Create(viewFrameGroupId: ObjectId) -> ObjectId
            Creates a new instance of a ViewFrameLabelGroup on the ViewFrameGroup with the default label style and anchor position of ViewFrameGroup.
            viewFrameGroupId: ObjectId - The ObjectId of the ViewFrameGroup where the label group is labeling.
        Create(viewFrameGroupId: ObjectId, labelStyleId: ObjectId, anchorPosition: Autodesk.Civil.ViewFrameLabelLocationType) -> ViewFrameLabelLocationType
            Creates a new instance of a ViewFrameLabelGroup on the ViewFrameGroup with the specified label style and anchor position.
            Remarks: The labelStyleId and anchorPosition will also be set as the DefaultViewFrameLabelAnchorPosition and DefaultViewFrameLabelStyleId.
            viewFrameGroupId: ObjectId - The ObjectId of the ViewFrameGroup where the label group is labeling.
            labelStyleId: ObjectId - The ObjectId of the ViewFrameLabel style.
            anchorPosition: Autodesk.Civil.ViewFrameLabelLocationType - The relative anchor position of ViewFrameLabelGroup.
        """
        pass
    
    
    def GetAvailableLabelGroupIds(self):
        """
        GetAvailableLabelGroupIds(viewFrameGroupId: ObjectId) -> ObjectIdCollection
            Returns an ObjectIdCollection of all the available ViewFrameLabelGroup objects in the specified ViewFrameGroup.
            viewFrameGroupId: ObjectId - The ObjectId of the ViewFrameGroup where the labelGroups are labeling.
        """
        pass
    
    pass

class VolumeSurfaceProperties(object):
    """
    This class encapsulates Volume surface statistics information.
    """

    pass

class VolumeTableType():
    """
    Defines table type.
    """
    pass

class WallBreaklineCreationData():
    """
    This structure specifies the information required to add wall breaklines to a surface.
    """
    pass

class WallBreaklineCreationDataEx(object):

class WidthOffsetTarget(object):
    """
    The WidthOffsetTarget class.
    """
    TargetId = None
    def GetDistanceToAlignment(self):
        """
        GetDistanceToAlignment(alignmentId: ObjectId, stationOnAlignment: System.Double, xOnTarget: System.Double, yOnTarget: System.Double) -> double
            alignmentId: ObjectId
            stationOnAlignment: System.Double
            xOnTarget: System.Double
            yOnTarget: System.Double
        GetDistanceToAlignment(alignmentId: ObjectId, stationOnAlignment: System.Double, side: Autodesk.Civil.DatabaseServices.AlignmentSide, xOnTarget: System.Double, yOnTarget: System.Double) -> AlignmentSide
            alignmentId: ObjectId
            stationOnAlignment: System.Double
            side: Autodesk.Civil.DatabaseServices.AlignmentSide
            xOnTarget: System.Double
            yOnTarget: System.Double
        """
        pass
    
    
    def GetNearestPipeOfNetworkToAlignment(self):
        """
        GetNearestPipeOfNetworkToAlignment(alignmentId: ObjectId, stationOnAlignment: System.Double, pipeId: ObjectId)
            alignmentId: ObjectId
            stationOnAlignment: System.Double
            pipeId: ObjectId
        GetNearestPipeOfNetworkToAlignment(alignmentId: ObjectId, stationOnAlignment: System.Double, side: Autodesk.Civil.DatabaseServices.AlignmentSide, pipeId: ObjectId) -> AlignmentSide
            alignmentId: ObjectId
            stationOnAlignment: System.Double
            side: Autodesk.Civil.DatabaseServices.AlignmentSide
            pipeId: ObjectId
        """
        pass
    
    pass