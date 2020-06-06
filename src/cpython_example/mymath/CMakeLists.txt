# src folder name is used as the target name 
get_filename_component(TARGET ${CMAKE_CURRENT_SOURCE_DIR} NAME)

Python3_add_library (${TARGET} SHARED "main.c")
set_target_properties(${TARGET} PROPERTIES SUFFIX ${PYTHON_MODULE_EXTENSION})

#IMPORTED_LOCATION IMPORTED_IMPLIB
get_target_property(PROP Python3::Python IMPORTED_IMPLIB)
message(STATUS ${Python3_LIBRARIES})

# install pyd files one directory structure UP in the destination as 
# CMAKE_CURRENT_SOURCE_DIR is holding the source files of the MODULE
# which matches the name of CMAKE_CURRENT_SOURCE_DIR
get_filename_component(CURRENT_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR} DIRECTORY)
if(${SRC_DIR} STREQUAL ${CURRENT_SRC_DIR}) 
    set(DST_DIR ".") # if parent is the base folder
else()
    file(RELATIVE_PATH DST_DIR ${SRC_DIR} ${CURRENT_SRC_DIR})
endif()
install(TARGETS ${TARGET} DESTINATION ${DST_DIR} COMPONENT "EXT")
