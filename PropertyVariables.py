from pydantic import BaseModel

class PropertyPrice(BaseModel):
    Property_Type: float
    Club_House: int
    School_University_In_Township: int
    Hospital_In_Township: int
    Mall_In_Township: int
    Park_Jogging_Track: int
    Swimming_Pool: int
    Gym: int
    Property_Area_in_SqFt: float
    Price_By_SubArea: float
    Amenities_Score: int
    Price_By_Amenities_Score: float
    Noun_Counts: int
    Verb_Counts: int
    Adjective_Counts: int
    boasts_elegant: int
    elegant_towers: int
    every_day: int
    great_community: int
    mantra_gold: int
    offering_bedroom: int
    quality_specification: int
    stories_offering: int
    towers_stories: int
    world_class: int    