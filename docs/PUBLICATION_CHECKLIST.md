# Publication Checklist

Before publishing:

- [ ] Search the repository for private names, addresses, phone numbers, account numbers, real contracts, medical details, and personal financial details.
- [ ] Confirm `examples/` contains only synthetic data.
- [ ] Confirm no private workspace path appears in public docs.
- [ ] Run tests.
- [ ] Validate `skill/`.
- [ ] Review README install commands.
- [ ] Decide the GitHub repository owner and final URL.
- [ ] Confirm README clone URL points to the final GitHub repository.

Recommended commands:

```bash
python3 -m unittest discover -s tests
python3 /path/to/skill-creator/scripts/quick_validate.py skill
grep -R "your-real-name-or-private-keyword" .
```
