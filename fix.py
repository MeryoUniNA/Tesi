with open('Capitoli/Capitolo_3/3.2_Fase1.tex', 'r') as f:
    text = f.read()
import re
text = re.sub(r'blocco di invocazione bash:\n\n\\begin\{lstlisting\}', r'blocco di invocazione bash:\n\\begin{lstlisting}', text)
with open('Capitoli/Capitolo_3/3.2_Fase1.tex', 'w') as f:
    f.write(text)
