from imports import *


class OntologyEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ontology Editor")

        self.root.geometry("1200x600")

        self.onto = get_ontology("l2.rdf").load()
        self.tabControl = ttk.Notebook(self.root)

        self.class_hierarchy_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.class_hierarchy_frame, text='Иерархия классов')
        self.class_hierarchy_listbox = tk.Listbox(self.class_hierarchy_frame, width=100, height=30)
        self.class_hierarchy_listbox.pack(pady=10)

        self.objects_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.objects_frame, text='Объекты')
        self.objects_listbox = tk.Listbox(self.objects_frame, width=100, height=30)
        self.objects_listbox.pack(pady=10)

        self.object_relations_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.object_relations_frame, text='Связи между объектами')
        self.object_relations_listbox = tk.Listbox(self.object_relations_frame, width=100, height=30)
        self.object_relations_listbox.pack(pady=10)

        self.create_class_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.create_class_frame, text='Создание класса')

        self.class_name_label = ttk.Label(self.create_class_frame, text="Название класса:")
        self.class_name_label.grid(row=0, column=0, sticky=tk.W)
        self.class_name_entry = ttk.Entry(self.create_class_frame)
        self.class_name_entry.grid(row=0, column=1)

        self.superclass_label = ttk.Label(self.create_class_frame, text="Надкласс:")
        self.superclass_label.grid(row=1, column=0, sticky=tk.W)
        self.superclass_var = tk.StringVar(value="Хирургия")
        self.superclass_combobox = ttk.Combobox(self.create_class_frame, textvariable=self.superclass_var,
                                                state="readonly")
        self.superclass_combobox.grid(row=1, column=1)
        self.superclass_combobox['values'] = [cls.name for cls in self.onto.classes()]

        self.create_individ_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.create_individ_frame, text='Создание объекта')

        self.individ_name_label = ttk.Label(self.create_individ_frame, text="Название объекта:")
        self.individ_name_label.grid(row=0, column=0, sticky=tk.W)
        self.individ_name_entry = ttk.Entry(self.create_individ_frame)
        self.individ_name_entry.grid(row=0, column=1)

        self.individ_class_label = ttk.Label(self.create_individ_frame, text="Класс:")
        self.individ_class_label.grid(row=1, column=0, sticky=tk.W)
        self.individ_class_var = tk.StringVar(value="Хирургия")
        self.individ_class_combobox = ttk.Combobox(self.create_individ_frame, textvariable=self.individ_class_var,
                                                   state="readonly")
        self.individ_class_combobox.grid(row=1, column=1)
        self.individ_class_combobox['values'] = [cls.name for cls in self.onto.classes()]

        self.create_relation_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.create_relation_frame, text='Создание связи')

        self.first_individ_class_label = ttk.Label(self.create_relation_frame, text="Класс первого объекта::")
        self.first_individ_class_label.grid(row=0, column=0, sticky=tk.W)
        self.first_individ_class_var = tk.StringVar(value="Хирургия")
        self.first_individ_class_combobox = ttk.Combobox(self.create_relation_frame,
                                                         textvariable=self.first_individ_class_var,
                                                         state="readonly")
        self.first_individ_class_combobox.grid(row=0, column=1)
        self.first_individ_class_combobox['values'] = [cls.name for cls in self.onto.classes()]

        self.first_individ_name_label = ttk.Label(self.create_relation_frame, text="Название первого объекта:")
        self.first_individ_name_label.grid(row=1, column=0, sticky=tk.W)
        self.first_individ_name_entry = ttk.Entry(self.create_relation_frame)
        self.first_individ_name_entry.grid(row=1, column=1)

        self.relation_name_label = ttk.Label(self.create_relation_frame, text="Название связи:")
        self.relation_name_label.grid(row=2, column=0, sticky=tk.W)
        self.relation_name_entry = ttk.Entry(self.create_relation_frame)
        self.relation_name_entry.grid(row=2, column=1)

        self.second_individ_class_label = ttk.Label(self.create_relation_frame, text="Класс второго объекта::")
        self.second_individ_class_label.grid(row=3, column=0, sticky=tk.W)
        self.second_individ_class_var = tk.StringVar(value="Хирургия")
        self.second_individ_class_combobox = ttk.Combobox(self.create_relation_frame,
                                                          textvariable=self.second_individ_class_var,
                                                          state="readonly")
        self.second_individ_class_combobox.grid(row=3, column=1)
        self.second_individ_class_combobox['values'] = [cls.name for cls in self.onto.classes()]

        self.second_individ_name_label = ttk.Label(self.create_relation_frame, text="Название второго объекта:")
        self.second_individ_name_label.grid(row=4, column=0, sticky=tk.W)
        self.second_individ_name_entry = ttk.Entry(self.create_relation_frame)
        self.second_individ_name_entry.grid(row=4, column=1)

        self.first_individ_class_label.grid(row=0, column=0, sticky=tk.W, pady=10)
        self.first_individ_class_combobox.grid(row=0, column=1, pady=10)
        self.first_individ_name_label.grid(row=1, column=0, sticky=tk.W, pady=10)
        self.first_individ_name_entry.grid(row=1, column=1, pady=10)
        self.relation_name_label.grid(row=2, column=0, sticky=tk.W, pady=10)
        self.relation_name_entry.grid(row=2, column=1, pady=10)
        self.second_individ_class_label.grid(row=3, column=0, sticky=tk.W, pady=10)
        self.second_individ_class_combobox.grid(row=3, column=1, pady=10)
        self.second_individ_name_label.grid(row=4, column=0, sticky=tk.W, pady=10)
        self.second_individ_name_entry.grid(row=4, column=1, pady=10)

        self.delete_class_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.delete_class_frame, text='Удаление класса')

        self.delete_class_name_label = ttk.Label(self.delete_class_frame, text="Название класса:")
        self.delete_class_name_label.grid(row=1, column=0, sticky=tk.W)
        self.delete_class_name_entry = ttk.Entry(self.delete_class_frame)
        self.delete_class_name_entry.grid(row=1, column=1)

        self.delete_individ_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.delete_individ_frame, text='Удаление объекта')

        self.delete_individ_name_label = ttk.Label(self.delete_individ_frame, text="Название объекта:")
        self.delete_individ_name_label.grid(row=1, column=0, sticky=tk.W)
        self.delete_individ_name_entry = ttk.Entry(self.delete_individ_frame)
        self.delete_individ_name_entry.grid(row=1, column=1)

        self.delete_relation_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.delete_relation_frame, text='Удаление связи')

        self.delete_relation_first_individ_name_label = ttk.Label(self.delete_relation_frame,
                                                                  text="Название первого объекта:")
        self.delete_relation_first_individ_name_label.grid(row=0, column=0, sticky=tk.W)
        self.delete_relation_first_individ_name_entry = ttk.Entry(self.delete_relation_frame)
        self.delete_relation_first_individ_name_entry.grid(row=0, column=1)

        self.delete_relation_name_label = ttk.Label(self.delete_relation_frame, text="Название связи:")
        self.delete_relation_name_label.grid(row=1, column=0, sticky=tk.W)
        self.delete_relation_name_entry = ttk.Entry(self.delete_relation_frame)
        self.delete_relation_name_entry.grid(row=1, column=1)

        self.delete_relation_second_individ_name_label = ttk.Label(self.delete_relation_frame, text="Название второго объекта:")
        self.delete_relation_second_individ_name_label.grid(row=3, column=0, sticky=tk.W)
        self.delete_relation_second_individ_name_entry = ttk.Entry(self.delete_relation_frame)
        self.delete_relation_second_individ_name_entry.grid(row=3, column=1)

        self.change_class_name_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.change_class_name_frame, text='Изменение класса')

        self.old_class_name_label = ttk.Label(self.change_class_name_frame,
                                                                  text="Старое название класса:")
        self.old_class_name_label.grid(row=0, column=0, sticky=tk.W)
        self.old_class_name_entry = ttk.Entry(self.change_class_name_frame)
        self.old_class_name_entry.grid(row=0, column=1)

        self.new_class_name_label = ttk.Label(self.change_class_name_frame, text="Новое название класса:")
        self.new_class_name_label.grid(row=1, column=0, sticky=tk.W)
        self.new_class_name_entry = ttk.Entry(self.change_class_name_frame)
        self.new_class_name_entry.grid(row=1, column=1)

        self.change_individ_name_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.change_individ_name_frame, text='Изменение объекта')

        self.old_individ_name_label = ttk.Label(self.change_individ_name_frame,
                                              text="Старое название объекта:")
        self.old_individ_name_label.grid(row=0, column=0, sticky=tk.W)
        self.old_individ_name_entry = ttk.Entry(self.change_individ_name_frame)
        self.old_individ_name_entry.grid(row=0, column=1)

        self.new_individ_name_label = ttk.Label(self.change_individ_name_frame, text="Новое название объекта:")
        self.new_individ_name_label.grid(row=1, column=0, sticky=tk.W)
        self.new_individ_name_entry = ttk.Entry(self.change_individ_name_frame)
        self.new_individ_name_entry.grid(row=1, column=1)

        self.sparql_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.sparql_frame, text='SPARQL')

        self.query_entry = tk.Text(self.sparql_frame, width=100, height=10)
        self.query_entry.pack(pady=10)
        self.query_entry.insert("1.0",   """SELECT ?individual
WHERE {
    ?individual rdf:type <http://www.semanticweb.org/user/ontologies/2024/2/untitled-ontology-3#Инструменты>
}"""
                                )

        self.result_text = tk.Text(self.sparql_frame, width=100, height=20)
        self.result_text.pack(pady=10)

        self.tabControl.pack(expand=1, fill="both")

        self.get_class_hierarchy_button = tk.Button(self.class_hierarchy_frame, text="Получить иерархию классов",
                                                    command=self.get_class_hierarchy)
        self.get_class_hierarchy_button.pack(pady=5)

        self.get_objects_button = tk.Button(self.objects_frame, text="Получить объекты", command=self.get_objects)
        self.get_objects_button.pack(pady=5)

        self.get_object_relations_button = tk.Button(self.object_relations_frame,
                                                     text="Получить связи между объектами",
                                                     command=self.get_object_relations)
        self.get_object_relations_button.pack(pady=5)

        self.create_class_button = tk.Button(self.create_class_frame,
                                             text="Создать класс",
                                             command=self.create_class)

        self.create_class_button.grid(row=2, column=0, pady=5)

        self.create_individ_button = tk.Button(self.create_individ_frame,
                                               text="Создать объект",
                                               command=self.create_individ)

        self.create_individ_button.grid(row=2, column=0, pady=5)

        self.create_relation_button = tk.Button(self.create_relation_frame,
                                                text="Создать связь",
                                                command=self.create_relation)

        self.create_relation_button.grid(row=5, column=0, pady=5)

        self.delete_class_button = tk.Button(self.delete_class_frame,
                                                text="Удалить класс",
                                                command=self.delete_class)

        self.delete_class_button.grid(row=5, column=0, pady=5)

        self.delete_individ_button = tk.Button(self.delete_individ_frame,
                                             text="Удалить объект",
                                             command=self.delete_individ)

        self.delete_individ_button.grid(row=5, column=0, pady=5)

        self.delete_relation_button = tk.Button(self.delete_relation_frame,
                                               text="Удалить объект",
                                               command=self.delete_relation)

        self.delete_relation_button.grid(row=5, column=0, pady=5)

        self.change_class_name_button = tk.Button(self.change_class_name_frame,
                                                text="Изменить класс",
                                                command=self.change_class)

        self.change_class_name_button.grid(row=5, column=0, pady=5)

        self.change_individ_name_button = tk.Button(self.change_individ_name_frame,
                                                  text="Изменить объект",
                                                  command=self.change_individ)

        self.change_individ_name_button.grid(row=5, column=0, pady=5)

        self.execute_query_button = tk.Button(self.sparql_frame, text="Выполнить запрос", command=self.execute_query)
        self.execute_query_button.pack(pady=5)

    def get_class_hierarchy(self):
        self.class_hierarchy_listbox.delete(0, tk.END)

        base_class = self.onto.Хирургия
        self.build_class_hierarchy(base_class, self.class_hierarchy_listbox)

    def build_class_hierarchy(self, cls, listbox, depth=0):
        class_name = cls.name
        listbox.insert(tk.END, "  " * depth + class_name)
        for subclass in cls.subclasses():
            self.build_class_hierarchy(subclass, listbox, depth + 1)

    def get_objects(self):
        self.objects_listbox.delete(0, tk.END)

        added_objects = set()

        for cls in self.onto.classes():
            self.objects_listbox.insert(tk.END, f"Класс {cls.name}")
            instances = list(cls.instances())
            for instance in instances:
                if instance.name not in added_objects:
                    self.objects_listbox.insert(tk.END, instance.name)
                    added_objects.add(instance.name)
            self.objects_listbox.insert(tk.END, "")

    def get_object_relations(self):
        self.object_relations_listbox.delete(0, tk.END)

        classes = list(self.onto.classes())

        added_objects = set()

        for cls in classes:
            instances = list(cls.instances())
            for instance in instances:
                if instance.name not in added_objects:
                    added_objects.add(instance.name)
                    relations = instance.get_properties()
                    if relations:
                        for relation in relations:
                            if isinstance(relation, ObjectPropertyClass):
                                related_objects = getattr(instance, relation.name)
                                for related_object in related_objects:
                                    self.object_relations_listbox.insert(
                                        tk.END, f"{instance.name} {relation.name} {related_object.name}")
                            else:
                                value = getattr(instance, relation.name)
                                self.object_relations_listbox.insert(
                                    tk.END, f"{instance.name} {relation.name} {value}")
                self.object_relations_listbox.insert(tk.END, "")

    def create_class(self):
        class_name = self.class_name_entry.get()
        superclass = self.superclass_var.get()

        classes = [cls.name for cls in self.onto.classes()]

        if class_name in classes:
            print(f"ERROR: Класс с именем {class_name} уже существует.")
        else:
            with self.onto:
                new_class = types.new_class(class_name, (self.onto[superclass],))

            self.onto.save(file="l2.rdf")

    def create_individ(self):
        individ_name = self.individ_name_entry.get()
        class_name = self.individ_class_var.get()

        instances = [instance.name for instance in self.onto[class_name].instances()]
        classes = [cls.name for cls in self.onto.classes()]

        if individ_name in instances:
            print(f"ERROR: Объект с именем {class_name} уже существует.")
        elif individ_name in classes:
            print(f"ERROR: Имя {class_name} не валидно.")
        else:
            new_individ = self.onto[class_name](individ_name)
            self.onto.save(file="l2.rdf")

    def create_relation(self):
        first_individ_class = self.first_individ_class_var.get()
        first_individ_name = self.first_individ_name_entry.get()
        relation_name = self.relation_name_entry.get()
        second_individ_class = self.second_individ_class_var.get()
        second_individ_name = self.second_individ_name_entry.get()

        obj_1 = getattr(self.onto, first_individ_name)
        obj_2 = getattr(self.onto, second_individ_name)

        if not obj_1:
            print(f"ERROR: Объект с именем {first_individ_name} не существует.")
            return
        if not obj_2:
            print(f"ERROR: Объект с именем {second_individ_name} не существует.")
            return

        if hasattr(obj_1, relation_name):
            print(f"ERROR: Связь {relation_name} уже существует.")
        else:
            with self.onto:
                prop = types.new_class(relation_name, (ObjectProperty, FunctionalProperty))
                prop.domain = [getattr(self.onto, first_individ_class)]
                prop.range = [getattr(self.onto, second_individ_class)]
            setattr(obj_1, relation_name, [obj_2])

        self.onto.save(file="l2.rdf")

    def delete_class(self):
        class_name = self.delete_class_name_entry.get()

        classes = [cls.name for cls in self.onto.classes()]

        if class_name not in classes:
            print(f"ERROR: Класса с именем {class_name} не существует.")

        else:
            with self.onto:
                for relation in self.onto.object_properties():
                    if relation.range and relation.range[0] == self.onto[class_name]:
                        destroy_entity(relation)
                destroy_entity(self.onto[class_name])
            self.onto.save(file="l2.rdf")

    def delete_individ(self):
        individ_name = self.delete_individ_name_entry.get()

        obj = getattr(self.onto, individ_name)

        if not obj:
            print(f"ERROR: Объект с именем {individ_name} не существует.")

        else:
            with self.onto:
                for relation in self.onto.object_properties():
                    for triple in relation.get_relations():
                        if triple[2] == obj:
                            destroy_entity(relation)
                destroy_entity(obj)
            self.onto.save(file="l2.rdf")

    def delete_relation(self):
        first_individ_name = self.delete_relation_first_individ_name_entry.get()
        relation_name = self.delete_relation_name_entry.get()
        second_individ_name = self.delete_relation_second_individ_name_entry.get()

        obj_1 = getattr(self.onto, first_individ_name)
        obj_2 = getattr(self.onto, second_individ_name)

        if not obj_1:
            print(f"ERROR: Объект с именем {first_individ_name} не существует.")
            return
        if not obj_2:
            print(f"ERROR: Объект с именем {second_individ_name} не существует.")
            return

        relations = obj_1.get_properties()

        for relation in relations:
            if isinstance(relation, ObjectPropertyClass) and relation.name == relation_name:
                related_objects = getattr(obj_1, relation.name)
                if obj_2 in related_objects:
                    related_objects.remove(obj_2)
                    print(f"Связь между {obj_1.name} и {obj_2.name} с именем {relation_name} удалена.")

        self.onto.save(file="l2.rdf")

    def change_class(self):
        old_class_name = self.old_class_name_entry.get()
        new_class_name = self.new_class_name_entry.get()

        classes = [cls.name for cls in self.onto.classes()]

        if old_class_name not in classes:
            print(f"ERROR: Класса с именем {old_class_name} не существует.")
            return
        if new_class_name in classes:
            print(f"ERROR: Класс с именем {new_class_name} уже существует.")
            return

        old_class = getattr(self.onto, old_class_name)

        old_class.name = new_class_name

        self.onto.save(file="l2.rdf")

    def change_individ(self):
        old_individ_name = self.old_individ_name_entry.get()
        new_individ_name = self.new_individ_name_entry.get()

        obj_1 = getattr(self.onto, old_individ_name)
        obj_2 = getattr(self.onto, new_individ_name)

        if not obj_1:
            print(f"ERROR: Объект с именем {old_individ_name} не существует.")
            return
        if obj_2:
            print(f"ERROR: Объект с именем {new_individ_name} уже существует.")
            return

        obj_1.name = new_individ_name

    def execute_query(self):
        query = self.query_entry.get("1.0", tk.END)

        odj = getattr(self.onto, "Инструменты")

        a = odj.iri

        with self.onto:
            results = default_world.sparql(query)

        self.result_text.delete("1.0", tk.END)
        for result in results:
            self.result_text.insert(tk.END, f"{result}\n")
