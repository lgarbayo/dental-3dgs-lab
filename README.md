# dental-3dgs-lab

Experimentos de **3D Gaussian Splatting** sobre escaneos intraorales: de la malla
dental (Teeth3DS+) a un campo de gaussianas entrenado, paso a paso y en notebooks.

| Notebook | Qué hace | GPU |
|---|---|---|
| [`01-vtk-3dgs-poc`](notebooks/01-vtk-3dgs-poc.ipynb) | Malla `.obj` + labels FDI → nube de puntos → *splatting* clásico con VTK. Caracteriza los 600 escaneos del dataset. | No |
| [`02-vtk-interactive-viewer`](notebooks/02-vtk-interactive-viewer.ipynb) | Visor 3D interactivo (ventana nativa VTK) para rotar malla, campo y nube. | No |
| [`03-synthetic-views-for-3dgs`](notebooks/03-synthetic-views-for-3dgs.ipynb) | Renderiza vistas sintéticas con **pose de cámara exacta** (sin COLMAP) → `images/`, `transforms.json`, `init.ply`. | No |
| [`04-train-3dgs-gsplat`](notebooks/04-train-3dgs-gsplat.ipynb) | Entrena gaussianas anisótropas con `gsplat` y evalúa **PSNR en vistas retenidas**. | **Sí** |

Detalle de cada uno en [`notebooks/README.md`](notebooks/README.md).

## Puesta en marcha

```bash
uv sync                      # entorno de los notebooks 01-03
./scripts/fetch_teeth3ds.sh  # descarga Teeth3DS+ en data/raw (~7,3 GiB; --subset para ~300 MiB)
uv run jupyter notebook
```

`uv run` es necesario para que el kernel use el `.venv` del proyecto; lanzar
`jupyter` a secas usaría el Python del sistema y fallaría con `ModuleNotFoundError`.

El orden es **01 → 03 → 04**: el 04 entrena sobre los paquetes de vistas que
genera el 03. El 02 es independiente y **requiere pantalla** (no corre headless).

### El notebook 04 usa un entorno aparte

`torch` y `gsplat` no están en `pyproject.toml` a propósito: dependen de la GPU y
del CUDA de la máquina, y un `uv sync` los podaría. Se instalan en su propio venv
con su kernel de Jupyter — instrucciones en la §0 del propio notebook.

Validado en **RTX 5070 (sm_120)** con `torch 2.11.0+cu128` y `gsplat 1.5.3`.

## Estructura

```
notebooks/              los cuatro experimentos, con sus figuras embebidas
packages/core-schemas/  contrato de datos (Pydantic) al que serializan 01 y 04
scripts/                fetch_teeth3ds.sh — descarga reproducible del dataset
docs/research/          nota del dataset Teeth3DS+
data/                   gitignored: raw/ es el dataset, processed/ los artefactos
```

`data/` no se versiona: pesa varios GB, es **regenerable** (script + notebooks) y
el dataset no debe redistribuirse por el repo. El repo guarda la receta, no el dato.

## Dataset

[Teeth3DS+](https://github.com/abenhamadou/3DTeethSeg_MICCAI_Challenges) (MICCAI
3DTeethSeg'22) — 300 pacientes / 600 escaneos. Licencia **CC-BY 4.0**
(Ben-Hamadou et al., 2022): atribuir en cualquier derivado. Ver
[`docs/research/dataset-teeth3ds.md`](docs/research/dataset-teeth3ds.md).
