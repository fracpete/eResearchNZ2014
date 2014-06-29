import adams.core.Utils as Utils
import adams.flow.core.Token as Token
import adams.flow.core.Unknown as Unknown
import adams.flow.transformer.AbstractScript as AbstractScript

import java.lang.Class as Class
import java.lang.Double
import java.lang.reflect.Array

from jarray import array
from jarray import zeros

class Spc2spreadsheet(AbstractScript):
    """
    Template of a Groovy transformer.

    @author FracPete (fracpete at waikato dot ac dot nz)
    @version $Revision: 7190 $
    """

    def __init__(self):
        """
        Initializes the transformer.
        """

        AbstractScript.__init__(self)

    def globalInfo(self):
        """
        Returns a string describing the object.

        @return: a description suitable for displaying in the gui
        """

        return "Calculating the first derivative."

    def accepts(self):
        """
        Returns the class of objects that it accepts.

        @return: the classes
        @rtype: list
        """

        # very in-elegant, but works
        # http://www.prasannatech.net/2009/02/class-object-name-java-interface-jython.html
        return [Class.forName("[[Ljava.lang.Double;")]

    def generates(self):
        """
        Returns the class of objects that it generates.

        @return: the classes
        @rtype: list
        """

        # very in-elegant, but works
        # http://www.prasannatech.net/2009/02/class-object-name-java-interface-jython.html
        return [Class.forName("[[Ljava.lang.Double;")]

    def doExecute(self):
        """
        Executes the flow item.

        @return: None if everything is fine, otherwise error message
        @rtype: str
        """
        
        inp  = self.m_InputToken.getPayload()
        rows = []
        for n in xrange(len(inp)):
            rowin  = inp[n]
            rowout = zeros(len(rowin) - 1, java.lang.Double)
            for i in xrange(len(rowin) - 1):
                rowout[i] = rowin[i+1] - rowin[i]
            rows.append(rowout)

        matrix = array(rows, Class.forName('[Ljava.lang.Double;'))
        self.m_OutputToken = Token(matrix)
        return None

