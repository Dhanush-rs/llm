from services.document_service import DocumentService


def main():
    DS = DocumentService()
    # create docs and try to read 
    print(DS.documents)
    DS.create_document("dhanush", "sample", "boogyman")
    DS.create_document(owner="Sanji", name="cook", content="the ultimate recipe...")
    DS.read_document("zoro","xyz")
    DS.read_document("zoro","sample")
    
    
    # grant permission and validate for valid and invalid docs
    DS.grant_read("zoro","asdc")
    DS.grant_read("zoro","sample")
    DS.read_document("zoro","sample")
    
    # grant write and update
    DS.update_document("zoro", "sample", "new content")
    DS.grant_write("zoro", "sample")
    DS.update_document("zoro", "sample", "new content")
    DS.read_document("zoro","sample")
    
    DS.delete_document("zoro","sample")
    DS.delete_document("dhanush", "sample")
    print(DS.documents)
if __name__ == "__main__":
    main()