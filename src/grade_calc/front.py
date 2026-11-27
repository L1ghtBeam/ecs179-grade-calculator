class Competency:
    key_map: dict[str, Competency] = {}
    max_name_length: int = 0

    def __new__(cls, key: str, name: str):
        instance = super().__new__(cls)

        cls.key_map[key] = instance
        cls.max_name_length = max(cls.max_name_length, len(name))

        return instance

    def __init__(self, key: str, name: str):
        self.key = key
        self.name = name

    def __repr__(self):
        return f"Competency(key={self.key}, name={self.name})"

    @classmethod
    def exists(cls, key: str) -> bool:
        return key in cls.key_map

    @classmethod
    def get_name(cls, key: str) -> str:
        return cls.key_map[key].name

    @classmethod
    def get_max_name_length(cls) -> int:
        return cls.max_name_length


for competency in [
    ("engine_usage", "Engine Usage"),
    ("design_patterns", "Design Patterns"),
    ("debugging", "Debugging and Testing"),
    ("code_standards", "Code Standards and Review"),
    ("versioning", "Versioning and Team Development"),
    ("game_systems", "Game Systems"),
    ("system_interrelations", "System Interrelations"),
    ("game_design_reasoning", "Game Design Reasoning"),
    ("design_context", "Design Context"),
    ("interaction_design", "Interaction Design"),
    ("interaction_loops", "Interaction Loops"),
    ("evaluation", "Evaluation and Iteration"),
]:
    Competency(*competency)


class CompetencyLevels:
    key_map: dict[str, CompetencyLevels] = {}
    level_map: dict[int, CompetencyLevels] = {}
    max_name_length: int = 0

    def __new__(cls, key: str, level: int):
        instance = super().__new__(cls)

        cls.key_map[key] = instance
        cls.level_map[level] = instance
        cls.max_name_length = max(cls.max_name_length, len(key))

        return instance

    def __init__(self, key: str, level: int):
        self.key = key
        self.level = level

    def __repr__(self):
        return f"CompetencyLevels(key={self.key}, level={self.level})"

    @staticmethod
    def get_name(key: str) -> str:
        return key.capitalize()

    @classmethod
    def exists(cls, key: str) -> bool:
        return key in cls.key_map

    @classmethod
    def get_level(cls, key: str) -> int:
        return cls.key_map[key].level

    @classmethod
    def get_key_from_level(cls, level: int) -> str:
        return cls.level_map[level].key

    @classmethod
    def get_name_from_level(cls, level: int) -> str:
        return cls.get_name(cls.get_key_from_level(level))

    @classmethod
    def get_max_name_length(cls) -> int:
        return cls.max_name_length


for i, level in enumerate(["locked", "unlocked", "developed", "mastered"]):
    CompetencyLevels(level, i)
