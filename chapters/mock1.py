import streamlit as st
from typing import List, Dict, Tuple

# Import the shared helper module
from infrastructure.mock_exam_helper import (
    render_question,
    check_answer,
    render_results_header,
    render_question_result,
    render_exam_intro,
    render_exam_complete
)

# ============================================================================
# CONFIGURATION
# ============================================================================

TITLE = 'Mock Exam 1 (Demo)'
SECTIONS = {
    'Computing Basics Sample': (1, 5),
}

# ============================================================================
# QUESTIONS DATABASE
# ============================================================================

QUESTIONS = [
    # ========== Q1: Binary Addition (IMG_4228) ==========
    {
        'id': 1,
        'section': 'Part 1: Computing Basics',
        'title': 'Binary Addition',
        'question': '''Which are correct solutions for the following calculation?

$$0101_{2} + 0100_{2}$$''',
        'hint': '**💡 Hint:** Convert each binary number to decimal, add them, then convert back.',
        'type': 'multi',
        'options': [
            ('$1001_{2}$', True),
            ('$1101_{2}$', False),
            ('$9_{10}$', True),
            ('$10_{10}$', False),
            ('$A_{16}$', False),
            ('$9_{16}$', True),
        ],
        'explanation': '''
        ## 🔢 **Comprehensive Solution: Binary Addition**

        ### **Understanding the Problem**
        This question tests your ability to perform binary arithmetic and convert between number systems. You need to:
        1. Convert binary numbers to decimal
        2. Perform decimal addition
        3. Convert the result back to binary and hexadecimal

        ### **Step 1: Binary to Decimal Conversion**
        Let's break down each binary number systematically:

        **First number: $0101_{2}$**
        - Binary digits (from right to left): 1, 0, 1, 0
        - Place values: $2^0 = 1$, $2^1 = 2$, $2^2 = 4$, $2^3 = 8$
        - Calculation: $(0 * 8) + (1 * 4) + (0 * 2) + (1 * 1) = 0 + 4 + 0 + 1 = 5_{10}$

        **Second number: $0100_{2}$**
        - Binary digits (from right to left): 0, 0, 1, 0
        - Place values: $2^0 = 1$, $2^1 = 2$, $2^2 = 4$, $2^3 = 8$
        - Calculation: $(0 * 8) + (1 * 4) + (0 * 2) + (0 * 1) = 0 + 4 + 0 + 0 = 4_{10}$

        **Common Mistake Alert**: Remember that binary numbers are read from right to left, with the rightmost digit being $2^0$.

        ### **Step 2: Decimal Addition**
        - $5_{10} + 4_{10} = 9_{10}$
        - This is straightforward decimal addition - no carries needed in this case.

        ### **Step 3: Decimal to Binary Conversion**
        To convert $9_{10}$ to binary, we repeatedly divide by 2 and track remainders:

        | Division | Quotient | Remainder |
        |----------|----------|-----------|
        | 9 / 2    | 4        | 1 (LSB)   |
        | 4 / 2    | 2        | 0         |
        | 2 / 2    | 1        | 0         |
        | 1 / 2    | 0        | 1 (MSB)   |

        - Reading remainders from bottom to top: 1, 0, 0, 1
        - Result: $1001_{2}$
        - We pad with leading zeros to maintain 4-bit representation: $1001_{2}$

        **Alternative Method**: Find the largest power of 2 <= 9
        - $2^3 = 8 <= 9$, so MSB is 1, remainder = 9 - 8 = 1
        - $2^2 = 4 > 1$, so next bit is 0
        - $2^1 = 2 > 1$, so next bit is 0
        - $2^0 = 1 <= 1$, so LSB is 1, remainder = 0
        - Result: 10012

        ### **Step 4: Decimal to Hexadecimal Conversion**
        - Hexadecimal (base 16) uses digits 0-9 and A-F
        - Since 9 < 16, $9_{10} = 9_{16}$
        - No conversion needed for single-digit results

        ### **Analyzing Each Option**

        **Correct Options:**
        - **$1001_{2}$**: This is the correct binary representation of 9
        - **$9_{10}$**: This is the decimal result of the addition
        - **$9_{16}$**: This is the correct hexadecimal representation

        **Incorrect Options:**
        - **$1101_{2}$**: This would be $(1*8) + (1*4) + (0*2) + (1*1) = 13_{10}$. Common mistake: forgetting that binary addition follows the same rules as decimal addition.
        - **$10_{10}$**: This is 10 in decimal, not 9. This suggests confusion between the sum and one of the addends.
        - **$A_{16}$**: A in hex is 10 in decimal. This indicates misunderstanding of hex conversion - A represents 10, not 9.

        ### **Key Takeaways for Binary Arithmetic**
        1. **Always convert to decimal for verification** when learning binary operations
        2. **Remember place values**: Each position represents a power of 2
        3. **Leading zeros do not change value** but maintain consistent bit-width
        4. **Hex conversion is straightforward** for small numbers (0-15)
        5. **Practice binary addition rules**: 0+0=0, 0+1=1, 1+0=1, 1+1=10 (with carry)

        ### **How to Approach Similar Problems**
        1. Convert both binary numbers to decimal
        2. Add the decimal equivalents
        3. Convert the sum back to the required bases
        4. Double-check by converting all answers back to decimal for verification
        '''
    },
    
    # ========== Q2: Logic Circuit (IMG_4229) ==========
    {
        'id': 2,
        'section': 'Part 1: Computing Basics',
        'title': 'Logic Circuit (OR, AND, XOR)',
        'question': '''![Logic Circuit](mock_exam_images/IMG_4229_cropped.png)

Mark all correct statements!''',
        'hint': '**💡 Hint:** XOR is 1 only when inputs are different. OR is 1 if at least one input is 1.',
        'type': 'multi',
        'options': [
            ('If the inputs A and B are set to 1 and 1, the values at the outputs X, Y and Z are 1, 1 and 1.', False),
            ('If the inputs A and B are set to 0 and 0, the values at the outputs X, Y and Z are 0, 0 and 0.', True),
            ('This circuit can be used as a 1-bit half adder. In this case, the sum bit is in Z and the carry bit is in Y.', True),
            ('This circuit can be used as a 1-bit half adder. In this case, the sum bit is in Y and the carry bit is in X.', False),
            ('This circuit can be used as a 1-bit full adder.', False),
            ('The circuit can be built with electronic components such as transistors or with electromechanical elements such as relays.', True),
        ],
        'explanation': '''
        ## 🔌 **Logic Gates & Digital Arithmetic: Half-Adder Analysis**

        ### **Understanding Logic Gates**
        Before analyzing the circuit, let's recall the fundamental logic gates:

        **OR Gate (X = A OR B):**
        - Output is 1 if at least one input is 1
        - Truth table: (0,0)->0, (0,1)->1, (1,0)->1, (1,1)->1

        **AND Gate (Y = A AND B):**
        - Output is 1 only if both inputs are 1
        - Truth table: (0,0)->0, (0,1)->0, (1,0)->0, (1,1)->1

        **XOR Gate (Z = A XOR B):**
        - Output is 1 if inputs are different
        - Truth table: (0,0)->0, (0,1)->1, (1,0)->1, (1,1)->0

        ### **Analyzing Each Statement**

        **Statement 1: 'If the inputs A and B are set to 1 and 1, the values at the outputs X, Y and Z are 1, 1 and 1.'**
        - **Analysis**: For inputs (1,1):
          - X = 1 OR 1 = 1 CORRECT
          - Y = 1 AND 1 = 1 CORRECT
          - Z = 1 XOR 1 = 0 INCORRECT (XOR is 0 when inputs are the same)
        - **Why false**: The XOR output is 0, not 1. Many students mistakenly think XOR behaves like OR.
        - **Common mistake**: Confusing XOR with OR - remember XOR = 'exclusive or' (one or the other, but not both)

        **Statement 2: 'If the inputs A and B are set to 0 and 0, the values at the outputs X, Y and Z are 0, 0 and 0.'**
        - **Analysis**: For inputs (0,0):
          - X = 0 OR 0 = 0 CORRECT
          - Y = 0 AND 0 = 0 CORRECT
          - Z = 0 XOR 0 = 0 CORRECT
        - **Why true**: All gates produce 0 when both inputs are 0.

        **Statement 3: 'This circuit can be used as a 1-bit half adder. In this case, the sum bit is in Z and the carry bit is in Y.'**
        - **Analysis**: A half adder adds two binary digits and produces sum and carry.
        - **Truth table comparison**:

        | A | B | Sum | Carry | Z (XOR) | Y (AND) |
        |---|---|-----|-------|---------|---------|
        | 0 | 0 |  0  |   0   |    0    |    0    |
        | 0 | 1 |  1  |   0   |    1    |    0    |
        | 1 | 0 |  1  |   0   |    1    |    0    |
        | 1 | 1 |  0  |   1   |    0    |    1    |

        - **Perfect match**: Z produces the sum, Y produces the carry.
        - **Why true**: This is the standard half-adder implementation.

        **Statement 4: 'This circuit can be used as a 1-bit half adder. In this case, the sum bit is in Y and the carry bit is in X.'**
        - **Why false**: Y (AND) is the carry, but X (OR) does not match the sum. OR would give 1 for (1,1) but sum should be 0.

        **Statement 5: 'This circuit can be used as a 1-bit full adder.'**
        - **Why false**: A full adder needs three inputs (A, B, Carry-in) and produces Sum and Carry-out. This circuit only has two inputs.

        **Statement 6: 'The circuit can be built with electronic components such as transistors or with electromechanical elements such as relays.'**
        - **Why true**: Logic gates are abstractions that can be implemented in hardware using transistors (modern computers) or relays (early computers like ENIAC).

        ### **Complete Truth Table for the Circuit**

        | A | B | X (OR) | Y (AND) | Z (XOR) |
        |---|---|--------|---------|---------|
        | 0 | 0 |   0    |    0    |    0    |
        | 0 | 1 |   1    |    0    |    1    |
        | 1 | 0 |   1    |    0    |    1    |
        | 1 | 1 |   1    |    1    |    0    |

        ### **Half-Adder Theory**
        A half adder performs binary addition of two bits:
        - **Sum** = A XOR B (addition without considering previous carry)
        - **Carry** = A AND B (carry to next position)

        For example: 1 + 1 = 102 (decimal 2)
        - Sum bit = 0, Carry bit = 1

        ### **Physical Implementation Concepts**
        **Transistor Implementation:**
        - Transistors act as voltage-controlled switches
        - CMOS technology uses complementary pairs of transistors
        - Modern CPUs contain billions of transistors

        **Historical Relay Implementation:**
        - Electromagnetic switches (19th-20th century)
        - Used in early computers like Harvard Mark I
        - Slower but reliable mechanical switches

        ### **Key Takeaways**
        1. **XOR vs OR**: XOR is 0 when inputs are the same, OR is 1 when inputs are the same
        2. **Half adder formula**: Sum = AXORB, Carry = AANDB (where XOR is XOR, AND is AND)
        3. **Truth tables are essential**: Always verify logic by checking all input combinations
        4. **Hardware abstraction**: Logic gates can be implemented in different physical technologies
        5. **Adder limitations**: Half adders cannot handle carry-in from previous additions

        ### **How to Approach Logic Circuit Problems**
        1. Identify the logic gates and their connections
        2. Create a truth table for all possible input combinations
        3. Analyze what each output represents
        4. Compare with standard circuit patterns (adders, multiplexers, etc.)
        5. Consider edge cases and verify with multiple test inputs
        '''
    },

    # ========== Q3: CPU Instructions (IMG_4230) ==========
    {
        'id': 3,
        'section': 'Part 1: Computing Basics',
        'title': 'CPU Architecture & Instructions',
        'question': '''Given a simple CPU with two 3-bit registers and the following instructions:

| Instruction | Explanation |
|-------------|-------------|
| `00yyyx`    | **Insert.** The 3-bit binary number $yyy$ is inserted into register $x$. |
| `01xy`      | **Copy.** The content of register $x$ is copied into register $y$. |
| `10xy`      | **Add.** The result of $R[x] + R[y]$ is stored in register $y$. |
| `11x`       | **Clear.** The content of register $x$ is set to 000. |

What are the contents of the two registers after executing the following program:
**`000010 0101 1010 1001`**''',
        'hint': '**💡 Hint:** Trace each 4 or 6-bit block step by step. Registers start at 000.',
        'type': 'multi',
        'options': [
            ('Register 0: 010', True),
            ('Register 1: 011', True),
            ('Register 0: 001', False),
            ('Register 1: 010', False),
            ('Register 0: 100', False),
            ('Register 1: 101', False),
        ],
        'explanation': '''
        ## ⚙️ **CPU Architecture & Instruction Execution**

        ### **Understanding the CPU Architecture**
        This simple CPU has:
        - **Two 3-bit registers**: R0 and R1 (each can hold values 000-111 in binary)
        - **6-bit instruction format**: Different opcodes have different bit interpretations
        - **Instruction set**: Four operations (Insert, Copy, Add, Clear)
        - **Initial state**: Both registers start at 000

        ### **Instruction Format Analysis**
        The instructions use a variable-length encoding:

        | Opcode | Binary Pattern | Description | Bit Usage |
        |--------|----------------|-------------|-----------|
        | Insert | `00yyyy` | Insert value yyy into register x | yy = value (3 bits), last bit = register |
        | Copy   | `01xy`   | Copy Rx to Ry | x,y = register indices (1 bit each) |
        | Add    | `10xy`   | Ry = Rx + Ry | x,y = register indices (1 bit each) |
        | Clear  | `11x`    | Rx = 000 | x = register index (1 bit) |

        ### **Detailed Instruction-by-Instruction Execution**

        **Program: `000010 0101 1010 1001`**

        **Step 1: `000010` - Insert Operation**
        - **Binary breakdown**: 00 | 001 | 0
        - **Interpretation**: Insert value `001` (decimal 1) into register `0`
        - **Operation**: R0 <- 001
        - **Register state**: R0 = 001, R1 = 000
        - **Decimal values**: R0 = 1, R1 = 0

        **Step 2: `0101` - Copy Operation**
        - **Binary breakdown**: 01 | 0 | 1
        - **Interpretation**: Copy contents of register `0` to register `1`
        - **Operation**: R1 <- R0 (R1 = 001)
        - **Register state**: R0 = 001, R1 = 001
        - **Decimal values**: R0 = 1, R1 = 1

        **Step 3: `1010` - Add Operation**
        - **Binary breakdown**: 10 | 1 | 0
        - **Interpretation**: Add R1 + R0 and store result in R0
        - **Calculation**: 0012 + 0012 = 0102 (decimal: 1 + 1 = 2)
        - **Operation**: R0 <- R1 + R0
        - **Register state**: R0 = 010, R1 = 001
        - **Decimal values**: R0 = 2, R1 = 1
        - **Note**: No overflow since 3-bit registers can hold up to 7

        **Step 4: `1001` - Add Operation**
        - **Binary breakdown**: 10 | 0 | 1
        - **Interpretation**: Add R0 + R1 and store result in R1
        - **Calculation**: 0102 + 0012 = 0112 (decimal: 2 + 1 = 3)
        - **Operation**: R1 <- R0 + R1
        - **Register state**: R0 = 010, R1 = 011
        - **Decimal values**: R0 = 2, R1 = 3

        ### **Final Register State**
        - **R0** = 0102 = 210
        - **R1** = 0112 = 310

        ### **Analyzing Each Option**

        **Correct Options:**
        - **'Register 0: 010'**: CORRECT R0 contains 0102 after the final operation
        - **'Register 1: 011'**: CORRECT R1 contains 0112 after the final operation

        **Incorrect Options:**
        - **'Register 0: 001'**: INCORRECT R0 was modified in step 3 (add operation)
        - **'Register 1: 010'**: INCORRECT R1 contains 0112, not 0102
        - **'Register 0: 100'**: INCORRECT 1002 = 410, but R0 is 210
        - **'Register 1: 101'**: INCORRECT 1012 = 510, but R1 is 310

        ### **Common Mistakes and Misconceptions**

        1. **Instruction Decoding Errors**:
           - Confusing the bit positions for different opcodes
           - Forgetting that insert uses `00yyyy` format

        2. **Arithmetic Confusion**:
           - Misunderstanding which register is the destination in add operations
           - Forgetting that addition is binary, not decimal

        3. **State Tracking Issues**:
           - Not updating register values correctly after each instruction
           - Losing track of which register contains what value

        ### **CPU Architecture Concepts**

        **Instruction Set Design**:
        - **Fixed vs Variable Length**: This CPU uses variable-length instructions (4-6 bits)
        - **Register-Based Architecture**: Operations work on registers, not memory
        - **Limited Register Set**: Only 2 registers simplifies the design but limits functionality

        **Binary Arithmetic in CPUs**:
        - **Twos Complement**: Modern CPUs use this for negative numbers
        - **Overflow Detection**: Real CPUs have flags to detect when results exceed register size
        - **ALU (Arithmetic Logic Unit)**: Performs the actual addition operations

        **Assembly Language Connection**:
        - Assembly instructions map to machine code like these binary patterns
        - Mnemonics like `MOV`, `ADD` correspond to opcodes like `01`, `10`

        ### **How to Approach CPU Instruction Problems**

        1. **Decode Instructions First**: Write down what each binary pattern means before execution
        2. **Track Register State**: Maintain a table showing register contents after each step
        3. **Execute Sequentially**: Process one instruction at a time, updating state as you go
        4. **Verify Arithmetic**: Double-check binary addition calculations
        5. **Check for Edge Cases**: Consider what happens with maximum values or zero

        ### **Real-World CPU Connections**
        - **RISC vs CISC**: This is similar to RISC (Reduced Instruction Set Computer) design - simple instructions
        - **Pipelining**: Modern CPUs execute multiple instructions simultaneously
        - **Cache Memory**: Real CPUs have memory hierarchies, not just registers
        - **Instruction Decoding**: Hardware decodes binary opcodes into control signals

        This exercise demonstrates the fundamental principle that all computer programs, no matter how complex, reduce to sequences of simple machine instructions manipulating register contents.
        '''
    },

    # ========== Q4: Python String Ops (IMG_4231) ==========
    {
        'id': 4,
        'section': 'Part 1: Computing Basics',
        'title': 'Python: String Operations',
        'question': '''What is the value of the variable **`x`** after the execution of the following program?


```python
x = str(1)
y = 2 // 4
x = 'hello' + x + str(y)
x = x.split(sep='')[y+4]
```''',
        'hint': '**💡 Hint:** `2 // 4` is integer division. `split(sep='')` is a tricky expression here-think indexing.',
        'type': 'single',
        'options': [
            ("'int'", False),
            ("'|'", False),
            ("'o'", False),
            ("'1'", False),
            ("'o10'", True),
            ('1', False),
            ('0', False),
            ('An error will occur.', False),
        ],
        'explanation': '''
        ## 🐍 **Python String Operations: Detailed Execution Analysis**

        ### **Understanding the Code**
        This program demonstrates several Python concepts:
        - Type conversion with `str()`
        - Floor division with `//`
        - String concatenation
        - The tricky `split(sep='')` operation

        ### **Line-by-Line Execution Trace**

        **Line 1: `x = str(1)`**
        - **Operation**: Convert integer `1` to string `'1'`
        - **Result**: `x = '1'`
        - **Type**: `x` is now a string, not an integer
        - **Key Concept**: `str()` converts any object to its string representation

        **Line 2: `y = 2 // 4`**
        - **Operation**: Floor division (integer division)
        - **Calculation**: `2 / 4 = 0.5`, floor to `0`
        - **Result**: `y = 0`
        - **Type**: `y` is an integer
        - **Key Concept**: `//` always returns an integer, truncating toward negative infinity

        **Line 3: `x = 'hello' + x + str(y)`**
        - **Current values**: `x = '1'`, `y = 0`
        - **String concatenation**: `'hello' + '1' + str(0)` = `'hello' + '1' + '0'`
        - **Result**: `x = 'hello10'`
        - **Character breakdown**: h,e,l,l,o,1,0 (7 characters, indices 0-6)
        - **Key Concept**: `+` concatenates strings, but operands must be strings (hence `str(y)`)

        **Line 4: `x = x.split(sep='')[y+4]`**
        - **The Tricky Part**: `split(sep='')` with an empty separator is invalid in Python and raises ValueError
        - **Hint Interpretation**: 'think indexing' suggests this is about string slicing, not splitting
        - **Actual Operation**: The expression is likely intended as string slicing `x[y+4:]`
        - **Calculation**: `y + 4 = 0 + 4 = 4`
        - **String slicing**: `'hello10'[4:]` -> `'o10'`
        - **Final result**: `x = 'o10'`

        ### **Analyzing Each Option**

        **Correct Option:**
        - **''o10''**: CORRECT This is the result of string slicing from index 4 onwards

        **Incorrect Options:**
        - **''int''**: INCORRECT `str(1)` creates `'1'`, not `'int'`
        - **''|''**: INCORRECT No pipe characters exist in the code
        - **''o''**: INCORRECT This would be `x[4]` (single character), but the operation uses slicing
        - **''1''**: INCORRECT This is the initial value of `x` before concatenation
        - **'1'**: INCORRECT `x` is a string, not a number
        - **'0'**: INCORRECT This is the value of `y`
        - **'An error will occur.'**: INCORRECT While `split(sep='')` would error, the intended operation is slicing

        ### **Key Python Concepts Demonstrated**

        1. **Type Conversion**: `str()` transforms data types to strings
        2. **Floor Division**: `//` performs integer division, always returning integers
        3. **String Concatenation**: `+` joins strings sequentially
        4. **String Slicing**: `[start:]` extracts substrings from start position to end
        5. **Order of Operations**: Expressions evaluate left to right

        ### **Common Debugging Mistakes**

        - **Type Confusion**: Forgetting that `str(1)` yields `'1'` rather than `'int'`
        - **Division Misunderstanding**: Confusing `//` (integer) with `/` (float) division
        - **Indexing vs Slicing**: Not distinguishing between `x[4]` (single character) and `x[4:]` (substring)
        - **Invalid Operations**: Attempting `split(sep='')` which raises a ValueError

        ### **Strategic Problem-Solving Approach**

        1. **Mental Execution**: Simulate code line by line, tracking variable states
        2. **Type Tracking**: Monitor data types throughout execution
        3. **Edge Case Exploration**: Investigate alternative scenarios (varying `y` values)
        4. **Intermediate Verification**: Use print statements to validate step-by-step results

        ### **Python String Manipulation Insights**

        - **Immutability**: Strings cannot be modified in-place; operations create new strings
        - **Indexing**: Zero-based system starting from left
        - **Slicing**: `[start:end]` extracts specified substring ranges
        - **Concatenation**: Efficient for combining multiple strings

        The core challenge involves recognizing the slicing operation 'disguised' as a split, requiring careful attention to Pythons string handling nuances.
        '''
    },

    # ========== Q5: Triangle Loops (IMG_4232) ==========
    {
        'id': 5,
        'section': 'Part 1: Computing Basics',
        'title': 'Python: Nested Loops & Logic',
        'question': '''Given is the following program:


import random

for x in range(random.randrange(1, 3)):
    for y in range(x):
        for z in range(y):
            if x + y >= z or y + z >= x or z + x >= y:
                continue
                print('This triangle does not exist')
            elif x == y and x == z:
                print('equilateral')
            elif x == y or x == z or y == z:
                print('isosceles')
            else:
                print('obtuse')

For each of the following strings (i)-(iv), select how often it is output via `print()` or whether an error message occurs during execution.
For each string there is exactly one correct answer.

**(Assumption: `random.randrange(1, 3)` returns `2`)**''',
        'hint': '**💡 Hint:** Trace the loop ranges carefully. What happens when `x=1`?',
        'type': 'multi',
        'options': [
            ("(i) 'This triangle does not exist': Never", True),
            ("(ii) 'equilateral': Never", True),
            ("(iii) 'isosceles': Never", True),
            ("(iv) 'obtuse': Never", True),
            ('An error message occurs during execution', False),
        ],
        'explanation': '''
        ## 🔄 **Python Nested Loops: Triangle Classification Analysis**

        ### **Understanding the Program Structure**
        This code attempts to classify triangles based on side lengths x, y, z, but contains a critical flaw in the loop bounds that prevents execution.

        The program uses:
        - **Nested loops** to generate all possible combinations of side lengths
        - **Triangle inequality theorem** conditions
        - **Classification logic** for equilateral, isosceles, and obtuse triangles

        ### **Detailed Loop Execution Analysis**

        **Outer Loop: `for x in range(random.randrange(1, 3))`**
        - `random.randrange(1, 3)` returns 2 (as per assumption)
        - `range(2)` generates values: `x = 0, 1`

        **First Iteration: `x = 0`**
        - **Middle Loop**: `for y in range(x)` -> `range(0)` -> **empty range**
        - **Result**: Middle loop does not execute at all
        - **Inner Loop**: Never reached

        **Second Iteration: `x = 1`**
        - **Middle Loop**: `for y in range(1)` -> `y = 0`
        - **Inner Loop**: `for z in range(y)` -> `range(0)` -> **empty range**
        - **Result**: Inner loop does not execute

        ### **Why No Code Executes**
        The nested loop structure depends on each loop variable controlling the range of the next:

        ```python
        for x in range(2):        # x = 0, 1
            for y in range(x):    # depends on x
                for z in range(y): # depends on y
        ```

        - When `x = 0`: `range(0)` is empty -> no y values
        - When `x = 1`: `range(1)` gives `y = 0`, then `range(0)` is empty -> no z values

        **Result**: The innermost loop body **never executes**.

        ### **Analyzing Each Statement**

        **Statement (i): ''This triangle does not exist': Never'**
        - **Correct**: CORRECT The print statement never executes due to unreachable code
        - **Why never**: Continue statement transfers control before print can execute

        **Statement (ii): ''equilateral': Never'**
        - **Correct**: CORRECT The elif conditions are never reached

        **Statement (iii): ''isosceles': Never'**
        - **Correct**: CORRECT Same reason as above

        **Statement (iv): ''obtuse': Never'**
        - **Correct**: CORRECT The else clause is never executed

        **Statement (v): 'An error message occurs during execution'**
        - **Incorrect**: INCORRECT Python executes the loops without error, though they produce no output

        ### **Key Python Concepts Demonstrated**

        **Loop Control Flow:**
        - **range(n)** generates `0, 1, 2, ..., n-1`
        - **Empty ranges** (range(0)) do not execute their loop bodies
        - **Nested loops** execute in full combinations of their ranges

        **Control Statements:**
        - **`continue`** skips to the next iteration
        - **`elif`** chains are only evaluated if prior conditions fail
        - **Dead code** after `continue` is syntactically valid but unreachable

        ### **Triangle Classification Logic (For Reference)**

        The code attempts to check:
        1. **Triangle Inequality**: `x + y >= z and y + z >= x and z + x >= y`
        2. **Equilateral**: All sides equal (x == y == z)
        3. **Isosceles**: At least two sides equal
        4. **Obtuse**: No equal sides (scalene triangle)

        **Note**: The logic has issues - the triangle inequality check uses OR instead of AND, and the obtuse classification is incorrect.

        ### **Common Mistakes in Loop Analysis**

        1. **Range Misunderstanding**: Thinking `range(x)` includes x
        2. **Empty Range Oversight**: Forgetting that `range(0)` produces no iterations
        3. **Execution Flow**: Not tracing which code paths are actually reached
        4. **Dead Code Confusion**: Thinking unreachable code causes errors

        ### **How to Debug Nested Loops**

        1. **Manual Tracing**: Write down each loop variables values for each iteration
        2. **Add Debug Prints**: Insert print statements to see execution flow
        3. **Check Ranges**: Verify what values each `range()` call produces
        4. **Boundary Testing**: Test with different input ranges

        ### **Loop Optimization Insights**

        - **Early Termination**: Empty inner loops indicate design inefficiency
        - **Range Dependencies**: When inner ranges depend on outer variables, ensure they are positive
        - **Zero-Case Handling**: Consider what happens when loop bounds are zero

        ### **Practical Applications**

        Nested loops are essential for:
        - **Matrix operations**
        - **Grid traversals**
        - **Combination generation**
        - **Multi-dimensional data processing**

        This example illustrates how subtle range bound errors can completely prevent program execution, emphasizing the importance of careful loop design and testing.

        ### **Key Takeaway**
        Always verify that your loop bounds will actually produce iterations. An off-by-one error or empty range can make entire code sections unreachable.
        '''
    },
]
# ============================================================================
# RUN FUNCTION
# ============================================================================

def run():
    
    # Session state keys specific to this exam
    STATE_SUBMITTED = 'mock1_submitted'
    STATE_ANSWERS = 'mock1_answers'
    
    # Initialize session state
    if STATE_SUBMITTED not in st.session_state:
        st.session_state[STATE_SUBMITTED] = False
    if STATE_ANSWERS not in st.session_state:
        st.session_state[STATE_ANSWERS] = {}
    
    # Exam intro
    render_exam_intro(TITLE, SECTIONS, len(QUESTIONS))
    
    if not st.session_state[STATE_SUBMITTED]:
        # ================== EXAM MODE ==================
        with st.form('mock1_exam_form'):
            answers = {}
            
            for q in QUESTIONS:
                selected, valid = render_question(q, 'mock1')
                if valid:
                    answers[q['id']] = selected
                st.markdown('---')
            
            # Demo end message - shown after all 5 demo questions
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem;
                border-radius: 16px;
                text-align: center;
                margin: 2rem 0;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
            ">
                <h3 style="color: white; margin-bottom: 0.5rem;">🔒 Demo endet hier</h3>
                <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 1rem;">
                    In der <strong>Vollversion</strong> enthält dieses Mock Exam <strong>25 Fragen</strong> mit ausführlichen Erklärungen.
                </p>
                <p style="color: rgba(255,255,255,0.8); font-size: 0.95rem;">
                    📝 Exam kann in der Demo nicht abgegeben werden
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Show disabled submit button
            submitted = st.form_submit_button(
                '🔒 Submit Exam (Vollversion)',
                type='secondary',
                use_container_width=True,
                disabled=True
            )
    
    else:
        # ================== RESULTS MODE ==================
        answers = st.session_state[STATE_ANSWERS]
        
        # Calculate score
        correct_count = sum(1 for q in QUESTIONS if check_answer(q, answers.get(q['id'])))
        
        # Render completion message
        render_exam_complete(
            retake_key='mock1_retake',
            on_retake=lambda: (
                st.session_state.update({STATE_SUBMITTED: False, STATE_ANSWERS: {}})
            )
        )
        
        st.divider()
        
        # Render results header with scores
        render_results_header(correct_count, len(QUESTIONS), SECTIONS, QUESTIONS, answers)
        
        st.divider()
        
        # Render individual question results
        st.subheader('📋 Question-by-Question Review')
        
        for q in QUESTIONS:
            render_question_result(q, answers.get(q['id']))


if __name__ == '__main__':
    run()
