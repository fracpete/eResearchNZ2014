/*
 * Template of a Groovy transformer.
 *
 * @author FracPete (fracpete at waikato dot ac dot nz)
 * @version $Revision: 7190 $
 */

import adams.flow.core.Token
import adams.flow.core.Unknown
import adams.flow.transformer.AbstractScript

class TemplateTransformer
  extends AbstractScript {

  /**
   * Returns a string describing the object.
   *
   * @return 			a description suitable for displaying in the gui
   */
  public String globalInfo() {
    return "Calculating the first derivative."
  }

  /**
   * Returns the class of objects that it accepts.
   *
   * @return		the accepted classes
   */
  public Class[] accepts() {
    return Double[][].class as Object[]
  }

  /**
   * Returns the class of objects that it generates.
   *
   * @return		the generated classes
   */
  public Class[] generates() {
    return Double[][].class as Object[]
  }

  /**
   * Executes the flow item.
   *
   * @return		null if everything is fine, otherwise error message
   */
  protected String doExecute() {
    Double[][] input = m_InputToken.getPayload()
    Double[][] matrix = new Double[input.length][]
    for (int i = 0; i < input.length; i++) {
      Double[] row = new Double[input[i].length - 1]
      for (int n = 1; n < input[i].length; n++) {
        row[n - 1] = input[i][n] - input[i][n - 1]
      }
      matrix[i] = row
    }
    m_OutputToken = new Token(matrix)
    return null
  }
}

