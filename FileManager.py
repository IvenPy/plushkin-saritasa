class FileManager:

    def __init__(self, clone_groups, exceptions,
                 sc_files_num, sc_fold_num, fold_name):
        self.clone_groups = dict(clone_groups)  # dict: {group_id:[file_clones]}
        self.unavailable_files = exceptions  # set: {file}
        self.scanned_files_num = sc_files_num  #
        self.scanned_folders_num = sc_fold_num
        self.duplications_num = len(clone_groups)
        self.name_scanned_folder = fold_name