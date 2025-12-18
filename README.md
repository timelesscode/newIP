# newIP
# Beat 'Em Up RPG - MVP Game Design Document

## 1. Game Overview

### High Concept
A 2D side-scrolling beat 'em up with deep RPG progression, elemental combat system, and open-world exploration inspired by Streets of Rage, River City Ransom, and Metroidvania design.

### Target Platform
- PC (with controller support)
- Engine: Godot 4 / Unreal Engine 4

### Core Pillars
1. **Progressive Combat** - Techniques evolve through use
2. **Exploration** - Interconnected world with secrets
3. **Build Variety** - Mix and match techniques and elements
4. **Player Freedom** - Non-linear progression

---

## 2. Core Gameplay Systems

### 2.1 Combat System

#### Basic Mechanics
- **Movement**: Left/Right movement, Jump, Dash/Roll
- **Attack Types**: 
  - Light Attack (Jab) - Fast, low damage
  - Heavy Attack - Slow, high damage
  - Special Techniques - Purchased/learned abilities
  - Grab/Throw - Context-sensitive grappling

#### Combo System
- String attacks together for combo multipliers
- Different techniques can chain into each other
- Combo counter increases damage and XP gain
- Breaking combos resets multiplier

#### Hit Feedback
- Hit stop/freeze frames
- Screen shake on heavy hits
- Damage numbers pop up
- Knockback and juggling mechanics

### 2.2 Progression System

#### Technique Leveling
- Each technique has individual XP
- XP gained by hitting enemies with that technique
- Levels 1-10 for MVP
- Level milestones unlock:
  - **Level 3**: Increased damage
  - **Level 5**: Reduced stamina cost, elemental infusion slot unlocked
  - **Level 7**: Increased combo potential
  - **Level 10**: Ultimate variant unlocked

#### Character Stats
- **HP** - Health points
- **Stamina** - Resource for special techniques
- **Strength** - Physical damage multiplier
- **Agility** - Movement speed, dash distance
- **Spirit** - Elemental damage multiplier, stamina regeneration
- **Defense** - Damage reduction

Stats increase through:
- Character level-ups (1 point per level)
- Equipment
- Consumables (permanent stat books)

#### Character Leveling
- Global character XP from defeating enemies
- Level 1-20 for MVP
- Each level: +1 stat point, +5% HP/Stamina

### 2.3 Elemental System

#### Core Elements (MVP)
1. **Fire** - Damage over time, breaks ice
2. **Ice** - Slows enemies, freezes water
3. **Lightning** - Chain damage, stuns

#### Element Progression
- Elements level independently (1-10)
- Gained through:
  - Using elemental techniques
  - Consuming elemental crystals
  - Training at elemental dojos

#### Elemental Infusion
- At technique level 5+, can infuse with element
- Infusion adds element damage scaling
- Creates status effects (burn, freeze, shock)
- Visual effects change based on element

#### Elemental Reactions
- Fire + Ice = Steam explosion (AoE damage)
- Ice + Lightning = Frozen shock (massive stun)
- Fire + Lightning = Plasma (highest damage combo)

---

## 3. World Design

### 3.1 World Structure

#### Map Layout (MVP)
```
[Starting Town] - Tutorial & First Dojo
    |
[Harbor District] - Water enemies, Ice Dojo
    |
[Industrial Zone] - Fire hazards, Fire Dojo  
    |
[Downtown] - Mixed enemies, Advanced Dojos
    |
[Mountain Path] - Lightning Dojo
    |
[Hidden Valley] - Secret techniques, Master Sensei
```

#### Town/City Features
- **Safe Zones**: No combat, can rest/save
- **Shops**: 
  - Item Shop (potions, crystals, stat books)
  - Weapon Shop (equippable weapons)
  - Dojo (technique purchases/training)
- **NPCs**: Quest givers, lore, hints
- **Save Points**: Benches, shrines

#### Combat Zones
- Street sections with waves of enemies
- Mini-boss encounters
- Environmental hazards (fire, spikes, pits)
- Breakable objects (barrels, crates) for items

### 3.2 Fast Travel System

#### Airship Terminals
- Unlocked after completing first major area
- Present in larger cities
- Select destination from map
- Costs small amount of currency

#### Discovery System
- Must visit location once before fast travel
- Terminals marked on map once discovered
- Secret locations have hidden terminals

---

## 4. Techniques System

### 4.1 Starting Techniques
- **Jab** (Light Attack) - Quick punch, 3-hit combo
- **Dash** - Quick movement ability

### 4.2 Purchasable Techniques (MVP Sample)

#### Basic Tier (500-1000g)
- **Rising Uppercut** - Anti-air launcher
- **Leg Sweep** - Low attack, trips enemies
- **Power Punch** - Charged heavy attack
- **Rolling Kick** - Dash attack

#### Intermediate Tier (2000-3000g)
- **Hurricane Kick** - Multi-hit spinning attack
- **Ground Slam** - AoE attack from air
- **Counter Strike** - Parry and counter
- **Chi Blast** - Ranged projectile

#### Advanced Tier (5000g+)
- **Dragon Fist** - Forward rushing combo finisher
- **Phoenix Dive** - Aerial dive attack with explosion
- **Shadow Step** - Teleport dodge with follow-up
- **Meteor Drop** - Grab and slam special

### 4.3 Secret Techniques
- Found in hidden scrolls
- Taught by secret senseis
- Require specific stat thresholds
- Ultra-rare, one per playthrough (MVP: 3 total)

---

## 5. Enemy Design

### 5.1 Enemy Types (MVP)

#### Basic Enemies
- **Thug** - Melee, basic punches
- **Knife Fighter** - Fast attacks, low HP
- **Brute** - Heavy hits, grabs, high HP
- **Gunner** - Ranged attacks, retreats

#### Element-Aligned Enemies
- **Flame Enforcer** - Fire damage, resistant to fire
- **Frost Guard** - Ice attacks, slow movement
- **Shock Trooper** - Lightning attacks, teleports

#### Mini-Bosses
- Tougher enemy variants
- Unique techniques
- Guard key areas/dojos

### 5.2 Enemy AI States
- **Idle** - Standing, looking for player
- **Approach** - Moving toward player
- **Attack** - Executing attack pattern
- **Block** - Defensive stance
- **Retreat** - Low HP escape behavior
- **Stagger** - Hit reaction state

---

## 6. MVP Feature Set

### Core Features (Must Have)
- [x] 2D side-scrolling movement (8-direction)
- [x] Basic combat (jab, heavy, grab)
- [x] 3 starting areas with combat zones
- [x] 1 town hub with shops and dojo
- [x] Technique leveling system (1-10)
- [x] 3 elements with infusion system
- [x] 5 purchasable techniques
- [x] Character stats and leveling (1-20)
- [x] 4 basic enemy types
- [x] 2 mini-bosses
- [x] Save/load system
- [x] Inventory system (20 slots)
- [x] Equipment system (weapon, armor)
- [x] World map with 5 locations

### Secondary Features (Should Have)
- [ ] 1 secret technique scroll
- [ ] Fast travel (airship terminal)
- [ ] Elemental reactions
- [ ] Quest system (3 side quests)
- [ ] Combo counter UI
- [ ] Tutorial section
- [ ] Sound effects and music
- [ ] Controller support

### Polish Features (Nice to Have)
- [ ] Particle effects for elements
- [ ] Animated backgrounds
- [ ] NPC dialogue system
- [ ] Achievement system
- [ ] Multiple character skins
- [ ] New Game+ mode

---

## 7. Technical Specifications

### 7.1 Godot 4 Implementation

#### Scene Structure
```
Main.tscn (Game Manager)
├── WorldMap.tscn (Global map container)
│   ├── TownHub.tscn
│   ├── HarborDistrict.tscn
│   └── IndustrialZone.tscn
├── Player.tscn (CharacterBody2D)
├── UI.tscn (CanvasLayer)
└── Systems/
    ├── CombatSystem.gd
    ├── ProgressionSystem.gd
    ├── InventorySystem.gd
    └── SaveSystem.gd
```

#### Key Scripts
- **Player.gd** - Movement, input handling, state machine
- **TechniqueBase.gd** - Base class for all techniques
- **EnemyBase.gd** - Enemy AI base class
- **ElementalSystem.gd** - Element calculations and effects
- **ProgressionManager.gd** - XP, levels, stats

#### Asset Organization
```
res://
├── scenes/
├── scripts/
├── assets/
│   ├── sprites/
│   ├── animations/
│   ├── audio/
│   └── ui/
├── data/
│   ├── techniques/
│   ├── enemies/
│   └── items/
└── saves/
```

### 7.2 UE4 Implementation

#### Blueprint Structure
- **BP_PlayerCharacter** (Character class)
- **BP_GameMode** (Game mode with systems)
- **BP_EnemyBase** (Enemy AI parent class)
- **BP_TechniqueComponent** (Actor component)
- **BP_ProgressionComponent** (Actor component)

#### C++ Classes (Optional)
- `ATechniqueSystem` - Core combat calculations
- `UProgressionComponent` - Character stats and leveling
- `AElementalEffect` - Elemental damage/effects actor
- `UCombatComponent` - Reusable combat component

#### Asset Organization
```
Content/
├── Blueprints/
│   ├── Player/
│   ├── Enemies/
│   ├── Systems/
│   └── UI/
├── Maps/
├── Characters/
├── Effects/
├── Audio/
└── Data/
    └── DataTables/
```

---

## 8. Data Structures

### Technique Data
```json
{
  "id": "hurricane_kick",
  "name": "Hurricane Kick",
  "description": "Spinning multi-hit attack",
  "base_damage": 15,
  "stamina_cost": 20,
  "hits": 5,
  "price": 2500,
  "unlock_level": 1,
  "element_slot": true,
  "animation": "hurricane_kick_anim"
}
```

### Character Stats
```json
{
  "level": 10,
  "xp": 5420,
  "xp_to_next": 1000,
  "hp": 150,
  "max_hp": 150,
  "stamina": 100,
  "max_stamina": 100,
  "strength": 12,
  "agility": 8,
  "spirit": 10,
  "defense": 7,
  "stat_points": 2
}
```

### Element Data
```json
{
  "fire": {
    "level": 5,
    "xp": 450,
    "damage_bonus": 1.25,
    "status": "burn",
    "status_duration": 3.0,
    "status_damage": 5
  }
}
```

---

## 9. UI/UX Design

### HUD Elements
- **Top Left**: HP bar, Stamina bar, Character level
- **Top Right**: Combo counter, XP bar
- **Bottom**: Active technique slots (4 hotkeys)

### Menu Screens
1. **Main Menu** - New Game, Continue, Options, Exit
2. **Pause Menu** - Resume, Character, Inventory, Map, Options, Quit
3. **Character Screen** - Stats, Techniques, Elements, Equipment
4. **Inventory** - Items grid, Use/Drop buttons
5. **Shop** - Buy/Sell interface with item descriptions
6. **Dojo** - Technique list with purchase/training options
7. **Map** - World map with discovered locations

---

## 10. Audio Design

### Sound Effects (MVP)
- Hit impacts (light, heavy, critical)
- Technique activation sounds
- Elemental effect sounds (fire, ice, lightning)
- Enemy sounds (hit, death, attack)
- UI sounds (menu navigate, button press)
- Ambient sounds (wind, fire crackle, city noise)

### Music (MVP)
- Town theme (calm, safe)
- Combat theme (upbeat, energetic)
- Boss theme (intense, dramatic)
- Victory theme (short, triumphant)

---

## 11. Development Roadmap

### Phase 1: Core Systems (Weeks 1-3)
- Player movement and controls
- Basic combat system (jab, heavy attack)
- Enemy AI basics
- Collision and hit detection

### Phase 2: Progression (Weeks 4-5)
- Technique leveling system
- Character stats and leveling
- XP and damage calculations
- Save/load system

### Phase 3: World Building (Weeks 6-7)
- 3 combat areas
- 1 town hub
- Shop and dojo functionality
- World map navigation

### Phase 4: Combat Depth (Weeks 8-9)
- 5 purchasable techniques
- Elemental system implementation
- Element infusion mechanics
- 4 enemy types + 2 mini-bosses

### Phase 5: Polish (Weeks 10-12)
- UI implementation
- Sound effects and music
- Balance testing
- Bug fixing
- Tutorial section

---

## 12. Design Principles

### Combat Feel
- Every hit should feel impactful
- Clear audio and visual feedback
- Responsive controls (< 100ms input lag)
- Fair difficulty curve

### Progression Satisfaction
- Regular rewards and unlocks
- Multiple paths to power
- Visible growth in abilities
- Experimentation encouraged

### Exploration Rewards
- Secrets worth finding
- Shortcuts that feel earned
- Environmental storytelling
- No dead ends

### Player Freedom
- Multiple viable builds
- Non-linear progression where possible
- Optional challenges
- Flexible playstyles

---

## 13. Success Metrics (MVP)

### Core Loop Engagement
- Average session length: 30-60 minutes
- Technique diversity: Players use 4+ techniques regularly
- Completion rate: 60%+ of players finish MVP content

### System Validation
- Combat satisfaction: 7/10+ player rating
- Progression clarity: Players understand technique leveling
- Build variety: At least 3 distinct viable builds

### Technical Goals
- Stable 60 FPS on target hardware
- Load times < 3 seconds between areas
- No game-breaking bugs in main path

---

## 14. Future Expansion (Post-MVP)

### Additional Content
- 3 more playable characters
- 10+ new techniques per character
- 2 more elements (Earth, Wind)
- Full story campaign (10+ hours)
- Multiplayer co-op
- PvP arena mode

### Systems Expansion
- Crafting system
- Tech fusion (combine techniques)
- Prestige/New Game+ with bonuses
- Challenge modes
- Leaderboards

---

## Appendix A: Controls Layout

### Keyboard (Default)
- **Arrow Keys** - Movement
- **Z** - Light Attack
- **X** - Heavy Attack
- **C** - Special Technique 1
- **V** - Special Technique 2
- **Space** - Jump
- **Shift** - Dash/Roll
- **A/S** - Grab/Throw
- **ESC** - Pause Menu
- **Tab** - Character Menu

### Controller (Xbox Layout)
- **Left Stick** - Movement
- **A** - Jump
- **X** - Light Attack
- **Y** - Heavy Attack
- **B** - Dash/Roll
- **RB/RT** - Special Techniques
- **LB/LT** - Grab/Throw
- **Start** - Pause Menu
- **Select** - Character Menu

---

## Appendix B: Balancing Guidelines

### Damage Scaling
- Base damage at level 1: 10
- Level 10: 25 (+150%)
- Elemental bonus: +20-50% based on element level
- Critical hits: 1.5x damage (10% base chance)

### Enemy HP Scaling
- Basic enemy: 50 HP
- Tough enemy: 100 HP
- Mini-boss: 300 HP
- Scale by area: +20% HP per area

### Economy
- Starting gold: 500
- Enemy drops: 10-50g
- Basic technique: 500-1000g
- Advanced technique: 5000g+
- Item costs: 50-500g

---

*This GDD is a living document and will be updated as development progresses.*
