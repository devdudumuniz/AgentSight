# Basic AgentSight Capture

```bash
python -m pip install -e ".[dev,capture]"
agentsight doctor
agentsight capture --mock --label demo --scope region --region 0,0,200,120 --consent --output .vision-runs/demo --json
agentsight report --run .vision-runs/demo
```

For real desktop capture, remove `--mock` and provide a real screen region:

```bash
agentsight capture --label real-region --scope region --region 100,100,800,600 --consent --output .vision-runs/real-region --json
```
