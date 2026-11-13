# Evidence provenance

`after-check-summary.csv` is a deterministic aggregation of the original local Prowler CIS export. Only `CHECKID`, `STATUS`, and the number of matching rows are retained. Account IDs, resource IDs/names, timestamps, extended finding text, and credentials are not published.

The aggregation preserves **170 result rows**: **76 PASS**, **91 FAIL**, and **3 MANUAL**. The checked-in helper recalculates totals from the aggregate.

`results.json` identifies each baseline's source. Before-scan totals come from [the original published lab](https://medium.com/@romancharleston/i-built-a-vulnerable-aws-environment-for-my-capstone-class-f30b8e108fa6); after-scan totals come from the retained local export. They are historical results, not a fresh cloud scan.

The Terraform fixture contains no concrete secret values. Its access-key resource would create a credential if someone deployed it, so the file is published as an inert `.tf.example` for source review. Raw state, provider caches, credential CSVs, and PEM files are deliberately excluded.
