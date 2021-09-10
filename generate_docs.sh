rm -rf "docs/*"
cd mikelint || exit 1

# Loop through all formatters and analysers
for file in {analysers,formatters}/*.py; do
  base=$(basename "$file" .py)
  parent=$(dirname "$file")
  if [ "$base" == '__init__' ]; then
    continue
  fi
  mkdir -p "../docs/$parent"
  pydoc-markdown -I . -m "$parent.$base" --render-toc > "../docs/$parent/$base.md"
done
