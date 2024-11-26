# MAIRD

**M**aid for **AI** **R**esearch and **D**evelopment

We use
- `vllm` to serve text models.
- `infinity emb` to serve text embedding and rerank models.
- `litellm` as proxy to serve all of these above.

These servers are OpenAI, Cohere, JinaAI compatible.

## Setup environment variables

Make a file at root, `vllm/.env`,
```bash
HUGGING_FACE_HUB_TOKEN=<your_api_key>
```

## Launch it

You need docker, nvidia runtime for docker, and docker compose. The setup varies on different OSes. Please have a look,
- [docker](https://docs.docker.com/engine/install/)
- [nvidia docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
- [docker compose](https://docs.docker.com/compose/install/linux/)

Because downloading model weights happens only once and can take very long time, we need to run some docker images first, 

```bash
docker compose -f one_time.yaml up
```

```bash
docker compose -f one_time.yaml down
```

Read `compose.yaml`, and other config files before running.

```bash
docker compose up
```

```bash
docker compose down --rmi local
```

## Try it

In your project folder with proper environment,
```bash
pip install openai==1.55.0 cohere==5.11.4
```

Read the file before running,
```bash
python main.py
```