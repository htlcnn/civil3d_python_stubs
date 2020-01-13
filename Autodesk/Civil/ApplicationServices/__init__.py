class CivilApplication(object):
    """
    The CivilApplication class.  This is the base class used to access CivilDocument.
    """
    ActiveDocument = None
    ActiveProduct = None
    SurveyProjects = None
    pass

class CivilDocument(object):
    """
    The CivilDocument class.  This is the root object for accessing settings, styles, and C3D entities, Alignment etc.
    """
    AssemblyCollection = None
    CogoPoints = None
    CorridorCollection = None
    CorridorState = None
    IsCorridorSectionViewActive = None
    IsDriveActive = None
    IsSectionEditorCorridorReferenceObject = None
    NetworkState = None
    PointGroups = None
    PointUDPClassifications = None
    PointUDPs = None
    Settings = None
    Styles = None
    SubassemblyCollection = None
    def GetAlignmentIds(self):
        """
        GetAlignmentIds() -> ObjectIdCollection
            Gets the objectId collection of all Alignment objects in the drawing.
            Remarks: The collection returned by this method includes both site and siteless alignments.
        """
        pass
    
    
    def GetAlignmentTableIds(self):
        """
        GetAlignmentTableIds() -> ObjectIdCollection
            Gets the objectId collection of all alignment tables.
        """
        pass
    
    
    def GetAllPointIds(self):
        """
        GetAllPointIds() -> ObjectIdCollection
            Gets the objectId collection of all points in the drawing.
        """
        pass
    
    
    def GetCivilDocument(self):
        """
        GetCivilDocument(database: Database) -> CivilDocument
            Gets the CivilDocument object from the AutoCAD Database object.
            database: Database - 
            The AutoCAD Database object.
        """
        pass
    
    
    def GetGeneralSegmentLabelIds(self):
        """
        GetGeneralSegmentLabelIds() -> ObjectIdCollection
            Gets the objectId collection of all GeneralSegmentLabel objects in the drawing.
        """
        pass
    
    
    def GetIntersectionIds(self):
        """
        GetIntersectionIds() -> ObjectIdCollection
            Gets the objectId collection of all intersection objects in the drawing.
        """
        pass
    
    
    def GetLegendTableIds(self):
        """
        GetLegendTableIds() -> ObjectIdCollection
            Gets the objectId collection of legend tables.
        """
        pass
    
    
    def GetNoteLabelIds(self):
        """
        GetNoteLabelIds() -> ObjectIdCollection
            Gets the objectId collection of all NoteLabel objects in the drawing.
        """
        pass
    
    
    def GetParcelSegmentTableIds(self):
        """
        GetParcelSegmentTableIds() -> ObjectIdCollection
            Gets the objectId collection of parcel segment tables.
        """
        pass
    
    
    def GetParcelTableIds(self):
        """
        GetParcelTableIds() -> ObjectIdCollection
            Gets the objectId collection of parcel tables.
        """
        pass
    
    
    def GetPipeNetworkIds(self):
        """
        GetPipeNetworkIds() -> ObjectIdCollection
            Gets the pipe network object id collection.
        """
        pass
    
    
    def GetPointTableIds(self):
        """
        GetPointTableIds() -> ObjectIdCollection
            Gets the objectId collection of point tables.
        """
        pass
    
    
    def GetSiteIds(self):
        """
        GetSiteIds() -> ObjectIdCollection
            Gets the objectId collection of all site objects in the drawing.
        """
        pass
    
    
    def GetSitelessAlignmentId(self):
        """
        GetSitelessAlignmentId(name: System.String) -> ObjectId
            Gets the objectId of a siteless Alignment object by name.
            Remarks: The siteless alignment name is unique, therefore it can be used as a key to get an alignment id.
            name: System.String - Name of the siteless alignment. 
        """
        pass
    
    
    def GetSitelessAlignmentIds(self):
        """
        GetSitelessAlignmentIds() -> ObjectIdCollection
            Gets the objectId collection of all siteless Alignment objects in the drawing.
        """
        pass
    
    
    def GetSurfaceIds(self):
        """
        GetSurfaceIds() -> ObjectIdCollection
            Gets the objectId collection of all surface objects in the drawing.
            Remarks: OBJECTID TYPE:Autodesk.Civil.DatabaseServices.Surface.
        """
        pass
    
    
    def GetViewFrameGroupIds(self):
        """
        GetViewFrameGroupIds() -> ObjectIdCollection
            Gets the objectId collection of all view frame groups in the drawing.
        """
        pass
    
    pass

class ProductType():
    """
    The available products types, returned by CivilApplication.ActiveProduct.
    """
    pass