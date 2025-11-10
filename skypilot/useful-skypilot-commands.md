# Useful SkyPilot Commands

[https://docs.skypilot.co/en/latest/overview.html](https://docs.skypilot.co/en/latest/overview.html)

## Installation
```
uv tool install --with pip "skypilot[gcp]"
```

## Common commands

### Check to verify cloud access
```
sky check gcp
```

### Status to see all clusters
```
sky status
```

### Dashboard for a nicer UI
```
sky dashboard
```

## Development Cluster

### Launch cluster with L4 GPU and 5 hours autostop
```
sky launch -c dev --gpus L4 --workdir . -i 300
```

### SSH into cluster
```
ssh dev
```

### Stop/ Terminate a cluster
```
sky [stop/down] dev # down to terminate
```
