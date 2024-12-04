# LaTeX walkthrough
## Table of contents
- [How to start document](#how-to-start-document)
- [Basic text](#basic-text)
- [Subsections](#subsections)
- [How to do lists](#how-to-do-lists)
- [Placing images](#placing-images)
- [Math writing](#math-writing)
  - [Inline math](#inline-math)
  - [Equation maths (Preferred method)](#equation-maths-preferred-method)
- [Tables](#tables)
- [Adding code](#adding-code)


## How to start document
```latex
\documentclass{article} % Document type
\usepackage{amsmath}    % For advanced math typesetting
\usepackage{graphicx}   % For including images
\usepackage{hyperref}   % For hyperlinks

\begin{document}

% Content goes here

\end{document}
```

## Basic text
```latex
\textbf{Bold text}, \textit{Italic text}, \underline{Underlined text}
```

## Subsections
```latex
\section{Main Section}
\subsection{Subsection}
\subsubsection{Subsubsection}
```

## How to do lists
```latex
\begin{itemize}
    \item First item
    \item Second item
\end{itemize}

```

## Placing images
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.5\textwidth]{example.png}
    \caption{This is an example image.}
    \label{fig:example}
\end{figure}

```
## Math writing
### Inline math
```latex
This is an inline equation: $E = mc^2$
```
### Equation maths (Profred method)
```latex
\begin{equation}
E = mc^2
\end{equation}
```
## Tables
```latex
\begin{table}[h]
    \centering
    \begin{tabular}{|c|c|c|}
        \hline
        Header1 & Header2 & Header3 \\ \hline
        Data1   & Data2   & Data3   \\ \hline
    \end{tabular}
    \caption{This is a table.}
    \label{tab:example}
\end{table}
```

## Adding code
```latex
\begin{verbatim}
Your code here
\end{verbatim}

```
