from dataclasses import dataclass, field


@dataclass
class Competency:
    name: str
    level: int


@dataclass
class CompetencyGroup:
    name: str
    competencies: dict[str, int] = field(default_factory=dict)
    competency_sources: dict[str, str] = field(default_factory=dict)

    def __add__(self, other: CompetencyGroup | Competency) -> CompetencyGroup:
        if isinstance(other, Competency):
            return self.add_competency(other)
        if not isinstance(other, CompetencyGroup):
            return NotImplemented

        new_competencies = self.competencies.copy()
        new_sources = self.competency_sources.copy()

        for competency, level in other.competencies.items():
            if competency in new_competencies:
                if level > new_competencies[competency]:
                    new_competencies[competency] = level
                    if competency in other.competency_sources:
                        new_sources[competency] = other.competency_sources[competency]
            else:
                new_competencies[competency] = level
                if competency in other.competency_sources:
                    new_sources[competency] = other.competency_sources[competency]

        return CompetencyGroup(
            name=f"{self.name} + {other.name}",
            competencies=new_competencies,
            competency_sources=new_sources,
        )

    def __iadd__(self, other: CompetencyGroup | Competency) -> CompetencyGroup:
        if isinstance(other, Competency):
            return self.iadd_competency(other)
        if not isinstance(other, CompetencyGroup):
            return NotImplemented

        for competency, level in other.competencies.items():
            if competency in self.competencies:
                if level > self.competencies[competency]:
                    self.competencies[competency] = level
                    if competency in other.competency_sources:
                        self.competency_sources[competency] = other.competency_sources[
                            competency
                        ]
            else:
                self.competencies[competency] = level
                if competency in other.competency_sources:
                    self.competency_sources[competency] = other.competency_sources[
                        competency
                    ]

        return self

    def __sub__(self, other: CompetencyGroup) -> CompetencyGroup:
        new_competencies = self.competencies.copy()
        new_sources = self.competency_sources.copy()

        for competency, level in other.competencies.items():
            if level >= new_competencies.get(competency, 0):
                new_competencies.pop(competency, None)
                new_sources.pop(competency, None)

        return CompetencyGroup(
            name=f"{self.name} - {other.name}",
            competencies=new_competencies,
            competency_sources=new_sources,
        )

    def __isub__(self, other: CompetencyGroup) -> CompetencyGroup:
        for competency, level in other.competencies.items():
            if level >= self.competencies.get(competency, 0):
                self.competencies.pop(competency, None)
                self.competency_sources.pop(competency, None)

        return self

    def add_competency(self, other: Competency) -> CompetencyGroup:
        new_competencies = self.competencies.copy()
        new_sources = self.competency_sources.copy()

        if other.name in new_competencies:
            if other.level > new_competencies[other.name]:
                new_competencies[other.name] = other.level
                new_sources[other.name] = self.name
        else:
            new_competencies[other.name] = other.level
            new_sources[other.name] = self.name

        return CompetencyGroup(
            name=self.name,
            competencies=new_competencies,
            competency_sources=new_sources,
        )

    def iadd_competency(self, other: Competency) -> CompetencyGroup:
        if other.name in self.competencies:
            if other.level > self.competencies[other.name]:
                self.competencies[other.name] = other.level
                self.competency_sources[other.name] = self.name
        else:
            self.competencies[other.name] = other.level
            self.competency_sources[other.name] = self.name

        return self
