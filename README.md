# python-app-prometheus

Uma simples aplicação python-flask instrumentalizada para entregar métricas para o prometheus

## Usando a imagem

Caso deseje executar a imagem para testes simples  

```bash
docker run --name jojoba -p 8080:5000 -d jojoba:latest
```

## Variáveis de ambiente

**REQUEST_LATENCY:**&nbsp;&nbsp; Adiciona um intervalo de tempo para que as requisições demorem mais pra ocorrer.  

```bash
docker run --name jojoba -p 8080:5000 -e "REQUEST_LATENCY=10" -d jojoba:latest
```
