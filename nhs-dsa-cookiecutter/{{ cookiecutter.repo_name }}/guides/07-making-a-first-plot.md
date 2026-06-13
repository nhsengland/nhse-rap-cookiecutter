# 7. Making your first plot

A good chart turns a table of numbers into something you can actually *see*.
This guide makes a simple plot with **matplotlib** (already installed in this
project) and saves it into `reports/figures/` so you can drop it into a report
or slide.

## A minimal example

In a notebook or Python shell:

```python
import matplotlib.pyplot as plt

from {{ cookiecutter.module_name }}.config import FIGURES_DIR
from {{ cookiecutter.module_name }}.dataset import load_dataset

# Load the small example data (see the "reading data safely" guide to create it).
df = load_dataset()

# Make a bar chart of age by name.
fig, ax = plt.subplots()
ax.bar(df["name"], df["age"])
ax.set_xlabel("Name")
ax.set_ylabel("Age")
ax.set_title("Age by person")

# Save it into reports/figures so it's easy to find and share.
output_path = FIGURES_DIR / "age_by_person.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
print(f"Saved chart to {output_path}")
```

Run it, and you'll find `age_by_person.png` waiting in `reports/figures/`.

## What each part does

- **`fig, ax = plt.subplots()`** creates a blank figure (`fig`) and a single set
  of axes (`ax`) to draw on. This is the standard, flexible way to start a plot.
- **`ax.bar(...)`** draws the bars. Other handy ones: `ax.plot()` for lines,
  `ax.scatter()` for dots, `ax.hist()` for distributions.
- **Labels and a title** (`set_xlabel`, `set_ylabel`, `set_title`) — never skip
  these. A chart without labels makes the reader guess.
- **`fig.savefig(...)`** writes the image to a file. `dpi=150` makes it crisp;
  `bbox_inches="tight"` trims the whitespace.

## Save figures, don't screenshot them

Saving with `savefig` (rather than screenshotting your notebook) means your
charts are:

- **Reproducible** — re-run the code and get the same image with fresh data.
- **High quality** — proper resolution for reports and slides.
- **Organised** — all in `reports/figures/`, ready to reuse.

When the underlying data changes, you just re-run the cell and the saved figure
updates. No manual screenshots to redo.

## Tips for clearer charts

- **One message per chart.** If you're trying to show two things, make two charts.
- **Label your axes and add units** (e.g. "Age (years)").
- **Pick the right type.** Bars compare categories; lines show change over time;
  histograms show how values are spread.

## Try it

Change the chart to a horizontal bar chart with `ax.barh(...)`, give it a new
title, and save it under a new filename. Open both images from
`reports/figures/` and compare.

➡️ Next: [What good looks like](08-what-good-looks-like.md)
