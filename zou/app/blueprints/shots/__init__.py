from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from .resources import (
    ShotResource,
    ShotsResource,
    ShotsAndTasksResource,
    ShotAssetsResource,
    ShotTaskTypesResource,
    ShotTasksResource,

    SceneResource,
    SceneTasksResource,

    ProjectShotsResource,
    ProjectScenesResource,
    ProjectSequencesResource,
    ProjectEpisodesResource,

    EpisodeResource,
    EpisodesResource,
    EpisodeSequencesResource,

    SequenceResource,
    SequencesResource,
    SequenceShotsResource,
    SequenceScenesResource,
    SequenceTasksResource,
    SequenceTaskTypesResource,

    CastingResource
)


routes = [
    ("/data/shots/all", ShotsResource),
    ("/data/shots/with-tasks", ShotsAndTasksResource),
    ("/data/shots/<shot_id>", ShotResource),
    ("/data/shots/<shot_id>/assets", ShotAssetsResource),
    ("/data/shots/<shot_id>/task-types", ShotTaskTypesResource),
    ("/data/shots/<shot_id>/tasks", ShotTasksResource),
    ("/data/scenes/<scene_id>", SceneResource),
    ("/data/scenes/<scene_id>/tasks", SceneTasksResource),
    ("/data/episodes", EpisodesResource),
    ("/data/episodes/<episode_id>", EpisodeResource),
    ("/data/episodes/<episode_id>/sequences", EpisodeSequencesResource),
    ("/data/sequences", SequencesResource),
    ("/data/sequences/<sequence_id>", SequenceResource),
    ("/data/sequences/<sequence_id>/shots", SequenceShotsResource),
    ("/data/sequences/<sequence_id>/scenes", SequenceScenesResource),
    ("/data/sequences/<sequence_id>/tasks", SequenceTasksResource),
    ("/data/sequences/<sequence_id>/task-types", SequenceTaskTypesResource),
    ("/data/projects/<project_id>/shots", ProjectShotsResource),
    ("/data/projects/<project_id>/scenes", ProjectScenesResource),
    ("/data/projects/<project_id>/sequences", ProjectSequencesResource),
    ("/data/projects/<project_id>/episodes", ProjectEpisodesResource),

    ("/data/shots/<shot_id>/casting", CastingResource)
]


blueprint = Blueprint("shots", "shots")
api = configure_api_from_blueprint(blueprint, routes)
