import csv
import os
import shutil
from collections import defaultdict

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    dataset_path = "/home/alex/DATASETS/TODO/LISA Traffic Light/archive"
    anns_pathes = "/home/alex/DATASETS/TODO/LISA Traffic Light/archive/Annotations/Annotations"
    batch_size = 30

    ds_name_to_folders = {
        "train": ["dayTrain", "nightTrain"],
        "test": ["daySequence1", "daySequence2", "nightSequence1", "nightSequence1"],
    }


    def create_ann(image_path):
        labels = []

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = 960  # image_np.shape[0]
        img_wight = 1280  # image_np.shape[1]

        seq_vaue, frame_value = get_file_name(image_path).split("--")
        frame_tag = sly.Tag(track_meta, value=int(frame_value))
        if seq_vaue[:3] == "day":
            seq_vaue = seq_vaue[3:]
        else:
            seq_vaue = seq_vaue[5:]

        seq = sly.Tag(seq_meta, value=seq_vaue)

        ann_data = im_name_to_data_traff[get_file_name_with_ext(image_path)]
        for curr_ann_data in ann_data:
            obj_class = name_to_class_traff[curr_ann_data[0]]

            left = int(curr_ann_data[1])
            top = int(curr_ann_data[2])
            right = int(curr_ann_data[3])
            bottom = int(curr_ann_data[4])

            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class)
            labels.append(label)

        ann_data = im_name_to_data[get_file_name_with_ext(image_path)]
        for curr_ann_data in ann_data:
            obj_class = name_to_class[curr_ann_data[0]]

            left = int(curr_ann_data[1])
            top = int(curr_ann_data[2])
            right = int(curr_ann_data[3])
            bottom = int(curr_ann_data[4])

            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class)
            labels.append(label)

        return sly.Annotation(
            img_size=(img_height, img_wight), labels=labels, img_tags=[seq, time_tag, frame_tag]
        )


    go = sly.ObjClass("go", sly.Rectangle)
    stop = sly.ObjClass("stop", sly.Rectangle)
    stop_left = sly.ObjClass("stop left", sly.Rectangle)
    warning = sly.ObjClass("warning", sly.Rectangle)
    go_left = sly.ObjClass("go left", sly.Rectangle)
    warning_left = sly.ObjClass("warning left", sly.Rectangle)
    forward_left = sly.ObjClass("go forward", sly.Rectangle)

    name_to_class = {
        "go": go,
        "stop": stop,
        "stopLeft": stop_left,
        "warning": warning,
        "goLeft": go_left,
        "warningLeft": warning_left,
        "goForward": forward_left,
    }

    go_traff = sly.ObjClass("go traffic light", sly.Rectangle)
    stop_traff = sly.ObjClass("stop traffic light", sly.Rectangle)
    stop_left_traff = sly.ObjClass("stop left traffic light", sly.Rectangle)
    warning_traff = sly.ObjClass("warning traffic light", sly.Rectangle)
    go_left_traff = sly.ObjClass("go left traffic light", sly.Rectangle)
    warning_left_traff = sly.ObjClass("warning left traffic light", sly.Rectangle)
    forward_left_traff = sly.ObjClass("go forward traffic light", sly.Rectangle)

    name_to_class_traff = {
        "go": go_traff,
        "stop": stop_traff,
        "stopLeft": stop_left_traff,
        "warning": warning_traff,
        "goLeft": go_left_traff,
        "warningLeft": warning_left_traff,
        "goForward": forward_left_traff,
    }

    track_meta = sly.TagMeta("track frame number", sly.TagValueType.ANY_NUMBER)
    seq_meta = sly.TagMeta("sequence", sly.TagValueType.ANY_STRING)
    day_meta = sly.TagMeta("day", sly.TagValueType.NONE)
    night_meta = sly.TagMeta("night", sly.TagValueType.NONE)

    all_classes = list(name_to_class.values()) + list(name_to_class_traff.values())


    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=all_classes,
        tag_metas=[track_meta, seq_meta, day_meta, night_meta],
    )
    api.project.update_meta(project.id, meta.to_json())

    for ds_name, folders in ds_name_to_folders.items():

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        for folder in folders:

            if folder[:3] == "day":
                time_tag = sly.Tag(day_meta)
            else:
                time_tag = sly.Tag(night_meta)

            curr_data_path = os.path.join(dataset_path, folder, folder)
            curr_ann_path = os.path.join(anns_pathes, folder)

            if ds_name == "train":
                for subfolder in os.listdir(curr_data_path):
                    images_path = os.path.join(curr_data_path, subfolder, "frames")
                    ann_path_traff = os.path.join(curr_ann_path, subfolder, "frameAnnotationsBOX.csv")
                    ann_path = os.path.join(curr_ann_path, subfolder, "frameAnnotationsBULB.csv")
                    im_name_to_data_traff = defaultdict(list)
                    if file_exists(ann_path_traff):
                        with open(ann_path_traff, "r") as file:
                            csvreader = csv.reader(file)
                            for idx, row in enumerate(csvreader):
                                if idx == 0:
                                    continue
                                curr_data = row[0].split(";")
                                im_name_to_data_traff[curr_data[0].split("/")[1]].append(curr_data[1:])

                    im_name_to_data = defaultdict(list)
                    if file_exists(ann_path):
                        with open(ann_path, "r") as file:
                            csvreader = csv.reader(file)
                            for idx, row in enumerate(csvreader):
                                if idx == 0:
                                    continue
                                curr_data = row[0].split(";")
                                im_name_to_data[curr_data[0].split("/")[1]].append(curr_data[1:])

                        images_names = os.listdir(images_path)

                        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

                        for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                            img_pathes_batch = [
                                os.path.join(images_path, image_name)
                                for image_name in images_names_batch
                            ]

                            img_infos = api.image.upload_paths(
                                dataset.id, images_names_batch, img_pathes_batch
                            )
                            img_ids = [im_info.id for im_info in img_infos]

                            anns = [create_ann(image_path) for image_path in img_pathes_batch]
                            api.annotation.upload_anns(img_ids, anns)

                            progress.iters_done_report(len(images_names_batch))

            else:
                images_path = os.path.join(curr_data_path, "frames")
                ann_path = os.path.join(curr_ann_path, "frameAnnotationsBOX.csv")
                im_name_to_data_traff = defaultdict(list)
                if file_exists(ann_path_traff):
                    with open(ann_path_traff, "r") as file:
                        csvreader = csv.reader(file)
                        for idx, row in enumerate(csvreader):
                            if idx == 0:
                                continue
                            curr_data = row[0].split(";")
                            im_name_to_data_traff[curr_data[0].split("/")[1]].append(curr_data[1:])

                im_name_to_data = defaultdict(list)
                if file_exists(ann_path):
                    with open(ann_path, "r") as file:
                        csvreader = csv.reader(file)
                        for idx, row in enumerate(csvreader):
                            if idx == 0:
                                continue
                            curr_data = row[0].split(";")
                            im_name_to_data[curr_data[0].split("/")[1]].append(curr_data[1:])

                    images_names = os.listdir(images_path)

                    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

                    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                        img_pathes_batch = [
                            os.path.join(images_path, image_name) for image_name in images_names_batch
                        ]

                        img_infos = api.image.upload_paths(
                            dataset.id, images_names_batch, img_pathes_batch
                        )
                        img_ids = [im_info.id for im_info in img_infos]

                        anns = [create_ann(image_path) for image_path in img_pathes_batch]
                        api.annotation.upload_anns(img_ids, anns)

                        progress.iters_done_report(len(images_names_batch))


    return project
