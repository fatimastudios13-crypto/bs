# Reusable Intelligence Modules (RIM)

A personal engineering OS for turning ideas into structured research, design, implementation, and durable knowledge.

## Core pipeline

`Idea → Expand → Research → Product Design → Feature Plan → Project Plan → Code → GitHub → Documentation → Release → Notion`

## Module contract

Every module has:

- `name`
- `subname`
- `description`
- `inputs`
- `use_case`
- `default`
- `result`
- `revolt` (kept for compatibility with the original Notion schema)
- `version`
- `type`
- `status`

## Design principles

1. Notion is the system of record for ideas, decisions, research, specs, and release records.
2. GitHub is the executable/versioned artifact layer.
3. Product Design is the research/design/prototyping layer.
4. Modules should be composable and versioned.
5. Unknowns must remain explicit instead of being silently invented.
6. A result is not complete until it has a validation step appropriate to its type.

## Initial modules

- idea-capture
- idea-expand
- idea-research
- product-design
- feature-planner
- project-planner
- code-generator
- github-project
- notion-writer
- documentation
- bug-fixer
- release-manager

## Status

Foundation implementation. Next steps are a CLI/runtime, schema validation, module registry, and Notion synchronization.
