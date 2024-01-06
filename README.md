Models:
    contains Two table author and book having foreignkey relation .
    Implimented a Custom model manager to Implement validation to ensure that an author cannot have more than 5 books.
Views:
    Created Class based function using DRF. Serialisers provided for both table, used basic APIView and Generic view    
Error Handeling:
    We can provide a try except for that . Also if we need to impliment permission class also for security .    