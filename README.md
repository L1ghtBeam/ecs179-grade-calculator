# ecs179 Grade Calculator

Run or build with [uv](https://docs.astral.sh/uv/).

```
uv run grade-calc -h
```

Use with TOML files of this format:
```toml
#example.toml

[[groups]]
# use for a specific exercise or task done
name = "<Group Name>"

[groups.competencies]
# all competencies for this group go here
engine_usage = "locked"
design_patterns = "unlocked"
debugging = "developed"
code_standards = "mastered"

# next group continues here
# [[groups]]
# ...
```

Valid competency keys:
- `engine_usage`
- `design_patterns`
- `debugging`
- `code_standards`
- `versioning`
- `game_systems`
- `system_interrelations`
- `game_design_reasoning`
- `design_context`
- `interaction_design`
- `interaction_loops`
- `evaluation`

# Specifications (excerpt from syllabus)

## Competency Levels

| Competency State | Meaning |
|---|---|
| **Locked** | I do not yet have enough evidence to verify this competency. |
| **Unlocked** | You can complete a guided application and explain its basic operation. |
| **Developed** | You can apply the competency to a changed problem and diagnose ordinary difficulties. |
| **Mastered** | You can apply the competency independently, evaluate the result, and justify your decisions. |

## Assessed Competencies

### Software Engineering

| Competency | What it means in this course | Concepts |
|---|---|---|
| **Engine Usage** | Use Godot's architecture and services appropriately when implementing gameplay. | Game engines, libraries, tools, wizards |
| **Design Patterns** | Implement, adapt, and evaluate recurring software structures used in games. | Command, Publish-Subscribe, Observer, Factories |
| **Debugging and Testing** | Investigate failures systematically and establish repeatable evidence about behavior. | Logging, exposure, unit tests |
| **Code Standards and Review** | Write understandable code and give or use technically specific review feedback. | Style guide, review, analysis |
| **Versioning and Team Development** | Use Git and an explicit team process to coordinate reliable development. | Git, communication, Agile methodology |

### Design

| Competency | What it means in this course | Concepts |
|---|---|---|
| **Game Systems** | Implement rules, state, relationships, and processes that create gameplay. | Game systems |
| **System Interrelations** | Reason about dependencies and consequences when gameplay systems interact. | System interactions, genres |
| **Game Design Reasoning** | Use design theory to explain or revise an implementation. | Game design theory, MDA |
| **Design Context** | Place implementation decisions in historical, platform, genre, and human contexts. | Game history, design frames, platform studies and adaptation, human-centered interactions |

### User Experience

| Competency | What it means in this course | Concepts |
|---|---|---|
| **Interaction Design** | Create legible and responsive interactions through controls, timing, visual information, and feedback. | Juice, graphic design |
| **Interaction Loops** | Implement and reason about repeated cycles of player action and system response. | Core loops, loop interaction |
| **Evaluation and Iteration** | Observe play, identify an interaction problem, and revise the game in response. | Evaluation |

## Course Grade

| Profile grade | Minimum competency profile |
|---|---|
| A | All 12 competencies Developed or higher, including at least 4 Mastered |
| A- | At least 10 Developed or higher, including at least 3 Mastered |
| B+ | At least 9 Developed or higher, including at least 2 Mastered |
| B | At least 8 Developed or higher, including at least 1 Mastered |
| B- | At least 7 Developed or higher |
| C+ | At least 5 Developed or higher |
| C | At least 4 Developed or higher |
| C- | At least 2 Developed or higher |
| D+ | At least 1 Developed or higher |
| D | At least 4 Unlocked or higher |
| D- | At least 1 Unlocked or higher |
| F | No verified competencies |

You receive the highest profile grade for which you've met all the requirements. Mastered competencies also count toward the Developed and Unlocked requirements, and Developed competencies count toward Unlocked.
