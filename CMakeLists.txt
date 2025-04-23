cmake_minimum_required(VERSION 3.20)
project(watch-sync)

add_executable(${PROJECT_NAME}
	./src/main.c
	# ./src/debug.c
	# ./src/environment.c
	# ./src/json.c
	# ./src/log.c
	# ./src/sql.c
)

target_include_directories(${PROJECT_NAME} PRIVATE inc/)

target_link_libraries(${PROJECT_NAME} PRIVATE -lb64 -lcjson -lsqlite3)

target_compile_options(${PROJECT_NAME} PRIVATE
	$<$<C_COMPILER_ID:GNU,Clang,AppleClang>:-Wall -Wextra -Wpedantic -Werror -fno-omit-frame-pointer>
	$<$<AND:$<C_COMPILER_ID:GNU,Clang,AppleClang>,$<CONFIG:Release>>:-O3>
	$<$<AND:$<C_COMPILER_ID:GNU,Clang,AppleClang>,$<CONFIG:Debug>>:-Og -g>
)
