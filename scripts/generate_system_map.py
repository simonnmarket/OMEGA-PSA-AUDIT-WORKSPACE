#!/usr/bin/env python3
"""
SCRIPT: generate_system_map.py
Objetivo: Produzir SYSTEM_MAP.md a partir de tree.txt do OMEGA_OS_Kernel.
Metodologia: FASE 1 — Cartografia Institucional (COUNCIL-DIRECTIVE-028).
Restrição: somente leitura; nenhuma interpretação de código-fonte.
"""

from pathlib import Path
from collections import defaultdict

TREE_PATH = Path(r"C:\Users\Lenovo\Desktop\OMEGA_OS_Kernel\tree.txt")
OUTPUT_PATH = Path(r"C:\OMEGA-PSA-AUDIT-WORKSPACE\SYSTEM_MAP.md")

EXCLUDED_DIRS = {"__pycache__", ".git"}


def parse_tree(path: Path):
    directories = []
    files = []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Skip first 3 lines (empty + headers)
    for line in lines[3:]:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        # The line format is: <FullName> <Length>
        # Length is optional; if present, it's a number at the end.
        parts = line.rsplit(" ", 1)
        if len(parts) == 2 and parts[1].strip().isdigit():
            full_name = parts[0].strip()
            length = int(parts[1].strip())
            files.append((full_name, length))
        else:
            full_name = line.strip()
            # Ignore if it looks like part of the header
            if full_name in ("FullName", "--------"):
                continue
            directories.append(full_name)

    return directories, files


def build_tree(directories, files):
    root = {"children": {}, "files": 0, "size": 0, "dirs": 0}

    for d in directories:
        parts = Path(d).parts
        if any(part in EXCLUDED_DIRS for part in parts):
            continue
        # Skip prefix until OMEGA_OS_Kernel
        try:
            idx = parts.index("OMEGA_OS_Kernel")
            parts = parts[idx + 1:]
        except ValueError:
            continue
        if not parts:
            continue
        node = root
        for part in parts:
            if part not in node["children"]:
                node["children"][part] = {"children": {}, "files": 0, "size": 0, "dirs": 0}
            node = node["children"][part]
        node["dirs"] += 1

    for f, size in files:
        parts = Path(f).parts
        if any(part in EXCLUDED_DIRS for part in parts):
            continue
        try:
            idx = parts.index("OMEGA_OS_Kernel")
            parts = parts[idx + 1:]
        except ValueError:
            continue
        if not parts:
            continue
        node = root
        for part in parts[:-1]:
            if part not in node["children"]:
                node["children"][part] = {"children": {}, "files": 0, "size": 0, "dirs": 0}
            node = node["children"][part]
        node["files"] += 1
        node["size"] += size

    return root


def aggregate(node):
    for child in node["children"].values():
        aggregate(child)
        node["files"] += child["files"]
        node["size"] += child["size"]
        node["dirs"] += child["dirs"]


def render_tree(name, node, prefix="", is_last=True, output_lines=None):
    if output_lines is None:
        output_lines = []
    connector = "└── " if is_last else "├── "
    count = f" [{node['files']} arquivos, {node['dirs']} dirs, {node['size'] / 1024:.1f} KB]"
    output_lines.append(f"{prefix}{connector}{name}{count}")
    children = list(node["children"].items())
    for i, (child_name, child) in enumerate(children):
        last = i == len(children) - 1
        new_prefix = prefix + ("    " if is_last else "│   ")
        render_tree(child_name, child, new_prefix, last, output_lines)
    return output_lines


def classify_top_level(name, files, dirs):
    # Heuristic classification based on name and contents
    lower = name.lower()
    if lower in {"core", "core_engines", "modules", "src", "engines", "entities"}:
        return "Domínio Técnico — Core/Engines"
    if lower in {"agents", "omega_intelligence_os", "omega_os_kernel", "omega_v6_code", "genesis"}:
        return "Domínio Técnico — Agentes/Inteligência"
    if lower in {"audit", "results", "paper", "shadow", "ohlcv_data", "fin_sense_data"}:
        return "Domínio de Dados/Evidências"
    if lower in {"tests", "scripts", "runner", "run"} or lower.startswith("run_") or "runner" in lower:
        return "Domínio de Execução/Testes"
    if lower in {"config", "governance", "docs", "documentation", "institutional analysis", "nasa_validation", "official_audit", "honest_audit", "forensic"}:
        return "Domínio de Configuração/Governança/Audit"
    if lower in {"telemetry", "logs", "smoke_test"} or "telemetry" in lower or "log" in lower:
        return "Domínio de Telemetria/Monitoramento"
    if lower in {"inativo", "verificar", "obsolete", "concepts 020625"}:
        return "Domínio de Arquivamento/Análise"
    if lower == "main.py":
        return "Entrypoint Principal"
    if name.endswith(".py"):
        return "Script de Orquestração/Utilitário"
    if name.endswith(".md"):
        return "Documentação"
    if name.endswith(".json"):
        return "Configuração/Dados"
    if name.endswith(".log"):
        return "Log"
    if name.endswith(".txt"):
        return "Texto/Configuração"
    return "Domínio em Classificação"


def main():
    directories, files = parse_tree(TREE_PATH)
    root = build_tree(directories, files)
    aggregate(root)

    total_dirs = len(directories)
    total_files = len(files)
    total_size = sum(size for _, size in files)

    top_level = []
    root_path = Path(r"C:\Users\Lenovo\Desktop\OMEGA_OS_Kernel")
    for name, child in root["children"].items():
        top_level.append({
            "name": name,
            "files": child["files"],
            "dirs": child["dirs"],
            "size": child["size"],
            "classification": classify_top_level(name, child["files"], child["dirs"]),
        })

    # Sort by size descending
    top_level.sort(key=lambda x: x["size"], reverse=True)

    lines = []
    lines.append("# SYSTEM_MAP.md")
    lines.append("")
    lines.append("## Cartografia Institucional do OMEGA_OS_Kernel")
    lines.append("")
    lines.append("**ID:** SYSTEM_MAP  ")
    lines.append("**Fase:** FASE 1 — Cartografia Institucional (COUNCIL-DIRECTIVE-028)  ")
    lines.append("**Data:** 2026-06-27  ")
    lines.append("**Fonte:** `tree.txt` do OMEGA_OS_Kernel  ")
    lines.append("**Modo:** somente leitura; nenhum código interpretado  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Resumo Estrutural")
    lines.append("")
    lines.append(f"- **Localização:** `C:\\Users\\Lenovo\\Desktop\\OMEGA_OS_Kernel`")
    lines.append(f"- **Total de diretórios:** {total_dirs}")
    lines.append(f"- **Total de arquivos:** {total_files}")
    lines.append(f"- **Tamanho total:** {total_size / 1024 / 1024:.2f} MB")
    lines.append(f"- **Arquivo de origem:** `tree.txt` ({TREE_PATH.stat().st_size / 1024:.1f} KB)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Domínios de Alto Nível")
    lines.append("")
    lines.append("| Domínio | Classificação | Arquivos | Diretórios | Tamanho (KB) |")
    lines.append("|---------|--------------|----------|------------|--------------|")
    for item in top_level:
        lines.append(
            f"| {item['name']} | {item['classification']} | {item['files']} | {item['dirs']} | {item['size'] / 1024:.1f} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Mapa Hierárquico de Diretórios")
    lines.append("")
    lines.append("```")
    tree_lines = render_tree("OMEGA_OS_Kernel", root)
    lines.extend(tree_lines)
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. Notas Metodológicas")
    lines.append("")
    lines.append("- Este mapa foi produzido exclusivamente a partir da estrutura física de diretórios e arquivos.")
    lines.append("- Nenhum código-fonte foi lido ou interpretado nesta fase.")
    lines.append("- A classificação dos domínios é heurística e será refinada nas FASES 2-4.")
    lines.append("- Arquivos de cache (`__pycache__`) e controle de versão (`.git`) foram excluídos da contagem.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 5. Evidências de Origem")
    lines.append("")
    lines.append(f"- `tree.txt` extraído de `C:\\Users\\Lenovo\\Desktop\\OMEGA_OS_Kernel\\tree.txt`")
    lines.append(f"- Total de linhas processadas: {len(directories) + len(files) + 3}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**Principal Solution Architect PSA**  ")
    lines.append("**2026-06-27**")
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"SYSTEM_MAP.md gerado em: {OUTPUT_PATH}")
    print(f"Diretórios: {total_dirs}, Arquivos: {total_files}, Tamanho: {total_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    main()
