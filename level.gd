extends Node2D
class_name Level
const _DIALOG_SCREEN: PackedScene = preload("res://dialog_screen.tscn")
var _dialog_data: Dictionary={
	0:{"faceset":"res://WhatsApp Image 2025-09-14 at 9.19.51 PM.jpeg",
		"title":"Japones gostoso",
		"dialog":"Esse cara tem aura"},
	1:{"faceset":"res://WhatsApp Image 2025-09-14 at 9.19.51 PM.jpeg",
		"title":"Japones gostoso do mal",
		"dialog":"Esse Nao tem aura"}
}	
@export_category("Objects")
@export var _hud:CanvasLayer=null
func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_select"):
		var new_dialog: Dialog_Screen=_DIALOG_SCREEN.instantiate()
		new_dialog.data=_dialog_data
		_hud.add_child(new_dialog)
