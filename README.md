# AI PDF Study Guide Generator

Converts lecture PDFs into structured study guides using a local LLM (Mistral via Ollama). Automatically extracts text, chunks it intelligently, summarizes in parallel, and refines the output into clean, exam-ready notes.

## How it works

The tool runs your PDF through a five-stage pipeline:

1. **Extract** — pulls raw text from the PDF page by page
2. **Chunk** — splits text on sentence boundaries (not arbitrary character limits) to preserve meaning
3. **Summarize** — sends each chunk to Mistral in parallel using `ThreadPoolExecutor` for speed
4. **Combine** — merges all summaries into a single cohesive document
5. **Refine** — makes a final pass to add structure, remove repetition, and format for studying

Output is saved as `notes.txt` in the same directory.

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- Mistral model pulled via Ollama

## Installation

```bash
# Clone the repo
git clone https://github.com/Vences33/ai-study-guide.git
cd ai-study-guide

# Install dependencies
pip install -r requirements.txt

# Pull the Mistral model (one-time setup)
ollama pull mistral
```

## Usage

```bash
python main.py your_lecture.pdf
```

Your study guide will be saved to `notes.txt`.

## Project structure

```
├── main.py        # Entry point — orchestrates the full pipeline
├── extract.py     # PDF text extraction using pypdf
├── chunk.py       # Sentence-aware text chunking
├── summarize.py   # Parallel LLM summarization of each chunk
├── combine.py     # Merges chunk summaries into one document
└── refine.py      # Final formatting and cleanup pass
```

## Example output

Input: An old 8 page, CS-251 Final exam
Output:  **CS 251 Final Exam Study Guide,**

**Exam Concepts and Key Definitions**

1. Access Modifiers
   - `private`: A member variable declared with the `private` access modifier is visible only to methods within the same class. It cannot be accessed by methods in nested classes or other top-level classes in the same package.

2. Overriding Methods
   - `super`: The keyword `super` is used to call the parent class version of an overridden method.

3. Variable Access
   - `this`: The keyword `this` can be used to access a member variable hidden by a local variable.

4. Interfaces and Enhanced For Loops
   - `Iterable`: An interface that allows a class to be used in an enhanced for loop (for-each loop).

5. Inherited Methods
   - All reference types in Java inherit the `toString()` method.

6. Exception Handling
   - Keywords: `try`, `catch`, and `finally`.

7. Ternary Operator Example
   - The ternary operator can be used for simple conditional expressions, such as the following example where it evaluates to 'B'.
     ```java
     char c = ( condition ) ? "ABCD".charAt(1) : "EFGH".charAt(1);
     ```

8. Variable Initialization Values
   - An uninitialized `int` member variable has a default value of 0.
   - An uninitialized `Integer` member variable has a default value of `null`.

9. Custom Painting in JPanel
   - To perform custom painting in a JPanel, you should override the `paintComponent()` method.

10. Map Interface Methods
    - `entrySet()`: One method provided by the Map interface that views the map as a collection.

**Programming Tasks and Examples**

1. Creating a new class called `DoubleCounter` that extends `Counter` and counts up by two from an initial value:

```java
public class DoubleCounter extends Counter {
    public DoubleCounter(int initialValue) {
        super(initialValue);
    }

    @Override
    public void increment() {
        super.increment();  // call the parent class's increment method
        if (value % 2 != 0) {   // if the value is odd, increment again
            increment();
        }
    }
}
```

2. Improper modification of instance variables from a static context like the main method:

```java
public class MyClass { private int x = 10; public static void main ( String [] args ) { x ++; System . out . println ( x ); } }
```

   *Note: This is not good practice as it can lead to unexpected behavior in your program.*

3. Additional study notes:
   - Incorrect variable scope can lead to errors in inner classes or anonymous classes.
   - When creating a list, the generic type must be specified both when declaring the variable and when instantiating it.
   - Program examples for reading from files, creating JButtons, implementing interfaces for to-do lists, using Swing components in a BorderLayout, etc.
(Some text removed that contained names of professor and university.)

## Built with

- [Ollama](https://ollama.com) — local LLM inference
- [Mistral](https://mistral.ai) — language model
- [pypdf](https://pypdf.readthedocs.io) — PDF text extraction
- [tqdm](https://tqdm.github.io) — progress tracking
- `concurrent.futures` — parallel chunk processing
