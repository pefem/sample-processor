from abc import ABC, abstractmethod

# -------------------------------------------------

class CreateSample(ABC):
    """
    abstract class serving as interface for sample types

    """

    @abstractmethod
    def load_origin(self):
        """
        loads the origin from which the samples are created

        """
        pass
    
    # -------------------------------------------------

    @abstractmethod
    def origin_size(self):
        """
        gets the size of the origin

        """
        pass

    # -------------------------------------------------

    @abstractmethod
    def display_origin(self):
        """
        displays the origin
        
        """
        pass
    
    # -------------------------------------------------

    @abstractmethod
    def origin_format(self):
        """
        gets the origin format
        
        """
        pass

# -------------------------------------------------
# END OF FILE
# -------------------------------------------------