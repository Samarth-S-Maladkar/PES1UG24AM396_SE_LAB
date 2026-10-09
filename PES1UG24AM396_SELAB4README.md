# Lab 4: VibeCoding (Pac-Man Repair Lab)

**Name:** Samarth S. Maladkar
**Project:** 34_pacman (Pac-Man in Pygame)

## Links

- **Forked repository:** https://github.com/Samarth-S-Maladkar/34_pacman
- **Original (assigned) repository:** https://github.com/SETAPESU26/34_pacman
- **Chat history (Claude):** https://claude.ai/share/57f39e20-8d2a-4be0-9eec-e6419f3da54e

## Folder Contents

```
Lab-4/
├── game.py              # Updated code
├── before.mp4           # 10 s gameplay before changes (bug visible)
├── after.mp4            # 10 s gameplay after all changes
├── chat_history.pdf     # Exported chat history
└── README.md
```

## Tasks Completed

Each task was done with a separate commit.

| # | Task | Summary |
|---|------|---------|
| 1 | Fix power pellet bug | `eat()` compared against the wrong character, so frightened mode never triggered. Fixed to match the maze's power pellet character. |
| 2 | Implement `ghost_color(name, mode)` | Each ghost now has a distinct frightened-mode tint. Other modes return `None` to keep defaults. |
| 3 | Implement `on_pellet_eaten(score, pellets_left)` | [Describe your feature, e.g. HUD flash on last pellet / bonus fruit] |
| 4 | Implement `bonus_life_threshold()` | Returns [your value] so the player earns an extra life at each multiple of that score. |

## How to Run

```bash
pip install pygame
python game.py
```

**Controls:** Arrow keys to move, `R` to reset.

## Submission Checklist

- [x] 10-second video before changes
- [x] 10-second video after changes
- [x] Updated code
- [x] Chat history (PDF and link)
- [x] Separate commits per task
- [x] No PR raised to SETAPESU26
