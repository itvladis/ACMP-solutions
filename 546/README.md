# Booklet printing

When a booklet is printed, four pages go on each sheet of paper: two on the front and
two on the back, so that after stacking the sheets and folding them in half the pages
come in the right order. For example, a 4-page booklet uses one sheet: the front holds
pages 4 and 1, the back holds pages 2 and 3. If the number of pages is not a multiple
of four, blank pages are added at the end, using the minimal number of sheets. Generate
the printing order for a booklet with the given number of pages.

**Input** (`input.txt`): the number of pages (a positive integer not exceeding 500).
**Output** (`output.txt`): one command per line: sheet number, side (1 for front, 2 for back), the page printed
on the left and the page printed on the right. A blank page is denoted by 0; a side
that is completely blank may be omitted.

Examples: `4` → `1 1 4 1` / `1 2 2 3`.

https://acmp.ru/index.asp?main=task&id_task=546
